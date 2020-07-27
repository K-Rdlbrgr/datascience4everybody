# pylint: disable=missing-docstring

# TODO: start by defining a `portfolio` using a dict!

# import request module
import requests

# Assigning the portfolio dictionary
portfolio = {
    'AAPL': {
        'vol': 10,
        'strike': 154.12
    },
    'GOOG': {
        'vol': 2,
        'strike': 812.56
    },
    'TSLA': {
        'vol': 12,
        'strike': 342.12
    },
    'FB': {
        'vol': 18,
        'strike': 209.0
    }
}

# Print out some information of the stocks within the portfolio
print(f' The volume of TSLA stocks in the portfolio is: {portfolio["TSLA"]["vol"]}')
print(f' The strike price of GOOG stocks in the portfolio is: {portfolio["GOOG"]["strike"]}')

# Calling the IEX API to get real life stock prices
url = "https://api.iextrading.com/1.0/tops/last?symbols=AAPL,GOOG,TSLA,FB"
real_time_market = requests.get(url).json()

# What type is the variable we stored the funtion output in and how does it look?
print(type(real_time_market))
print(real_time_market)


# Transforming the real time data into a similar data structure as the portfolio
real_portfolio = {}

for index, stock in enumerate(real_time_market):
    real_portfolio[stock['symbol']] = {'vol': stock['size'], 'strike': stock['price']}

# The new dictionary looks ver much the same
print(real_portfolio)


# Updating the API to be dynamic
tickers = ','.join([ticker for ticker in portfolio.keys()])

# Calling the IEX API to get real life stock prices
url = "https://api.iextrading.com/1.0/tops/last?symbols=AAPL,GOOG,TSLA,FB"
dynamic_real_time_market = requests.get(url).json()

# Now it automatically changes the tickers and data
print(f'This is our current portfolio: {dynamic_real_time_market}')


# Let's make the API dynamic based on the actual portfolio
# If we add Amazon to the portfolio now, the code right now would still
# ignore the Amazon stock and return the same portfolio
portfolio['AMZN'] = {
    'vol': 10,
    'strike': 1812.11
}

dynamic_real_time_market = requests.get(url).json()

print(f'Before making the call dynamic: {dynamic_real_time_market}')

# We need to adjust the URL accordingly by making it dynamic.
# We can achieve this by connecting the last bit of the URL call with the actualy portfolio stocks
stocks = ','.join([stock for stock, values in portfolio.items()])

# Now we have a string of tickers in the same format as in the URL which the API needs to work
print(stocks)

# Using the new dynamic URL now will include the Amazon stock
url = f'https://api.iextrading.com/1.0/tops/last?symbols={stocks}'
dynamic_real_time_market = requests.get(url).json()

print(f'After making the call dynamic: {dynamic_real_time_market}')
