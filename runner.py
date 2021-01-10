

import alpaca_trade_api as tradeapi
import config
import pandas as pd


def simple_list_positions():
    pos = api.list_positions()
    df = pd.DataFrame() # columns=['symbol', 'market_value', 'qty']
    for x in pos:
        df2 = pd.DataFrame([[x.symbol,x.market_value,x.qty]],columns=['symbol', 'market_value', 'qty'])
        df = df.append(df2)
        
    print(df)


api = tradeapi.REST(config.KEY_ID, config.SECRET_KEY, base_url='https://paper-api.alpaca.markets')
account = api.get_account()

print(account.status)

#print(api.list_positions())



hot_list = ['AAPL', 'TSLA', 'SQ']

simple_list_positions()


