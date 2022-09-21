# -*- coding: utf-8 -*-
# import requests
# from bs4 import BeautifulSoup
import pandas as pd

def GetMarketData():
    url = 'https://s.cafef.vn/TraCuuLichSu2/TraCuu.chn#data'
    items = pd.read_html(url)
    LEN = len(items)
    df = items[LEN-1]    
    df.rename(columns = {0:'Symbol', 
                         1:'Close',
                         2:'%',                         
                         3:'TC',
                         4:'TC',
                         5:'Open',
                         6:'High',
                         7:'Low',
                         8:'Volume',
                         9:'GT-TT'}, inplace = True)    
    df = df[0:len(df)-1]
    #print(df)
    df['Volume'] = df['Volume'].astype(float)
    df['%'] = df['%'].apply(lambda x: x.split(' ')[1][1:])
    #print(df)
    #df.describe()
    #df.info()
    df['%'] = df['%'].astype(float)    
    #df.describe()
    #df.info()
    print(df)
    #df.isnull().sum()
    return df

def GetStocksByDragonFly():
    df = GetMarketData()
    df = df[(df['High']==df['Close'])]
    df = df[df['Volume'] > 50000]
    df = df[df['%'] >= 3]
    df = df.reset_index(drop=True)
    return df

#df = GetStocksByDragonFly()
#print(df)