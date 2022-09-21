from datetime import datetime


class Transaction:
    BUY_FEE = 0.01 #%
    BUY_FEE = 0.01 #%

    BUY_TAX = 0.01 #%
    SELL_TAX = 0.01 #%

    BUY_DATE = datetime.now().today()
    #SELL_DATE = datetime.now().today()

    Quantity = -1 #Số âm là chưa mua
    PRICE = -1 #Số âm là chưa mua

class BuyTransaction:
    pass

class SellTransaction:
    pass



class TransactionBook:
    pass




class StockStore:
    stocks = None
    def __init__(self) -> None:
        self.Symbols = None

    def Insert(symbol, quantity, price, buy_date):
        pass
    def Delete(symbol,quanity,price,)
    def Report():
        pass

store: StockStore()

def Buy():
    #If buy
    store.Update()



    
