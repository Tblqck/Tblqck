


import requests
import json
from exchange_markets import exchange_market_lists

def fetch_present_data_and_save_okex(asset):
    base_url = 'https://www.okex.com/api/v5/market/history-mark-price-candles'
    trading_pair = exchange_market_lists['OKEx'][asset]
    params = {'instId': trading_pair}
    
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json().get('data', [])
        if data:
            candle = data[0]
            timestamp = candle[0]
            open_price = candle[1]
            high_price = candle[2]
            low_price = candle[3]
            close_price = candle[4]
            volume = candle[5]  # Adding this line
            
            present_data = {
                'exchange': 'OKEx',
                'asset': asset,
                'trading_pair': trading_pair,
                'timestamp': timestamp,  # No need to convert to datetime
                'open': open_price,
                'high': high_price,
                'low': low_price,
                'close': close_price,
                'volume': volume  # Adding this line
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
            print(f"No data found for {trading_pair} on OKEx.")
    else:
        print('Error occurred. Status Code:', response.status_code)

if __name__ == '__main__':
    asset_to_fetch = input("Enter the asset you want to fetch data for: ").strip().upper()
    fetch_present_data_and_save_okex(asset_to_fetch)



