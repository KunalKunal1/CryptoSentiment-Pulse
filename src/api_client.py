import requests
import random

def get_coin_price(coin_id):
    """
    Fetches current market data from CoinGecko.
    """
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        'ids': coin_id,
        'vs_currencies': 'usd',
        'include_24hr_change': 'true'
    }
    
    try:
        response = requests.get(url, params=params)
        data = response.json()
        if coin_id in data:
            return {
                'price': data[coin_id]['usd'],
                'change_24h': data[coin_id]['usd_24h_change']
            }
        return None
    except Exception as e:
        print(f"API Error: {e}")
        return None

def get_mock_news(coin_id):
    """
    Simulates fetching news headlines.
    """
    templates = [
        f"{coin_id} is skyrocketing after new regulation rumors.",
        f"Experts warn that {coin_id} might face a dip soon.",
        f"Investors are bullish on {coin_id} this week.",
        f"Tech issues reported on the {coin_id} network, slowing transactions.",
        f"{coin_id} adoption hits an all-time high in Europe.",
        f"Why {coin_id} is the future of decentralized finance."
    ]
    # Return 3 random headlines
    return random.sample(templates, 3)