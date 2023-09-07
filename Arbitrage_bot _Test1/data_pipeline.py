



import json
import importlib
from function_map import function_files, relevant_functions_for_present_data, relevant_functions_for_history_data, tokens_to_fetch
import time

# Define a function to execute present data functions with a time constraint
def execute_present_data_functions_with_timeout(asset, timeout_minutes=30):
    start_time = time.time()
    
    for exchange, exchange_data in relevant_functions_for_present_data.items():
        for module_name, function_names in exchange_data.items():
            try:
                # Load the module dynamically
                module = importlib.import_module(module_name)
                
                for function_name in function_names:
                    # Check if the function exists in the module
                    if hasattr(module, function_name):
                        # Get the function
                        fetch_function = getattr(module, function_name)
                        
                        # Call the function with the asset as an argument
                        try:
                            fetch_function(asset)
                            print(f"Fetched data for {asset} using {function_name} in {module_name} for exchange {exchange}")
                        except Exception as e:
                            print(f"Error while fetching data for {asset} using {function_name} in {module_name}: {str(e)}")
                    else:
                        print(f"Function '{function_name}' not found in '{module_name}' module for exchange {exchange}")
            except ModuleNotFoundError:
                print(f"Module '{module_name}' not found for exchange {exchange}.")
            
            elapsed_time = time.time() - start_time
            if elapsed_time >= timeout_minutes * 60:
                print(f"Execution timed out after {timeout_minutes} minutes.")
                return
    
    print("PROCESSING")  # Print "PROCESSING" when finished fetching data

if __name__ == '__main__':
    # Iterate through tokens_to_fetch
    for asset_to_fetch in tokens_to_fetch:
        # Execute present data functions with a 20-minute time constraint
        execute_present_data_functions_with_timeout(asset_to_fetch, timeout_minutes=20)

# -----------------------------------------------

def find_arbitrage_opportunities(filename, withdrawal_fee=4, exchange_fee=0.69, trading_amount=1000, max_liquidity_score=500):
    def load_market_data(filename):
        with open(filename, 'r') as file:
            return json.load(file)

    data = load_market_data(filename)  # Load market data from the JSON file

    opportunities = []

    # Group data by asset and exchange
    asset_exchange_data = {}
    for entry in data:
        asset = entry['asset']
        exchange = entry['exchange']
        price = entry.get('price') or entry.get('lastPrice')  # Use 'price' if available, otherwise use 'lastPrice'
        volume = entry.get('volume') or entry.get('volume_24h')  # Use 'volume' if available, otherwise use 'volume_24h'
        liquidity_score = entry.get('liquidity_score', 0)  # Default to 0 if 'liquidity_score' is missing

        if price is None or liquidity_score >= max_liquidity_score:  # Skip entries with missing or None price or high liquidity score
            continue

        if asset not in asset_exchange_data:
            asset_exchange_data[asset] = {}

        if exchange not in asset_exchange_data[asset]:
            asset_exchange_data[asset][exchange] = []

        asset_exchange_data[asset][exchange].append({'price': price, 'volume': volume})

    # Find arbitrage opportunities
    for asset, exchanges in asset_exchange_data.items():
        for exchange, data_list in exchanges.items():
            if len(data_list) >= 2:
                data_list.sort(key=lambda x: float(x['price']))

                min_price = float(data_list[0]['price'])
                max_price = float(data_list[-1]['price'])

                # Arbitrage within the same exchange
                if max_price - min_price > withdrawal_fee + exchange_fee:
                    profit = (max_price - min_price - withdrawal_fee - exchange_fee) * trading_amount / min_price
                    opportunities.append({
                        'asset': asset,
                        'exchange': exchange,
                        'action': 'Within Exchange Arbitrage',
                        'profit': profit
                    })

                # Arbitrage between different exchanges
                other_exchanges = [ex for ex in exchanges.keys() if ex != exchange]
                for other_exchange in other_exchanges:
                    other_data = exchanges[other_exchange]
                    other_data.sort(key=lambda x: float(x['price']))
                    other_min_price = float(other_data[0]['price'])

                    if max_price - other_min_price > withdrawal_fee + 2 * exchange_fee:
                        profit = (max_price - other_min_price - withdrawal_fee - 2 * exchange_fee) * trading_amount / other_min_price
                        opportunities.append({
                            'asset': asset,
                            'exchange': exchange,
                            'action': 'Between Exchanges Arbitrage',
                            'profit': profit,
                            'opposite_exchange': other_exchange
                        })

    return opportunities

def format_arbitrage_opportunity(opportunity):
    asset = opportunity['asset']
    exchange = opportunity['exchange']
    action = opportunity['action']
    profit = opportunity['profit']

    if action == 'Within Exchange Arbitrage':
        return f"ASSET IN VIEW: {asset}, BUY: {asset}, from {exchange}, SEND TO: {asset}, TO: {exchange},CHANGE TO: 'USDT', Action: {action}, Profit: ${profit:.2f}"
    elif action == 'Between Exchanges Arbitrage':
        opposite_exchange = opportunity['opposite_exchange']
        return f"ASSET IN VIEW: {asset}, BUY:{asset}, from {exchange}, SEND TO: {asset}, TO: {opposite_exchange},CHANGE TO: 'USDT', Action: {action}, Profit: ${profit:.2f}"

if __name__ == '__main__':
    arbitrage_opportunities = find_arbitrage_opportunities('market_data.json', max_liquidity_score=500)

    if arbitrage_opportunities:
        arbitrage_opportunities.sort(key=lambda x: x['profit'], reverse=True)
        for opportunity in arbitrage_opportunities:
            formatted_opportunity = format_arbitrage_opportunity(opportunity)
            print(formatted_opportunity)
    else:
        print("No arbitrage opportunities found.")

        
#-----
def clear_json_file(filename):
    with open(filename, 'w') as file:
        file.write('')

# Clear market_data.json
clear_json_file('market_data.json')
print('Data in market_data.json cleared.')
        
        
        
