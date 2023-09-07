



import requests
import json
from datetime import datetime
from exchange_markets import exchange_market_lists

def fetch_present_data_and_save_Cexio(asset):
    base_url = "https://cex.io/api"
    
    if 'CEX.IO' in exchange_market_lists and asset in exchange_market_lists['CEX.IO']:
        symbol = exchange_market_lists['CEX.IO'][asset]
        symbol1 = symbol['symbol1']
        symbol2 = symbol['symbol2']
    else:
        print(f"Fetching data is only supported for tokens listed in exchange_market_lists for 'CEX.IO'.")
        return

    endpoint = f"/ticker/{symbol1}/{symbol2}"
    url = base_url + endpoint

    response = requests.get(url)
    data = response.json()

    if 'pair' not in data:
        print(f"Data not found for {asset}.")
        return

    price = float(data['last'])
    volume = float(data['volume'])

    liquidity_score = calculate_liquidity_score(price, volume)

    present_data = {
        'exchange': 'CEX.IO',
        'asset': asset,
        'trading_pair': f"{symbol1}:{symbol2}",
        'price': price,
        'volume': volume,
        'liquidity_score': liquidity_score,
        'fetch_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }

    # Save the data to a JSON file
    try:
        with open('market_data.json', 'r') as market_data_file:
            existing_data = json.load(market_data_file)
    except (FileNotFoundError, json.JSONDecodeError):
        existing_data = []

    existing_data.append(present_data)

    with open('market_data.json', 'w') as market_data_file:
        json.dump(existing_data, market_data_file, indent=4)
        print(f'{asset} present data appended to market_data.json')

def calculate_liquidity_score(price, volume):
    # Modify this logic based on your specific requirements
    liquidity_score = (price * volume) / 1000
    return round(liquidity_score, 2)

if __name__ == '__main__':
    asset_to_fetch = input("Enter the asset you want to fetch data for: ").strip().upper()
    fetch_present_data_and_save_Cexio(asset_to_fetch)





