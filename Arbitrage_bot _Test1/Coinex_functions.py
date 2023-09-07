


import requests
import json
from datetime import datetime
from exchange_markets import exchange_market_lists

def fetch_present_data_and_save_coinex(asset):
    base_url = "https://api.coinex.com"
    endpoint = "/v1/market/ticker"
    market = exchange_market_lists['Coinex'][asset]  # Get the Coinex market symbol

    params = {"market": market}
    url = base_url + endpoint

    def calculate_liquidity_score(vol, last):
        # Modify this logic based on your specific requirements
        liquidity_score = (float(vol) * float(last)) / 1000
        return round(liquidity_score, 2)

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        ticker_data = data['data']['ticker']
        vol = ticker_data['vol']
        last = ticker_data['last']
        liquidity_score = calculate_liquidity_score(vol, last)

        present_data = {
            'exchange': 'Coinex',
            'asset': asset,
            'trading_pair': market,
            'price': last,
            'volume': vol,
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
    fetch_present_data_and_save_coinex(asset_to_fetch)





