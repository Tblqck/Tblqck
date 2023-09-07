

import requests
import json
from datetime import datetime
from exchange_markets import exchange_market_lists  # Assuming you have this module with exchange mappings

def fetch_and_save_bybit(asset):
    base_url = "https://api.bybit.com/v2/public/tickers"
    trading_pair = exchange_market_lists['Bybit'][asset]
    params = {"symbol": trading_pair}

    response = requests.get(base_url, params=params)

    def calculate_liquidity_score(last_price, volume_24h):
        # Modify this logic based on your specific requirements
        last_price = float(last_price)
        volume_24h = float(volume_24h)
        liquidity_score = (last_price * volume_24h) / 1000
        return round(liquidity_score, 2)

    if response.status_code == 200:
        data = response.json()
        ticker_info = data["result"][0]
        last_price = ticker_info["last_price"]
        volume_24h = ticker_info["volume_24h"]
        liquidity_score = calculate_liquidity_score(last_price, volume_24h)

        present_data = {
            "exchange": "Bybit",
            "asset": asset,
            "trading_pair": trading_pair,
            "last_price": last_price,
            "volume_24h": volume_24h,
            "liquidity_score": liquidity_score,
            "fetch_time": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }

        try:
            # Load existing data from JSON file
            with open('market_data.json', 'r') as market_data_file:
                existing_data = json.load(market_data_file)
        except (FileNotFoundError, json.JSONDecodeError):
            existing_data = []

        # Append the new present data to existing data
        existing_data.append(present_data)

        # Save the updated data to JSON file
        with open('market_data.json', 'w') as market_data_file:
            json.dump(existing_data, market_data_file, indent=4)
            print(f'{asset} present data appended to market_data.json')
    else:
        print('Error occurred. Status Code:', response.status_code)

if __name__ == '__main__':
    asset_to_fetch = input("Enter the asset you want to fetch data for: ").strip().upper()
    fetch_and_save_bybit(asset_to_fetch)








