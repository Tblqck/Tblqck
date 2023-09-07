

import requests
import json
from datetime import datetime, timedelta
from exchange_markets import exchange_market_lists  # Make sure this import works

def fetch_present_data_and_save_bitmart(asset):
    base_url = 'https://api-cloud.bitmart.com'
    endpoint = '/spot/quotation/v3/tickers'
    url = base_url + endpoint

    response = requests.get(url)
    data = response.json()

    def calculate_liquidity_score(price, volume):
        # Modify this logic based on your specific requirements
        liquidity_score = (price * volume) / 1000
        return round(liquidity_score, 2)

    if response.status_code == 200:
        trading_pair = exchange_market_lists.get('BitMart', {}).get(asset)
        if trading_pair is not None:
            for ticker in data['data']:
                if ticker[0] == trading_pair:
                    price = float(ticker[1])
                    volume = float(ticker[2])
                    liquidity_score = calculate_liquidity_score(price, volume)

                    present_data = {
                        'exchange': 'BitMart',
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
                    break
            else:
                print(f'No data found for asset {asset} on BitMart')
        else:
            print(f'No trading pair defined for asset {asset} on BitMart')
    else:
        print('Error occurred. Status Code:', response.status_code)

if __name__ == '__main__':
    asset_to_fetch = input("Enter the asset you want to fetch present data for: ").strip().upper()
    fetch_present_data_and_save_bitmart(asset_to_fetch)


#--------------------------------------------------------------------------


def fetch_historical_data_and_save_bitmart(asset):  # Changed function name
    interval = '1m'  # 1 minute interval
    limit = 60  # Retrieve data for the past 60 minutes
    base_url = 'https://api-cloud.bitmart.com/spot/quotation/v3/lite-klines'
    trading_pair = exchange_market_lists['BitMart'][asset]
    
    params = {
        'symbol': trading_pair,
        'step': 1,  # K-Line step (in minutes)
        'limit': limit
    }
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()['data']
        historical_data = []

        for entry in data:
            timestamp = int(entry[0])  # The timestamp is in seconds
            if datetime.fromtimestamp(timestamp) > datetime.now() - timedelta(days=1):
                open_price = float(entry[1])
                high_price = float(entry[2])
                low_price = float(entry[3])
                close_price = float(entry[4])

                readable_timestamp = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
                historical_data.append({
                    'exchange': 'BitMart',
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
    fetch_historical_data_and_save_bitmart(asset_to_fetch)



