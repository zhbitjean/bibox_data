#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 11:25:34 2018

@author: huaqingxie
"""
import pandas as pd
import ccxt
import numpy as np

"""
BiboxAPI: https://github.com/Biboxcom/API_Docs/wiki
ccxt: https://github.com/ccxt/ccxt/
"""

api = {"apiKey": 'eeccea338ecb24b796497f82765ba8ab71561d52',
       "secret": '5f7e2c9bd79ca6b3a7676ff7cdc6765e6d1c68ac'}

ccxt_client = ccxt.bibox(api)
symbol = 'BIX/GUSD'
interval = '1d'

symbol_l = ccxt_client.fetch_ohlcv(symbol, interval)


def parsing_list(list_):
    """
    Convert the list to dictionary 
    把交易所返回的列表转换成字典
    : param list_: the list return from exchange
    : param _historical_data: the historical ohlcv data
    : return dictionary contains ohlcv data
    """
    time_series = {}
    for line in list_:
        info = dict()
        info['Open'] = line[1]
        info['High'] = line[2]
        info['Low'] = line[3]
        info['Close'] = line[4]
        info['Volume'] = line[5]
        time_series[line[0]] = info
    return time_series

bibox_index = [
    'date',
    'Open',
    'High',
    'Low',
    'Close',
    'Volume'
]

symbol_df = pd.DataFrame(symbol_l, columns=bibox_index)
# print(symbol_df)
# symbol_df[['Open', 'High', 'Low', 'Close', 'Volume']] \
#     = symbol_df[['Open', 'High', 'Low', 'Close', 'Volume']].astype(np.float64)

symbol_df['date'] = symbol_df['date'].astype('datetime64[ms]')
symbol_df['mean_volume'] = symbol_df['Volume']
symbol_df = symbol_df.set_index(['date'])
symbol_df.to_csv('symbol_org.csv')
# print(symbol_df.index)
# df1 = df.groupby(level=0)['Value']
# .apply(lambda x: x.shift().rolling(min_periods=1,window=2).mean())
# .reset_index(name='Value_Average_Past_2_days')
# df = symbol_df['mean_volume'].apply(lambda x: x.shift().rolling(min_periods=1, window=7).mean())
df = symbol_df.copy()
df = df.rolling(min_periods=1, window=7).mean()
df.to_csv('symbol_mean.csv')
df = df.reset_index()
print(df)
print(df.to_json())
# convert timestamp to datetime
# data.index = pd.to_datetime(data.index, unit='ms')
