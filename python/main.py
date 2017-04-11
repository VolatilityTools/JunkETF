
## import data, load into dataframes

import pandas as pd



## Date	Open	High	Low	Close	Volume	Adj Close

hyg_prices = pd.read_csv('C:/Github/hyg prices.csv', names=['Date', 'Open', 'High', \
    'Low', 'Close', 'Volume', 'Adj Close'], skiprows=1)
    
    
## Date	Dividends
hyg_dividends = pd.read_csv('C:/Github/hyg dividends.csv', names=['Date', \
    'Dividends'], skiprows=1)
    
    
sorted_dividends = hyg_dividends.sort(['Date'], ascending=1)    

hyg_prices = hyg_prices.sort(['Date'], ascending=1)    

sorted_dividends.plot()


hyg_prices = hyg_prices.drop('Open', 1)
hyg_prices = hyg_prices.drop('High', 1)
hyg_prices = hyg_prices.drop('Low', 1)
hyg_prices = hyg_prices.drop('Volume', 1)

hyg_prices.plot()




