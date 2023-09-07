

import requests
import json
from datetime import datetime, timedelta
from exchange_markets import exchange_market_lists

def fetch_present_data_and_save_binance(asset):
    base_url = 'https://api.binance.com/api/v3/ticker/24hr'
    trading_pair = exchange_market_lists['Binance'][asset]
    params = {'symbol': trading_pair}
    response = requests.get(base_url, params=params)

    def calculate_liquidity_score(price, volume):
        # Modify this logic based on your specific requirements
        liquidity_score = (price * volume) / 1000
        return round(liquidity_score, 2)

    if response.status_code == 200:
        data = response.json()
        price = float(data['lastPrice'])
        volume = float(data['quoteVolume'])
        liquidity_score = calculate_liquidity_score(price, volume)

        present_data = {
            'exchange': 'Binance',
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
    fetch_present_data_and_save_binance(asset_to_fetch)
#---------------------------------------------------------
def fetch_historical_data_and_save(asset):
    interval = '1m'  # 1 minute interval
    limit = 60  # Retrieve data for the past 60 minutes
    base_url = 'https://api.binance.com/api/v3/klines'
    trading_pair = exchange_market_lists['Binance'][asset]

    params = {
        'symbol': trading_pair,
        'interval': interval,
        'limit': limit
    }
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        historical_data = []

        for entry in data:
            timestamp = entry[0] / 1000  # Convert milliseconds to seconds
            if datetime.fromtimestamp(timestamp) > datetime.now() - timedelta(days=1):
                open_price = entry[1]
                high_price = entry[2]
                low_price = entry[3]
                close_price = entry[4]

                readable_timestamp = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
                historical_data.append({
                    'exchange': 'Binance',
                    'asset': asset,
                    'trading_pair': trading_pair,
                    'timestamp': readable_timestamp,
                    'open': open_price,
                    'high': high_price,
                    'low': low_price,
                    'close': close_price
                })

        try:
            # Load existing historical data from JSON file
            with open('his_market_data.json', 'r') as his_market_data_file:
                existing_data = json.load(his_market_data_file)
        except (FileNotFoundError, json.JSONDecodeError):
            existing_data = []

        # Append the new historical data to existing data
        existing_data.extend(historical_data)

        # Save the updated data to JSON file
        with open('his_market_data.json', 'w') as his_market_data_file:
            json.dump(existing_data, his_market_data_file, indent=4)
            print(f'Historical data for {asset} appended to his_market_data.json')
    else:
        print('Error occurred. Status Code:', response.status_code)

if __name__ == '__main__':
    asset_to_fetch = input("Enter the asset you want to fetch historical data for: ").strip().upper()
    fetch_historical_data_and_save(asset_to_fetch)

