from cProfile import label
import pandas as pd
import numpy as np
import db
import StockHelper as helper
import matplotlib.pyplot as plt

stocks = ["VND","DBC","HAG","FRT"]

def get_mark_p(stock, df_data, i): #Lấy điểm sức mạnh của phiên thứ i (tính về trước, nghĩa là phiên gần nhất có chỉ số = 0)    
    data = df_data
    n = len(data)
    if i > n-1:
        print(str(i) + " > số phiên có trong dữ liệu " + str(n))
        return -1 # Số âm (-1) là để bạn biết i không hợp lệ so với bộ dữ liệu
    #index = n - i-1
    index = i
    #print('Đang tính phiên thứ : ' + str(index))
    data_row = data.iloc[index]
    #print(data_row)
    o = data_row['Open']
    c = data_row['Close']
    h = data_row['High']
    l = data_row['Low']
    
    mark = helper.mark_bar_by_p(open=o,close=c,high=h,low = l)
    print(stock + " - Mark : " +str(mark) + " <= c: " + str(c) + " - h: " + str(h) + " - " + str(data_row['Date']))
    return mark

def test_stocks_mark():
    
    for stock in stocks:    
        data = db.GetStockData(stock=stock)
        for i in range(0,2):
            get_mark_p(stock=stock, df_data=data, i=i)

def get_mark_p_all_time(stock):
    data = db.GetStockData(stock=stock)
    start = 0
    stop = len(data)
    lst = list()
    for i in range(start,stop):
        rs = get_mark_p(stock=stock, df_data=data, i=i)
        #lst.append([i,rs])
        lst.append(rs)
    #df = DataFrame(lst,columns=['Index','Mark'])
    df = pd.DataFrame(lst,columns=['Mark'])
    return df


def draw_mark_stocks():
    plt.title('Vẽ đồ thị trong Python với Matplotlib')
    for stock in stocks[0:1]:
        df = get_mark_p_all_time(stock=stock)
        df = df[df['Mark']<10].head(100)
        #plt.plot(df, 'go-', label=stock)
        plt.plot(df,label=stock)
        # plt.xlabel('X')
        # plt.ylabel('Y')
    plt.legend(loc='best')    
    
    plt.show()

def draw_mark_stock(stock):
    plt.title('Tổng quan cổ phiếu: ' + stock)
    df = db.GetStockData(stock=stock)
    df_mark = get_mark_p_all_time(stock=stock)
    df_mark = df_mark[df_mark['Mark']<10]
    df_mark = df_mark.head(100)
    #plt.plot(df, 'go-', label=stock)
    #plt.plot(df_mark,label="Mark")
    #plt.bar(data=df=['%'],label='bien_do',width=1,height=10)
    df = df.head(100)
    plt.bar(df['Date'],df['%'])
    plt.legend(loc='best')    
    
    plt.show()

#draw_mark_stock("VND")

def draw_bien_do_d(stock, distance):   
    data = db.GetStockData(stock=stock)
    prices = data['Close']
    bien_do_s = data['%']
    #Tính toán theo tổng biên độ của độ dài (d) phiên
    d = distance
    lst_bien_do = helper.slice_lst(distance=d,lst= bien_do_s)
    #print(lst_bien_do)
    lst = list() 
    for i in range(0,len(lst_bien_do)-1):
        sum_bien_do = np.sum(lst_bien_do[i])
        lst.append([i,sum_bien_do])
    lst = np.array(lst)
    print(lst_bien_do)
    df_bien_do_d = pd.DataFrame(lst,columns=['Index','Biên độ'])
    plt.title(stock + " : " + stock)
    plt.bar(df_bien_do_d['Index'], df_bien_do_d['Biên độ'])
    plt.legend(loc='best')        
    plt.show()

def draw_bien_do_d_s(stock, distances,n_data):
    data = db.GetStockData(stock=stock)
    prices = data['Close']
    bien_do_s = data['%']
    #Tính toán theo tổng biên độ của độ dài (d) phiên
    for d in distances:        
        lst_bien_do = helper.slice_lst(distance=d,lst= bien_do_s)        
        lst = list() 
        for i in range(0,len(lst_bien_do)-1):
            sum_bien_do = np.sum(lst_bien_do[i])
            lst.append([i,sum_bien_do])
        lst = np.array(lst)    
        df_bien_do_d = pd.DataFrame(lst,columns=['Index','Biên độ'])
        df_bien_do_d= df_bien_do_d.tail(n=100)
        plt.bar(df_bien_do_d['Index'], df_bien_do_d['Biên độ'])        
    
    plt.title(stock + " : " + stock)
    #plt.legend(loc='best',loc=2)
    plt.legend(distances,loc=2)
    plt.show()   

#draw_bien_do_d("VND",3)#
#draw_bien_do_d("VND",1)#
# draw_bien_do_d_s("VND",[1,5,10,20],100)
# draw_bien_do_d_s("BID",[1,5,10,20],100)
# draw_bien_do_d_s("FLC",[1,5,10,20],100)
#draw_mark_stocks()
# print(df.head(10))
# plt.plot(df)


def current_deep(df, start_index):
    '''
    ĐỘ SÂU HIỆN TẠI
    start: Chỉ số bắt đầu tính toán
    '''
    d = 1 #Khoảng cách hay còn gọi là số phiên tính toán, hoặc là khoảng cách tính toán, thời gian tính toán
    end = start_index #Do dữ liệu được sắp xếp ngược nên ta đánh số cũng đảo ngược
    start = start_index - d
    
    deep = 0
    for i in range(start,end):
        deep = np.sum(df.iloc[i]['%'])
    
    return deep

def test_deep(stock):
    df = db.GetStockData(stock=stock)
    start = 0
    d = 1
    rs = current_deep(df,start_index=start)
    print(rs)
    
test_deep("VND")