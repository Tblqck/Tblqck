

import requests
import json
from datetime import datetime, timedelta
from exchange_markets import exchange_market_lists

def fetch_present_data_and_save_huobi(asset):
    base_url = 'https://api.huobi.pro/market/history/kline'
    trading_pair = exchange_market_lists['Huobi'][asset]
    
    # Define the parameters for the API request to fetch 1-day candle data
    params = {
        'symbol': trading_pair,
        'period': '1day',  # Specify the period of each candle (1 day)
        'size': 1  # Fetch one data point
    }
    
    response = requests.get(base_url, params=params)
    
    def calculate_liquidity_score(price, volume):
        # Modify this logic based on your specific requirements
        liquidity_score = (price * volume) / 1000
        return round(liquidity_score, 2)
    
    if response.status_code == 200:
        data = response.json()
        candle_data = data.get('data', [])
        
        if candle_data:
            candle = candle_data[0]
            timestamp = candle['id']
            readable_timestamp = datetime.fromtimestamp(timestamp // 1000).strftime('%Y-%m-%d %H:%M:%S')
            
            price = candle['close']  # Use the close price as the current price
            volume = candle['vol']  # Use the volume for the 1-day candle
            liquidity_score = calculate_liquidity_score(price, volume)

            present_data = {
                'exchange': 'Huobi',
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
            print(f'No candle data found for {asset} on Huobi.')
    else:
        print('Error occurred. Status Code:', response.status_code)

if __name__ == '__main__':
    asset_to_fetch = input("Enter the asset you want to fetch data for: ").strip().upper()
    fetch_present_data_and_save_huobi(asset_to_fetch)

    
#----------------------------------


def fetch_historical_data_and_save_huobi(asset):
    trading_pair = exchange_market_lists['Huobi'][asset]
    interval = '1min'  # 1-minute interval
    size = 1000  # Number of data points to fetch (adjust as needed)
    
    # Define the base URL for historical data
    base_url = f'https://api.huobi.pro/market/history/kline?symbol={trading_pair}&period={interval}&size={size}'
    
    # Send a GET request to Huobi's API
    response = requests.get(base_url)
    
    if response.status_code == 200:
        huobi_data = response.json()
        if 'data' in huobi_data:
            huobi_data = huobi_data['data']

            historical_data = []

            for entry in huobi_data:
                timestamp = entry['id']  # Timestamp from the exchange
                open_price = entry['open']
                high_price = entry['high']
                low_price = entry['low']
                close_price = entry['close']

                # Convert timestamp to a readable format
                readable_timestamp = timestamp_to_readable(timestamp)
                
                historical_data.append({
                    'exchange': 'Huobi',
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
            print(f'No data available from Huobi for {asset}.')
    else:
        print('Error occurred. Status Code:', response.status_code)

def timestamp_to_readable(timestamp):
    # Convert timestamp to a readable format
    return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

if __name__ == '__main__':
    asset_to_fetch = input("Enter the asset you want to fetch historical data for: ").strip().upper()
    fetch_historical_data_and_save_huobi(asset_to_fetch)
    
    
    
