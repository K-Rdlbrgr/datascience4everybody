# ============ CHALLENGE ==================

# Make the whole program loop and show a menu with an option to see our portfolio
# and to add a symbol to our portfolio


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

# Calcuating profits and losses of our prortfolio


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


# Adding a new stock to the portfolio
def addStock():
    # First we let the user type in all the necessary data for the investment
    ticker = input('Please tell me the ticker of the stock you would like to add: ').upper()
    volume = int(input(f'How many stocks of {ticker} did you buy? '))
    strike = float(input(f'How much did a single stock of {ticker} cost? '))

    # Then we append the new investment to our portfolio
    portfolio[ticker.lower()] = {'volume': volume, 'strike': strike}

    # We return a confirmation message for the successful purchase
    return f'Perfect! Your portfolio got updated with the purchase of {volume} shares of {ticker} for $ {price} each'


# Make the whole program loop and show a menu with an option to see our portfolio
# and to add a symbol to our portfolio
run = True

# Here the program starts with a while loop which is only exited if the user wants to stop the program
while run:

    # We start by printing the current portfolio
    print("Current Portfolio 💰💰💰 \n")
    for sym, pos in portfolio.items():
        total = pos['volume'] * pos['strike']
        print(f"{sym.upper()} Stock - {pos['volume']} bought for {pos['strike']}$ ({round(total,2)}$)")

    print("\n")

    # Now the request to the API is dynamic, so it will interpolate in the URL
    # only the symbols present in your portfolio
    symbols = ",".join(portfolio.keys())
    url = f"https://api.iextrading.com/1.0/tops/last?symbols={symbols}"

    # After their server responds we get a big str that needs to be parsed to
    # JSON so that we can use it in the Python world
    print("Fetching latest market prices 📡 ")
    print("Starting the API request ... ⏳⏳⏳")
    real_time_market = requests.get(url).json()
    print("🚀 Done! \nAPI response: \n", real_time_market)
    print("\n")

    # Our goal is to create dynamically our market dict
    market = {}

    # Populating the market dict with info from the API
    for stock in real_time_market:
        # get the company symbol and lowercase it, like we have in our portfolio
        stock_symbol = stock['symbol'].lower()
        market[stock_symbol] = stock['price']

    # Displaying new market values
    print('Updated Market values:')
    for name, price in market.items():
        print(f"{name.upper()} at {price}$")
    print('\n')

    # Calculating the current profits and losses on our portfolio
    print("💵 Computing PnL 💵")
    pnl = short_pnl(portfolio, market)
    print("\n")
    print(f"Total PnL: \n{pnl}$")

    # Asking the user if he/she wants to add a new stock or not
    check = input('Do you want to add a stock? (yes/no) ').lower()
    flag = True

    # We enter the new while loop and exit it striaght away if the user does
    # not want to add a new stock or after the user added the stock
    # successfully
    while flag:
        if check == 'yes':
            addStock()
            flag = False
        elif check == 'no':
            flag = False
        else:
            check = input('Oops. You made a spelling mistake. So, do you want to add a stock? (yes/no) ').lower()

    # Finally we ask the user if he/she wants to update the portfolio or if the program should be closed
    status = input('Do you want to update your portfolio or close the program? (run/close) ').lower()

    # In case the user wants to update the portfolio, the code runs again from
    # the start or if the user wants to close the program it exits the first
    # while loop and the script exits
    flag = True
    while flag:
        if status == 'run':
            flag = False
        elif status == 'close':
            flag, run = False, False
        else:
            status = input(
                'Oops. You made a spelling mistake. So, do you want to update your portfolio or close the program? (yes/no) ').lower()
