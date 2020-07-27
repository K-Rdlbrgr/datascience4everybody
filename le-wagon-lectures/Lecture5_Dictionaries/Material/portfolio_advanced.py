# pylint: disable=missing-docstring

# TODO: start by defining a `portfolio` using a dict!

# How to store the data? What structures should we use?

# portfolio is a dictionary with the keys as the stock symbols and the values 
# as another dictionary
portfolio = {
  'aapl': {'volume': 10 , 'strike': 154.12 },
  'goog': {'volume': 2, 'strike': 812.56 },
  'tsla': {'volume': 12, 'strike': 342.12 },
  'fb': {'volume': 18, 'strike': 209.0 }
  }

market = {
  "aapl":  198.84,
  "goog": 1217.93,
  "tsla":  267.66,
  "fb":    179.06
}

# Reading some stats
print('Portfolio Dict: \n', portfolio)
print('TSLA Volume', portfolio['tsla']['volume'])
print('GOOG Strike', portfolio['goog']['strike'])
print('=========================================')


# P&L 
def short_pnl(positions, mtm):
    result = []
    
    # iterate the portfolio dictionary
    for name, pos in portfolio.items():
        # name: str
        # pos: dictionary
        # for each element append the pnl to a new list
        result.append(mtm[name] - pos['strike'])
    
    return sum(result)


# ==== TESTS ====

# 1. using the variables on top of the file
print('PnL: ', short_pnl(portfolio, market))    

# 2. 
portfolio = {
  'aapl': {'volume': 10 , 'strike': 100 },
  'goog': {'volume': 2, 'strike': 140 },
  'tsla': {'volume': 12, 'strike': 200 },
  }

market = {
  "aapl":  110,
  "goog": 120,
  "tsla":  180,
}

print('PnL: ', short_pnl(portfolio, market))
# (110 - 100) + (120 - 140) + (180 - 200) = -30
# -30

# 3. Changing the market values only for test purposes
market['aapl'] = 90
market['goog'] = 160
market['tsla'] = 230

print('PnL: ', short_pnl(portfolio, market))
# (90 - 100) + (160 - 140) + (230 - 200) = -10 + 20 + 30 = 40
# 40

