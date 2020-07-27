# pylint: disable=missing-docstring

aapl = [10, 154.12]
goog = [2, 812.56]
tsla = [12, 342.12]
fb = [18, 209.0]

portfolio = [aapl, goog, tsla, fb]


#            AAPL     GOOG    TSLA      FB
market = [198.84, 1217.93, 267.66, 179.06]


def pnl_calculation(portfolio, market):

    # We assign the initial pnl as 0
    pnl = 0

    # We loop through the stocks in our portfolio and calculate the profits and losses
    for index, stock in enumerate(portfolio):
        pnl += (market[index] - stock[1]) * stock[0]

    # We return the rounded pnl
    return round(pnl, 1)


# We call the function and print the output
print(pnl_calculation(portfolio, market))
