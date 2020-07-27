# -*- coding: utf-8 -*-

# =============== API =====================
import requests
# We use the requests python library do perform the request

print("\n\n==========================================================\n")
print("\t🤑 Welcome DS4Everybody Portfolio Manager! 🤑")
print("\n==========================================================\n\n")

# Our Portfolio
portfolio = {
    'aapl': {'volume': 10, 'strike': 154.12},
    'goog': {'volume': 2, 'strike': 812.56},
    'tsla': {'volume': 12, 'strike': 342.12},
    'fb': {'volume': 18, 'strike': 300.0}
}

print("Current Portfolio 💰💰💰 \n")
for sym, pos in portfolio.items():
    total = pos['volume'] * pos['strike']
    print(f"{sym.upper()} Stock - {pos['volume']} bought for {pos['strike']}$ ({round(total,2)}$)")

print("\n")

# Now the request to the API is dynamic, so it will interpolate in the URL
# only the symbols present in your portfolio
symbols = ",".join(portfolio.keys())
url = f"https://api.iextrading.com/1.0/tops/last?symbols={symbols}"

# If we open the URL in the browser we get something like this:
# [
#     {
#         "symbol": "AAPL",
#         "price": 389.58,
#         "size": 100,
#         "time": 1595261748102
#     },
#     {
#         "symbol": "GOOG",
#         "price": 1555.69,
#         "size": 100,
#         "time": 1595261350794
#     },
#      ...
# ]
#

# After their server responds we get a big str that needs to be parsed to
# JSON so that we can use it in the Python world

print("Fetching latest market prices 📡 ")
print("Starting the API request ... ⏳⏳⏳")
real_time_market = requests.get(url).json()
print("🚀 Done! \nAPI response: \n", real_time_market)
print("\n")

# API response:
# [ {'symbol': 'AAPL', 'price': 389.77, 'size': 100, 'time': 1595261882570}, ...
# So the variable 'real_time_market' is a list


# Our goal is to create dynamically our market dict
market = {}

# Populating the market dict with info from the API
for stock in real_time_market:
    # get the company symbol and lowercase it, like we have in our portfolio
    stock_symbol = stock['symbol'].lower()
    market[stock_symbol] = stock['price']

# Equivalent to:
#market = dict((stock['symbol'].lower(), stock['price']) for stock in real_time_market)


# displaying new market values
print('Updated Market values:')
for name, price in market.items():
    print(f"{name.upper()} at {price}$")
print('\n')


# Same function
def short_pnl(positions, mtm):
    result = []

    # iterate the portfolio dictionary
    for name, pos in portfolio.items():
        # name: str
        # pos: dictionary
        # for each element append the pnl to a new list
        pnl = (mtm[name] * pos['volume']) - (pos['strike'] * pos['volume'])
        #pnl = mtm[name] - pos['strike']
        print(f"PnL {name.upper()}: {round(pnl, 2)}$")
        result.append(pnl)

    return sum(result)


print("💵 Computing PnL 💵")
pnl = short_pnl(portfolio, market)
print("\n")
print(f"Total PnL: \n{pnl}$")

# OBS
# Of course it would be more accurate if we calculated the Pnl, not with a single
# stock but with the volume that we bough (our_volume * market) - (our_volume * strike)
# So i commented out the previous version.

# Challenge! Improve my code!
# Add the possibility of adding more stocks by asking the symbols to the user
# and save them in the portfolio


def addStock():
    ticker = input('Please tell me the ticker of the stock you would like to add: ').upper()
    volume = int(input(f'How many stocks of {ticker} did you buy? '))
    strike = float(input(f'How much did a single stock of {ticker} cost? '))
    portfolio[ticker] = {'volume': volume, 'strike': strike}

    return f'Perfect! Your portfolio got updated with the purchase of {volume} shares of {ticker} for $ {price} each'
