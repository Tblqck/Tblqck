

import requests
import json
from datetime import datetime, timedelta
from exchange_markets import exchange_market_lists  # Use the same exchange_market_lists for Crypto.com

def fetch_present_data_and_save_crypto(asset):
    base_url = 'https://api.crypto.com/v2/public/get-ticker'
    exchange = 'Crypto.com'  # Specify the exchange
    trading_pair = exchange_market_lists[exchange][asset]
    params = {'instrument_name': trading_pair}
    response = requests.get(base_url, params=params)

    def calculate_liquidity_score(price, volume):
        # Modify this logic based on your specific requirements
        liquidity_score = (price * volume) / 1000
        return round(liquidity_score, 2)

    if response.status_code == 200:
        data = response.json()['result']['data'][0]
        price = float(data['a'])
        volume = float(data['v'])
        liquidity_score = calculate_liquidity_score(price, volume)

        present_data = {
            'exchange': exchange,
            'asset': asset,
            'trading_pair': trading_pair,
            'price': price,
            'volume': volume,
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
    fetch_present_data_and_save_crypto(asset_to_fetch)
    
    
    
