# 📊 CryptoSentiment Pulse

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/YOUR_GITHUB_USERNAME/CryptoSentiment-Pulse)
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io)

**CryptoSentiment Pulse** is a Full-Stack Data Analytics dashboard that provides real-time cryptocurrency tracking combined with Natural Language Processing (NLP) to gauge market sentiment.

### 🚀 Live Demo
[Insert your Deployment URL here]

---

### 🌟 Key Features
* **Real-time Data:** Fetches live crypto prices via the CoinGecko API.
* **NLP Analysis:** Uses `TextBlob` to calculate sentiment polarity (Positive/Negative) on market headlines.
* **Interactive Visualization:** Dynamic charts using Plotly.
* **Persistence:** Built-in SQLite database to track trending user searches.

### 🛠 Tech Stack
* **Python 3.10**
* **Streamlit** (Frontend)
* **SQLite** (Database)
* **TextBlob** (NLP)
* **Plotly** (Viz)

---

### ⚡ How to Run

#### Option 1: GitHub Codespaces (Recommended)
1. Click the **"Open in GitHub Codespaces"** badge above.
2. Wait for the environment to build.
3. In the terminal, run:
   ```bash
   streamlit run app.py

How to run locally
Clone the repo.

Install dependencies:

Bash

pip install -r requirements.txt
python -m textblob.download_corpora

Run the app:

Bash

streamlit run app.py
