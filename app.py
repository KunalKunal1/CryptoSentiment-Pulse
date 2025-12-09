import streamlit as st
import plotly.express as px
from src import api_client, nlp_engine, db_manager

import subprocess
import sys
subprocess.check_call([sys.executable, "-m", "textblob.download_corpora"])
# -------------------------
# Page Config
st.set_page_config(
    page_title="CryptoSentiment Pulse",
    page_icon="📊",
    layout="wide"
)

# Initialize DB
db_manager.init_db()

# --- SIDEBAR ---
st.sidebar.title("Configuration")
selected_coin = st.sidebar.selectbox(
    "Select Cryptocurrency",
    ("bitcoin", "ethereum", "dogecoin", "solana", "ripple")
)

st.sidebar.markdown("---")
st.sidebar.info("This app uses NLP to analyze mock news sentiment and fetches real-time prices via CoinGecko.")

# --- MAIN PAGE ---
st.title(f"📊 CryptoSentiment Pulse: {selected_coin.upper()}")

# 1. Fetch & Display Price Data
col1, col2, col3 = st.columns(3)

price_data = api_client.get_coin_price(selected_coin)

if price_data:
    current_price = price_data['price']
    change = price_data['change_24h']
    
    col1.metric("Current Price (USD)", f"${current_price:,.2f}", f"{change:.2f}%")
    
    # Log the search
    db_manager.log_search(selected_coin)
else:
    col1.error("Failed to fetch price data.")

# 2. News & Sentiment Analysis
st.subheader("📰 Recent News & Sentiment Analysis")

news_items = api_client.get_mock_news(selected_coin.capitalize())
df_sentiment = nlp_engine.process_news_sentiment(news_items)

# Display Data Table
st.dataframe(df_sentiment, use_container_width=True)

# 3. Visualization
st.subheader("📈 Sentiment Visualization")

if not df_sentiment.empty:
    # Bar Chart for Sentiment Scores
    fig = px.bar(
        df_sentiment, 
        x='Headline', 
        y='Score', 
        color='Sentiment',
        color_discrete_map={"Positive 🚀": "green", "Negative 📉": "red", "Neutral 😐": "gray"},
        title="Sentiment Score per Headline"
    )
    st.plotly_chart(fig, use_container_width=True)

    # Average Sentiment
    avg_score = df_sentiment['Score'].mean()
    st.info(f"Overall Sentiment Score: {avg_score:.2f} (Scale: -1 to 1)")

# 4. Database (Search History)
st.markdown("---")
st.subheader("🔍 Popular Searches (From Local DB)")
top_searches = db_manager.get_top_searches()

if not top_searches.empty:
    st.bar_chart(top_searches.set_index("coin_id"))
else:
    st.write("No search history yet.")