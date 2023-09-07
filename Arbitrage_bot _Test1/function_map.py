


# List of tokens to fetch
tokens_to_fetch = [
    'MATIC',
    'QUICK',
    'SUSHI',
    'WMATIC',
    'AAVE',
    'WBTC',
    'USDC',
    'DAI',
    'CRV',
    'WETH',
    'SNX',
    'LINK',
    'UNI',
    'RENBTC',
    'BADGER',
    'RARI',
    'QUICK',
    'FRAX',
    'CEL',
    'REN',
    'CRV',
    'BZRX',
    'DAI',
    'USDT',
    'WBTC',
    'SUSHI',
    'PICKLE',
    'SPELL',
    'GHST',
    'CURVE'
]


# List of function files
function_files = [
'Binance_functions',
'Bitmart_functions',
'Bitstamp_functions',
'Bittrex_functions',
'Bybit_functions',
'Cexio_functions',
'coinbase_functions',
'Coinex_functions',
'crypto_com_functions',
'Hitbtc_functions',
'huobi_functions',
'kraken_functions',
'kucoin_functions',
#'mexc_functions',
'OKEx_functions',
'Probit_functions',
'Wazirx_functions'
                 ]
#list of exchange                
all_exchanges = ["Binance", "Bitmart", "Bitstamp", "Bittrex", "Bybit", "Cexio", "Coinbase", "Coinex", "Crypto", "Hitbtc", "Huobi", "Kraken", "Kucoin", "OKEx", "Probit", "Wazirx"]
                 
# List of relevant functions
relevant_functions_for_present_data  = {
    'Binance': {
        'Binance_functions': ['fetch_present_data_and_save_binance']
    },
    'Bitmart': {
        'Bitmart_functions': ['fetch_present_data_and_save_bitmart']
    }, 
    'Bitstamp': {
        'Bitstamp_functions': ['fetch_present_data_and_save_bitstamp']
    }, 
    'Bittrex': {
        'Bittrex_functions': ['fetch_present_data_and_save_bittrex']
    }, 
    'Bybit': {
        'Bybit_functions': ['fetch_and_save_bybit']
    },
    'Cexio': {
        'Cexio_functions': ['fetch_present_data_and_save_Cexio']
    },
    'Coinbase': {
        'coinbase_functions': ['fetch_present_data_and_save_coinbase']
    },
    'Coinex': {
        'Coinex_functions': ['fetch_present_data_and_save_coinex']
    },
    'Crypto': {
        'crypto_com_functions': ['fetch_present_data_and_save_crypto']
    },
    'Hitbtc': {
        'Hitbtc_functions': ['fetch_present_data_and_save_hitbtc']
    },
    'Huobi': {
        'huobi_functions': ['fetch_present_data_and_save_huobi']
    },
    'Kraken': {
        'kraken_functions': ['fetch_present_data_and_save_kraken']
    },
    'Kucoin': {
        'kucoin_functions': ['fetch_present_data_and_save_kucoin']
    },
    #'mexc_functions': ['fetch_present_data_and_save_kucoin'],(x2)
    'OKEx': {
        'OKEx_functions': ['fetch_present_data_and_save_okex']
    },
    'Probit': {
        'Probit_functions': ['fetch_present_data_and_save_probit']
    },
    'Wazirx': {
        'Wazirx_functions': ['fetch_present_data_and_save_wazirx']
    },
}




###-----------------------------------------------------------------------------------------
# List of relevant functions
relevant_functions_for_history_data  = {
    'Binance': {
        'Binance_functions': ['fetch_historical_data_and_save']
    },
    'Bitmart': {
        'Bitmart_functions': ['fetch_historical_data_and_save_bitmart']
    },
    'Bittrex': {
        'Bittrex_functions': ['fetch_historical_data_and_save_bittrex']
    },
    'Coinbase': {
        'coinbase_functions': ['fetch_historical_data_and_save_coinbase']
    },
     'Huobi': {
        'huobi_functions': ['fetch_historical_data_and_save_huobi']
    },
    'Kraken': {
        'kraken_functions': ['fetch_historical_data_and_save_kraken']
    },


    
}




relevant_functions_for_remove = {
    'Binance': {
        'Binance_functions': ['fetch_present_data_and_save_binance']
    },
    'Bitmart': {
        'Bitmart_functions': ['fetch_present_data_and_save_bitmart']
    }, 
    'Bitstamp': {
        'Bitstamp_functions': ['fetch_present_data_and_save_bitstamp']
    }, 
    'Bittrex': {
        'Bittrex_functions': ['fetch_present_data_and_save_bittrex']
    }, 
    'Bybit': {
        'Bybit_functions': ['fetch_and_save_bybit']
    },
    'Cexio': {
        'Cexio_functions': ['fetch_present_data_and_save_Cexio']
    },
    'Coinbase': {
        'coinbase_functions': ['fetch_present_data_and_save_coinbase']
    },
    'Coinex': {
        'Coinex_functions': ['fetch_present_data_and_save_coinex']
    },
    'Crypto': {
        'crypto_com_functions': ['fetch_present_data_and_save_crypto']
    },
    'Hitbtc': {
        'Hitbtc_functions': ['fetch_present_data_and_save_hitbtc']
    },
    'Huobi': {
        'huobi_functions': ['fetch_present_data_and_save_huobi']
    },
    'Kraken': {
        'kraken_functions': ['fetch_present_data_and_save_kraken']
    },
    'Kucoin': {
        'kucoin_functions': ['fetch_present_data_and_save_kucoin']
    },
    #'mexc_functions': ['fetch_present_data_and_save_kucoin'],(x2)
    'OKEx': {
        'OKEx_functions': ['fetch_present_data_and_save_okex']
    },
    'Probit': {
        'Probit_functions': ['fetch_present_data_and_save_probit']
    },
    'Wazirx': {
        'Wazirx_functions': ['fetch_present_data_and_save_wazirx']
    },
}













