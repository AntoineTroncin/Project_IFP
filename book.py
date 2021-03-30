import pandas as pd
from tabulate import tabulate 

class Order:
    def __init__(self, quantity, price, buy = True):
        self.quantity = quantity
        self.price = price
        self.buy = buy

    def __str__(self):
        return "%s @ %s" % (self.quantity, self.price)

#o = Order(5, 11.0) 

class Book:
    def __init__(self, name, liste = []):
        self.name = name
        self.liste = liste

    def insert_buy(self, quantity, price):
        ide = len(self.liste) + 1
        self.liste.append([quantity, price, ide, True])
        print ('--- Insert BUY ', quantity, '@', price, ' id = ', ide, ' on ', self.name)
        print ('Book on ', self.name)
        
        listesell = []
        for i in range(len(self.liste)):
            if(self.liste[i][3] == False):
                listesell += [self.liste[i]]
        if len(listesell) > 0:
            print ('     SELL ', listesell[0][0], '@', listesell[0][1], ' id = ', listesell[0][2])
        
        listebuy = []
        for i in range(len(self.liste)):
            if(self.liste[i][3] == True):
                listebuy += [self.liste[i]]
        n = len(listebuy)
        for i in range(1, n):
            cle = listebuy[i]
            j = i - 1
            while(j >= 0 and listebuy[j][1] >= cle[1]):
                listebuy[j+1] = listebuy[j]
                j = j - 1
                if(listebuy[j][1] == cle[1]):
                    if(listebuy[j][0] < cle[0]):
                        listebuy[j+1] = listebuy[j]

            listebuy[j+1] = cle
        for i in range(1, n+1):
            print ('     BUY ', listebuy[n-i][0], '@', listebuy[n-i][1], ' id = ', listebuy[n-i][2])
        
        print ('-----------------------------')

    def insert_sell(self, quantity, price):
        ide = len(self.liste) + 1
        self.liste.append([quantity, price, ide, False])

        print ('--- Insert SELL ', quantity, '@', price, ' id = ', ide, ' on ', self.name)

        listesell = []
        for i in range(len(self.liste)):
            if(self.liste[i][3] == False):
                listesell += [self.liste[i]]
        p = len(listesell)
        
        listebuy = []        
        for i in range(len(self.liste)):
            if(self.liste[i][3] == True):
                listebuy += [self.liste[i]]
        n = len(listebuy)

        for i in range(1, n):
            cle = listebuy[i]
            j = i - 1
            while(j >= 0 and listebuy[j][1] >= cle[1]):
                listebuy[j+1] = listebuy[j]
                j = j - 1
                if(listebuy[j][1] == cle[1]):
                    if(listebuy[j][0] < cle[0]):
                        listebuy[j+1] = listebuy[j]

            listebuy[j+1] = cle
        
        stock = listebuy[n-1][0]
        if(p >= 2):
            if(quantity > listebuy[n-1][0]):
                print ('Execute ', listebuy[n-1][0], ' at ', listebuy[n-1][1], ' on ', self.name)
                print ('Execute ', quantity-listebuy[n-1][0], ' at ', listebuy[n-2][1], ' on ', self.name)
                listebuy[n-2][0] = listebuy[n-2][0] - quantity + listebuy[n-1][0]
            else:
                print ('Execute ', listebuy[n-1][0] - quantity, ' at ', listebuy[n-1][1], ' on ', self.name)
                listebuy[n-1][0] = quantity
        else:
            None

        print ('Book on ', self.name)
        print ('     SELL ', listesell[0][0], '@', listesell[0][1], ' id = ', listesell[0][2])
        
        if(quantity > stock):
            for i in range(2,n+1):
                print ('     BUY ', listebuy[n-i][0], '@', listebuy[n-i][1], ' id = ', listebuy[n-i][2])
        else:
            for i in range(1,n+1):
                print ('     BUY ', listebuy[n-i][0], '@', listebuy[n-i][1], ' id = ', listebuy[n-i][2])
        print ('-----------------------------')


    def dataframe(self):
        quantitybuy = []
        pricebuy = []
        quantitysell = []
        pricesell = []
        for i in range(len(self.liste)):
            if(self.liste[i][3]):
                quantitybuy += [self.liste[i][0]]
                pricebuy += [self.liste[i][1]]
            else :
                quantitysell += [self.liste[i][0]]
                pricesell += [self.liste[i][1]]

        BUY = { "quantity buy : " : quantitybuy, "price buy :" : pricebuy}
        SELL = { "price sell :" : pricesell, "quantity sell :" : quantitysell}

        resBUY = pd.DataFrame(BUY)
        resSELL = pd.DataFrame(SELL)

        print(tabulate(resBUY, headers = 'keys', tablefmt = 'psql'))
        print(tabulate(resSELL, headers = 'keys', tablefmt = 'psql'))





#book = Book("TEST")
#book.insert_buy(10, 10.0)
#book.insert_sell(120, 12.0)
#book.insert_buy(5, 10.0)
#book.insert_buy(2, 11.0)
#book.insert_sell(1, 10.0)
#book.insert_sell(10, 10.0)

#book.dataframe()

