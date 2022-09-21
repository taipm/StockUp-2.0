# from array import array
# from operator import indexOf
# import os
# from re import A
# import sys
# from collections import deque
from operator import index, indexOf

from sqlalchemy import true
import db
import numpy as np
import pandas as pd

def get_data_stock(stock):
    return db.GetStockData(stock=stock)

def get_price_data_stock(stock):
    df = db.GetStockData(stock=stock)    
    rs_df = df[['Open','Close','High','Low']]
    print(rs_df)
    return rs_df

      
def get_close_price_data(stock):
    prices = db.GetStockData(stock=stock)['Close']
    return prices


data = get_close_price_data("VND")


def print_info_data(data):
    n = len(data)
    min = np.min(data)
    max = np.max(data)
    max_index = indexOf(data,max)
    min_index = indexOf(data,min)
    print('Chuỗi: ' + str(data))
    print('\nĐộ dài: ' + str(n))
    print('Max: ' + str(max) + " . Vị trí: " + str(max_index))
    print('Min: ' + str(min) + " . Vị trí: " + str(min_index))

#print_info_data(data=data)
def find_up_arr(data):
    '''
    Trả về chuỗi giảm liên tiếp có độ dài lớn nhất
    '''
    n = len(data)
    a = data
    lst_up = list() #Chuỗi lưu các dãy con
    #lst_down = list()
    
    for i in range(0,n-1): #Chạy từ đầu
        rs_up = [] #dãy con hiện tại đang xây dựng
        #rs_down = []
        for j in range(i, n-1): #j chạy tiếp từ i
            #print('a[i]' + str(a[i]))
            #print('a[j]' + str(a[j]))
            if (a[j] >= a[i]): #a[j] chính xác là phần tử tăng tiếp theo                
                #print('Tăng')
                rs_up.append(a[j])
                i = j
            else:
                break
        #print(rs_up)
        #print(rs_down)
        lst_up.append(rs_up)
        #lst_down.append(rs_down)
                
    print('Up: '+ str(lst_up))    
    return lst_up
    #print('Down: '+ str(lst_down))

def find_down_arr(data):
    '''
    Trả về chuỗi giảm liên tiếp có độ dài lớn nhất
    '''
    n = len(data)
    a = data    
    lst_down = list()
    
    for i in range(0,n-1): #Chạy từ đầu        
        rs_down = []
        for j in range(i, n-1): #j chạy tiếp từ i
            #print('a[i]' + str(a[i]))
            #print('a[j]' + str(a[j]))
            if (a[j] <= a[i]): #a[j] chính xác là phần tử tăng tiếp theo                
                #print('Giảm')
                rs_down.append(a[j])
                i = j
            else:
                break
        #print(rs_down)        
        lst_down.append(rs_down)                    
    print('Down: '+ str(lst_down))
    return lst_down

def analysis_prices(lst):
    for i in range(0, len(lst)-1):
        print(str(lst[i]) + " : " + str(len(lst[i])))
        
# lst_up = find_up_arr(data=data)
# lst_down = find_down_arr(data=data)

#analysis_prices(lst_up)
#analysis_prices(lst_down)

def percent(x,y):
    try:       
        return np.float64((((x-y)/y)*100))
    except:
        print('Lỗi phép chia cho 0')
        return np.float64

GIAM_MANH = -5 #%
#CONST TANG_MANH
TANG_MANH = 5 #%

def is_giam_manh(i,a): #Nếu a[i] giảm mạnh
    p = percent(a[i],a[i-1])
    if(p <=GIAM_MANH):        
        return True
    return False

def is_tang_manh(i,a): #Nếu a[i] giảm mạnh
    p = percent(a[i],a[i-1])
    if(p >= TANG_MANH):
        return True
    return False

def start_big_down(data):
    a = data
    n = len(data)
    for i in range(1,n):
        if(is_giam_manh(i,a)):            
            print('Giảm mạnh tại giá: ' + str(a[i]) + " : Biên độ: " +str(percent(a[i],a[i-1])) + " : " + str(a[i-1]) + " -> " + str(a[i]))
            for j in range(i+1,n):
                print(str(a[i]) + " -> " + str(a[j]) + " : " + str(percent(a[j],a[i])) + ' (%)') #Cần tính % của j,i vì giá được xếp ngược
                #print(percent(a[i],a[j]))

def suc_manh_nen(open,close,high,low):
    suc_manh = 0
    if(high == close):
        suc_manh = 1
    return suc_manh


'''
KIỂM TRA SỨC MẠNH TOÀN BỘ NẾN
'''
def scan_candle_stick(stock):
    stock = 'VND'
    #1. Chuẩn bị dữ liệu
    df = get_price_data_stock(stock=stock)
    
    print('Sức mạnh nến: ')
    #last_row = df.tail(1)
    
    #df = df.assign(CandleStick = lambda x : (suc_manh_nen(x['Open'],x['Close'],x['High'],x['Low'])))
    #df['SucManh']
    start = 0
    stop = len(df)-1
    for i in range(start,stop):
        _open = df.iloc[i]['Open']
        _close = df.iloc[i]['Close']
        _high = df.iloc[i]['High']
        _low = df.iloc[i]['Low']

        print("Điểm sức mạnh: " + str(suc_manh_nen(_open,_close,_high,_low)))
        
    #print(df.sort_values(by=['CandleStick'],ascending=True))
    #print(df['CandleStick'].sort_values(ascending=True))
    #print(np.min(df['CandleStick']))

scan_candle_stick('VND')
        
#start_big_down(data=data)
#print(data[len(data)-1])
