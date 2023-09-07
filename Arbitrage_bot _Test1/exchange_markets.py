# exchange_markets.py

# exchange_markets.py

exchange_market_lists = {
    'Binance': {
        'MATIC': 'MATICUSDT',
        'QUICK': 'QUICKUSDT',
        'SUSHI': 'SUSHIUSDT',
        'WMATIC': 'WMATICUSDT',
        'AAVE': 'AAVEUSDT',
        'WBTC': 'BTCUSDT',
        'USDC': 'USDCUSDT',
        'DAI': 'DAIUSDT',
        'CRV': 'CRVUSDT',
        'WETH': 'ETHUSDT',
        'SNX': 'SNXUSDT',
        'LINK': 'LINKUSDT',
        'UNI': 'UNIUSDT',
        'RENBTC': 'RENBTCUSDT',
        'BADGER': 'BADGERUSDT',
        'RARI': 'RARIUSDT',
        'FRAX': 'FRAXUSDT',
        'CEL': 'CELUSDT',
        'REN': 'RENUSDT',
        'BZRX': 'BZRXUSDT',
        'USDT': 'USDTUSDT',
        'PICKLE': 'PICKLEUSDT',
        'SPELL': 'SPELLUSDT',
        'GHST': 'GHSTUSDT',
        'CURVE': 'CURVEUSDT',
        
        
        # Add or modify more assets and trading pairs for Binance
    },
    
#---------------------------------------------------------------------------------------------------------------
    'Kraken': {
        'MATIC': 'MATICUSD',
        'QUICK': 'QUICKUSD',
        'SUSHI': 'SUSHIUSD',
        'WMATIC': 'WMATICUSD',
        'AAVE': 'AAVEUSD',
        'WBTC': 'XBTUSD',
        'USDC': 'USDCUSD',
        'DAI': 'DAIUSD',
        'CRV': 'CRVUSD',
        'WETH': 'ETHUSD',
        'SNX': 'SNXUSD',
        'LINK': 'LINKUSD',
        'UNI': 'UNIUSD',
        'RENBTC': 'RENBTCUSD',
        'BADGER': 'BADGERUSD',
        'RARI': 'RARIUSD',
        'FRAX': 'FRAXUSD',
        'CEL': 'CELUSD',
        'REN': 'RENUSD',
        'BZRX': 'BZRXUSD',
        'USDT': 'USDTUSD',
        'PICKLE': 'PICKLEUSD',
        'SPELL': 'SPELLUSD',
        'GHST': 'GHSTUSD',
        'CURVE': 'CRVUSD',
        # Add or modify more assets and trading pairs for Kraken
    },
    'Crypto.com': {
        'MATIC': 'MATIC_USDT',
        'QUICK': 'QUICK_USDT',
        'SUSHI': 'SUSHI_USDT',
        'WMATIC': 'WMATIC_USDT',
        'AAVE': 'AAVE_USDT',
        'WBTC': 'WBTC_USDT',
        'USDC': 'USDC_USDT',
        'DAI': 'DAI_USDT',
        'CRV': 'CRV_USDT',
        'WETH': 'WETH_USDT',
        'SNX': 'SNX_USDT',
        'LINK': 'LINK_USDT',
        'UNI': 'UNI_USDT',
        'RENBTC': 'RENBTC_USDT',
        'BADGER': 'BADGER_USDT',
        'RARI': 'RARI_USDT',
        'FRAX': 'FRAX_USDT',
        'CEL': 'CEL_USDT',
        'REN': 'REN_USDT',
        'BZRX': 'BZRX_USDT',
        'USDT': 'USDT_USDT',
        'PICKLE': 'PICKLE_USDT',
        'SPELL': 'SPELL_USDT',
        'GHST': 'GHST_USDT',
        'CURVE': 'CURVE_USDT',
        # Add or modify more assets and trading pairs for Crypto.com
    },
     'MEXC': {
        'MATIC': 'MATICUSDT',
        'QUICK': 'QUICKUSDT',
        'SUSHI': 'SUSHIUSDT',
        'WMATIC': 'WMATICUSDT',
        'AAVE': 'AAVEUSDT',
        'WBTC': 'BTCUSDT',
        'ETH': 'ETHUSDT',
        'DAI': 'DAIUSDT',
        'CRV': 'CRVUSDT',
        'WETH': 'ETHUSDT',
        'SNX': 'SNXUSDT',
        'LINK': 'LINKUSDT',
        'UNI': 'UNIUSDT',
        'RENBTC': 'RENBTCUSDT',
        'BADGER': 'BADGERUSDT',
        'RARI': 'RARIUSDT',
        'FRAX': 'FRAXUSDT',
        'CEL': 'CELUSDT',
        'REN': 'RENUSDT',
        'BZRX': 'BZRXUSDT',
        'USDT': 'USDTUSDT',
        'PICKLE': 'PICKLEUSDT',
        'SPELL': 'SPELLUSDT',
        'GHST': 'GHSTUSDT',
        'CURVE': 'CRVUSDT',
        # Add or modify more assets and trading pairs for MEX
    },
    'coinbase': {
        'MATIC': 'MATIC-USD',
        'QUICK': 'QUICK-USD',
        'SUSHI': 'SUSHI-USD',
        'WMATIC': 'WMATIC-USD',
        'AAVE': 'AAVE-USD',
        'WBTC': 'BTC-USD',
        'USDC': 'USDC-USD',
        'DAI': 'DAI-USD',
        'CRV': 'CRV-USD',
        'WETH': 'ETH-USD',
        'SNX': 'SNX-USD',
        'LINK': 'LINK-USD',
        'UNI': 'UNI-USD',
        'RENBTC': 'RENBTC-USD',
        'BADGER': 'BADGER-USD',
        'RARI': 'RARI-USD',
        'FRAX': 'FRAX-USD',
        'CEL': 'CEL-USD',
        'REN': 'REN-USD',
        'BZRX': 'BZRX-USD',
        'USDT': 'USDT-USD',
        'PICKLE': 'PICKLE-USD',
        'SPELL': 'SPELL-USD',
        'GHST': 'GHST-USD',
        'CURVE': 'CRV-USD',
        # Add or modify more assets and trading pairs for Coinbase
    },
    
    'Bittrex': {
        'MATIC': 'MATIC-USDT',
        'QUICK': 'QUICK-USDT',
        'SUSHI': 'SUSHI-USDT',
        'WMATIC': 'WMATIC-USDT',
        'AAVE': 'AAVE-USDT',
        'ETH': 'ETH-USDT',
        'DAI': 'DAI-USDT',
        'CRV': 'CRV-USDT',
        'SNX': 'SNX-USDT',
        'LINK': 'LINK-USDT',
        'UNI': 'UNI-USDT',
        'RENBTC': 'RENBTC-USDT',
        'BADGER': 'BADGER-USDT',
        'RARI': 'RARI-USDT',
        'FRAX': 'FRAX-USDT',
        'CEL': 'CEL-USDT',
        'REN': 'REN-USDT',
        'BZRX': 'BZRX-USDT',
        'USDT': 'USDT-USDT',
        'PICKLE': 'PICKLE-USDT',
        'SPELL': 'SPELL-USDT',
        'GHST': 'GHST-USDT',
        'CURVE': 'CRV-USDT',
        # Add or modify more assets and trading pairs for Bittrex
    },
    
    'Huobi': {
        'MATIC': 'maticusdt',
        'QUICK': 'quickusdt',
        'SUSHI': 'sushiusdt',
        'WMATIC': 'wmaticusdt',
        'AAVE': 'aaveusdt',
        'WBTC': 'btcusdt',
        'ETH': 'ethusdt',
        'DAI': 'daiusdt',
        'CRV': 'crvusdt',
        'WETH': 'ethusdt',
        'SNX': 'snxusdt',
        'LINK': 'linkusdt',
        'UNI': 'uniusdt',
        'RENBTC': 'renbtcusdt',
        'BADGER': 'badgerusdt',
        'RARI': 'rariusdt',
        'FRAX': 'fraxusdt',
        'CEL': 'celusdt',
        'REN': 'renusdt',
        'BZRX': 'bzrxusdt',
        'USDT': 'usdtusdt',
        'PICKLE': 'pickleusdt',
        'SPELL': 'spellusdt',
        'GHST': 'ghstusdt',
        'CURVE': 'crvusdt',
        # Add or modify more assets and trading pairs for Huobi
    },
    'OKEx': {
        'MATIC': 'MATIC-USDT',
        'MATIc': 'MATIC-USDC',
        'QUICK': 'QUICK-USDT',
        'SUSHI': 'SUSHI-USDT',
        'WMATIC': 'WMATIC-USDT',
        'AAVE': 'AAVE-USDT',
        'WBTC': 'WBTC-USDT',
        'ETH': 'ETH-USDT',
        'DAI': 'DAI-USDT',
        'CRV': 'CRV-USDT',
        'WETH': 'WETH-USDT',
        'SNX': 'SNX-USDT',
        'LINK': 'LINK-USDT',
        'UNI': 'UNI-USDT',
        'RENBTC': 'RENBTC-USDT',
        'BADGER': 'BADGER-USDT',
        'RARI': 'RARI-USDT',
        'FRAX': 'FRAX-USDT',
        'CEL': 'CEL-USDT',
        'REN': 'REN-USDT',
        'BZRX': 'BZRX-USDT',
        'USDT': 'USDT-USDT',
        'PICKLE': 'PICKLE-USDT',
        'SPELL': 'SPELL-USDT',
        'GHST': 'GHST-USDT',
        'CURVE': 'CURVE-USDT',
        # Add or modify more assets and trading pairs for OKEx
    },
    'Bitstamp': {
        'MATIC': 'MATICUSD',
        'QUICK': 'QUICKUSD',
        'SUSHI': 'SUSHIUSD',
        'WMATIC': 'WMATICUSD',
        'AAVE': 'AAVEUSD',
        'WBTC': 'XBTUSD',
        'ETH': 'ETHUSD',
        'DAI': 'DAIUSD',
        'CRV': 'CRVUSD',
        'WETH': 'ETHUSD',
        'SNX': 'SNXUSD',
        'LINK': 'LINKUSD',
        'UNI': 'UNIUSD',
        'RENBTC': 'RENBTCUSD',
        'BADGER': 'BADGERUSD',
        'RARI': 'RARIUSD',
        'FRAX': 'FRAXUSD',
        'CEL': 'CELUSD',
        'REN': 'RENUSD',
        'BZRX': 'BZRXUSD',
        'USDT': 'USDTUSD',
        'PICKLE': 'PICKLEUSD',
        'SPELL': 'SPELLUSD',
        'GHST': 'GHSTUSD',
        'CURVE': 'CRVUSD',
        # Add or modify more assets and trading pairs for Bitstamp
    },
    'KuCoin': {
        'MATIC': 'MATIC-USDT',
        'QUICK': 'QUICK-USDT',
        'SUSHI': 'SUSHI-USDT',
        'WMATIC': 'WMATIC-USDT',
        'AAVE': 'AAVE-USDT',
        'WBTC': 'WBTC-USDT',
        'USDC': 'USDC-USDT',
        'DAI': 'DAI-USDT',
        'CRV': 'CRV-USDT',
        'WETH': 'WETH-USDT',
        'SNX': 'SNX-USDT',
        'LINK': 'LINK-USDT',
        'UNI': 'UNI-USDT',
        'RENBTC': 'RENBTC-USDT',
        'BADGER': 'BADGER-USDT',
        'RARI': 'RARI-USDT',
        'FRAX': 'FRAX-USDT',
        'CEL': 'CEL-USDT',
        'REN': 'REN-USDT',
        'BZRX': 'BZRX-USDT',
        'USDT': 'USDT-USDT',
        'PICKLE': 'PICKLE-USDT',
        'SPELL': 'SPELL-USDT',
        'GHST': 'GHST-USDT',
        'CURVE': 'CURVE-USDT',
        # Add or modify more assets and trading pairs for KuCoin
    },
    'HitBTC': {
        'MATIC': 'MATICUSDT',
        'QUICK': 'QUICKUSDT',
        'SUSHI': 'SUSHIUSDT',
        'WMATIC': 'WMATICUSDT',
        'AAVE': 'AAVEUSDT',
        'WBTC': 'WBTCUSDT',
        'USDC': 'USDCUSDT',
        'DAI': 'DAIUSDT',
        'CRV': 'CRVUSDT',
        'WETH': 'WETHUSDT',
        'SNX': 'SNXUSDT',
        'LINK': 'LINKUSDT',
        'UNI': 'UNIUSDT',
        'RENBTC': 'RENBTCUSDT',
        'BADGER': 'BADGERUSDT',
        'RARI': 'RARIUSDT',
        'FRAX': 'FRAXUSDT',
        'CEL': 'CELUSDT',
        'REN': 'RENUSDT',
        'BZRX': 'BZRXUSDT',
        'USDT': 'USDTUSDT',
        'PICKLE': 'PICKLEUSDT',
        'SPELL': 'SPELLUSDT',
        'GHST': 'GHSTUSDT',
        'CURVE': 'CURVEUSDT',
        # Add or modify more assets and trading pairs for HitBTC
    },
    'BitMart': {
        'MATIC': 'MATIC_USDT',
        'QUICK': 'QUICK_USDT',
        'SUSHI': 'SUSHI_USDT',
        'WMATIC': 'WMATIC_USDT',
        'AAVE': 'AAVE_USDT',
        'WBTC': 'WBTC_USDT',
        'USDC': 'USDC_USDT',
        'DAI': 'DAI_USDT',
        'CRV': 'CRV_USDT',
        'WETH': 'WETH_USDT',
        'SNX': 'SNX_USDT',
        'LINK': 'LINK_USDT',
        'UNI': 'UNI_USDT',
        'RENBTC': 'RENBTC_USDT',
        'BADGER': 'BADGER_USDT',
        'RARI': 'RARI_USDT',
        'FRAX': 'FRAX_USDT',
        'CEL': 'CEL_USDT',
        'REN': 'REN_USDT',
        'BZRX': 'BZRX_USDT',
        'USDT': 'USDT_USDT',
        'PICKLE': 'PICKLE_USDT',
        'SPELL': 'SPELL_USDT',
        'GHST': 'GHST_USDT',
        'CURVE': 'CURVE_USDT',
        # Add or modify more assets and trading pairs for Bitmart
    }, 
    'Probit': {
        'MATIC': 'MATIC-USDT',
        'QUICK': 'QUICK-USDT',
        'SUSHI': 'SUSHI-USDT',
        'WMATIC': 'WMATIC-USDT',
        'AAVE': 'AAVE-USDT',
        'WBTC': 'WBTC-USDT',
        'USDC': 'USDC-USDT',
        'DAI': 'DAI-USDT',
        'CRV': 'CRV-USDT',
        'WETH': 'WETH-USDT',
        'SNX': 'SNX-USDT',
        'LINK': 'LINK-USDT',
        'UNI': 'UNI-USDT',
        'RENBTC': 'RENBTC-USDT',
        'BADGER': 'BADGER-USDT',
        'RARI': 'RARI-USDT',
        'FRAX': 'FRAX-USDT',
        'CEL': 'CEL-USDT',
        'REN': 'REN-USDT',
        'BZRX': 'BZRX-USDT',
        'USDT': 'USDT-USDT',
        'PICKLE': 'PICKLE-USDT',
        'SPELL': 'SPELL-USDT',
        'GHST': 'GHST-USDT',
        'CURVE': 'CURVE-USDT',
        # Add or modify more assets and trading pairs for Probit
    },
    'Coinex': {
        'MATIC': 'maticusdt',
        'QUICK': 'quickusdt',
        'SUSHI': 'sushiusdt',
        'WMATIC': 'wmaticusdt',
        'AAVE': 'aaveusdt',
        'WBTC': 'wbtcusdt',
        'USDC': 'usdcusdt',
        'DAI': 'daiusdt',
        'CRV': 'crvusdt',
        'WETH': 'wethusdt',
        'SNX': 'snxusdt',
        'LINK': 'linkusdt',
        'UNI': 'uniusdt',
        'RENBTC': 'renbtcusdt',
        'BADGER': 'badgerusdt',
        'RARI': 'rariusdt',
        'FRAX': 'fraxusdt',
        'CEL': 'celusdt',
        'REN': 'renusdt',
        'BZRX': 'bzrxusdt',
        'USDT': 'usdtusdt',
        'PICKLE': 'pickleusdt',
        'SPELL': 'spellusdt',
        'GHST': 'ghstusdt',
        'CURVE': 'crvusdt',
        # Add or modify more assets and trading pairs for Coinex
    },
    'Bybit': {
        'MATIC': 'MATICUSDT',
        'QUICK': 'QUICKUSDT',
        'SUSHI': 'SUSHIUSDT',
        'WMATIC': 'WMATICUSDT',
        'AAVE': 'AAVEUSDT',
        'WBTC': 'BTCUSDT',
        'ETH': 'ETHUSDT',
        'DAI': 'DAIUSDT',
        'CRV': 'CRVUSDT',
        'WETH': 'ETHUSDT',
        'SNX': 'SNXUSDT',
        'LINK': 'LINKUSDT',
        'UNI': 'UNIUSDT',
        'RENBTC': 'RENBTCUSDT',
        'BADGER': 'BADGERUSDT',
        'RARI': 'RARIUSDT',
        'FRAX': 'FRAXUSDT',
        'CEL': 'CELUSDT',
        'REN': 'RENUSDT',
        'BZRX': 'BZRXUSDT',
        'USDT': 'USDTUSDT',
        'PICKLE': 'PICKLEUSDT',
        'SPELL': 'SPELLUSDT',
        'GHST': 'GHSTUSDT',
        'CURVE': 'CURVEUSDT',
        # Add or modify more assets and trading pairs for Bybit
    },
    'WazirX': {
           'MATIC': 'maticusdt',
        'QUICK': 'quicusdt',
        'SUSHI': 'sushiusdt',
        'WMATIC': 'wmaticusdt',
        'AAVE': 'aaveusdt',
        'WBTC': 'wbtcusdt',
        'USDC': 'usdcusdt',
        'DAI': 'daiusdt',
        'CRV': 'crvusdt',
        'WETH': 'wethusdt',
        'SNX': 'snxusdt',
        'LINK': 'linkusdt',
        'UNI': 'uniusdt',
        'RENBTC': 'renbtcusdt',
        'BADGER': 'badgerusdt',
        'RARI': 'rariusdt',
        'FRAX': 'fraxusdt',
        'CEL': 'celusdt',
        'REN': 'renusdt',
        'BZRX': 'bzrxusdt',
        'USDT': 'usdtusdt',
        'PICKLE': 'pickleusdt',
        'SPELL': 'spellusdt',
        'GHST': 'ghstusdt',
        'CURVE': 'curveusdt',
        # Add or modify more assets and trading pairs for WazirX
    },
      'CEX.IO': {
        'MATIC': {'symbol1': 'MATIC', 'symbol2': 'USDT'},
        'USDT': {'symbol1': 'USDT', 'symbol2': 'USDT'},
        'QUICK': {'symbol1': 'QUICK', 'symbol2': 'USDT'},
        'SUSHI': {'symbol1': 'SUSHI', 'symbol2': 'USDT'},
        'WMATIC': {'symbol1': 'WMATIC', 'symbol2': 'USDT'},
        'AAVE': {'symbol1': 'AAVE', 'symbol2': 'USDT'},
        'WBTC': {'symbol1': 'WBTC', 'symbol2': 'USDT'},
        'ETH': {'symbol1': 'ETH', 'symbol2': 'USDT'},
        'DAI': {'symbol1': 'DAI', 'symbol2': 'USDT'},
        'CRV': {'symbol1': 'CRV', 'symbol2': 'USDT'},
        'WETH': {'symbol1': 'WETH', 'symbol2': 'USDT'},
        'SNX': {'symbol1': 'SNX', 'symbol2': 'USDT'},
        'LINK': {'symbol1': 'LINK', 'symbol2': 'USDT'},
        'UNI': {'symbol1': 'UNI', 'symbol2': 'USDT'},
        'RENBTC': {'symbol1': 'RENBTC', 'symbol2': 'USDT'},
        'BADGER': {'symbol1': 'BADGER', 'symbol2': 'USDT'},
        'RARI': {'symbol1': 'RARI', 'symbol2': 'USDT'},
        'FRAX': {'symbol1': 'FRAX', 'symbol2': 'USDT'},
        'CEL': {'symbol1': 'CEL', 'symbol2': 'USDT'},
        'REN': {'symbol1': 'REN', 'symbol2': 'USDT'},
        'BZRX': {'symbol1': 'BZRX', 'symbol2': 'USDT'},
        'USDT': {'symbol1': 'USDT', 'symbol2': 'USDT'},
        'PICKLE': {'symbol1': 'PICKLE', 'symbol2': 'USDT'},
        'SPELL': {'symbol1': 'SPELL', 'symbol2': 'USDT'},
        'GHST': {'symbol1': 'GHST', 'symbol2': 'USDT'},
        'CURVE': {'symbol1': 'CURVE', 'symbol2': 'USDT'},
        # Add or modify more assets and trading pairs for CEX.IO
    },
    'DigiFinex': {
        'MATIC': 'matic_usdt',
        'QUICK': 'quick_usdt',
        'SUSHI': 'sushi_usdt',
        'WMATIC': 'wmatic_usdt',
        'AAVE': 'aave_usdt',
        'WBTC': 'wbtc_usdt',
        'ETH': 'eth_usdt',
        'DAI': 'dai_usdt',
        'CRV': 'crv_usdt',
        'WETH': 'weth_usdt',
        'SNX': 'snx_usdt',
        'LINK': 'link_usdt',
        'UNI': 'uni_usdt',
        'RENBTC': 'renbtc_usdt',
        'BADGER': 'badger_usdt',
        'RARI': 'rari_usdt',
        'FRAX': 'frax_usdt',
        'CEL': 'cel_usdt',
        'REN': 'ren_usdt',
        'BZRX': 'bzrx_usdt',
        'USDT': 'usdt_usdt',
        'PICKLE': 'pickle_usdt',
        'SPELL': 'spell_usdt',
        'GHST': 'ghst_usdt',
        'CURVE': 'curve_usdt',
        # Add or modify more assets and trading pairs for DigiFinex
    },
    
}#REMEBER EXCHANGE LIKE OKEKX HAVE MATIC AND MATIc FOR USDT AND USDC MARK RESPECTIVELY