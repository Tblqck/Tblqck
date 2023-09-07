

import requests
import json
from datetime import datetime
from exchange_markets import exchange_market_lists

def fetch_present_data_and_save_bittrex(asset):
    base_url = 'https://api.bittrex.com/v3/markets/{symbol}/ticker'
    trading_pair = exchange_market_lists['Bittrex'][asset]
    url = base_url.format(symbol=trading_pair)
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        present_data = {
            'exchange': 'Bittrex',
            'asset': asset,
            'trading_pair': trading_pair,
            'price': data['lastTradeRate'],
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
        print(f"Failed to fetch present data from Bittrex. Status code: {response.status_code}")

if __name__ == '__main__':
    asset_to_fetch = input("Enter the asset you want to fetch data for: ").strip().upper()
    fetch_present_data_and_save_bittrex(asset_to_fetch)
#-----------------------------------------

def fetch_historical_data_and_save_bittrex(asset):
    interval = 'MINUTE_1'  # 1-minute interval
    base_url = 'https://api.bittrex.com/v3/markets/{symbol}/candles/{interval}/recent'
    trading_pair = exchange_market_lists['Bittrex'][asset]
    
    url = base_url.format(symbol=trading_pair, interval=interval)
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        historical_data = []

        for candle in data:
            timestamp = candle['startsAt'][:-1]  # Remove the trailing 'Z'
            open_price = candle['open']
            high_price = candle['high']
            low_price = candle['low']
            close_price = candle['close']
            
            readable_timestamp = datetime.fromisoformat(timestamp).strftime('%Y-%m-%d %H:%M:%S')
            historical_data.append({
                'exchange': 'Bittrex',
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
    fetch_historical_data_and_save_bittrex(asset_to_fetch)


