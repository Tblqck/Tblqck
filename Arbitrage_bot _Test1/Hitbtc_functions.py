





import requests
import json
from datetime import datetime
from exchange_markets import exchange_market_lists

def fetch_present_data_and_save_hitbtc(asset):
    base_url = "https://api.hitbtc.com/api/3/public/ticker"
    trading_pair = exchange_market_lists['HitBTC'][asset]
    url = f"{base_url}/{trading_pair}"

    response = requests.get(url)

    def calculate_liquidity_score(data):
        # Modify this logic based on your specific requirements
        liquidity_score = (float(data['last']) * float(data['volume'])) / 1000
        return round(liquidity_score, 2)

    if response.status_code == 200:
        data = response.json()

        liquidity_score = calculate_liquidity_score(data)

        present_data = {
            'exchange': 'HitBTC',
            'asset': asset,
            'trading_pair': trading_pair,
            'price': float(data['last']),
            'volume': float(data['volume']),
            'liquidity_score': liquidity_score,
            'fetch_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
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
    fetch_present_data_and_save_hitbtc(asset_to_fetch)





