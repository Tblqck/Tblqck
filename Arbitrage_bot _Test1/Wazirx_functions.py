





import requests
import json
from datetime import datetime
from exchange_markets import exchange_market_lists

def fetch_present_data_and_save_wazirx(asset):
    exchange = 'WazirX'  # Hard-coded to WazirX
    if exchange not in exchange_market_lists:
        print(f"Exchange '{exchange}' is not supported.")
        return

    symbol = fetch_symbol(exchange, asset)
    if not symbol:
        print(f"Asset '{asset}' symbol not found for '{exchange}'.")
        return

    base_url = "https://api.wazirx.com/api/v2/tickers"
    response = requests.get(base_url)
    data = response.json()

    matic_usdt_ticker = None

    for ticker_symbol, ticker_data in data.items():
        if ticker_symbol == symbol:
            matic_usdt_ticker = ticker_data
            break

    if matic_usdt_ticker:
        price = float(matic_usdt_ticker['last'])
        volume = float(matic_usdt_ticker['volume'])
        liquidity_score = calculate_liquidity_score(price, volume)

        present_data = {
            'exchange': exchange,
            'asset': asset,
            'trading_pair': symbol,
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
        print(f'Error occurred. Symbol not found for {asset} on {exchange}.')

def fetch_symbol(exchange, asset):
    if exchange not in exchange_market_lists:
        print(f"Exchange '{exchange}' is not supported.")
        return

    if asset not in exchange_market_lists[exchange]:
        print(f"Asset '{asset}' not found for '{exchange}'.")
        return

    return exchange_market_lists[exchange][asset]

def calculate_liquidity_score(price, volume):
    # Modify this logic based on your specific requirements
    liquidity_score = (price * volume) / 1000
    return round(liquidity_score, 2)

if __name__ == '__main__':
    asset_to_fetch = input("Enter the asset you want to fetch data for: ").strip().upper()
    fetch_present_data_and_save_wazirx(asset_to_fetch)



