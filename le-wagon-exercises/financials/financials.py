# pylint: disable=missing-docstring
import math

# TODO: 1st exercise: Define the `forward_price` function
def forward_price(spot, interest_rate, time):
    # Return the whole Forward Price function at once
    return round(spot * math.e ** (interest_rate * time), 2)

# TODO: 2nd exercise: Define the `short_pnl` function
def short_pnl(positions, mtm):
    result = 0
    # Looping through the lists and add te difference to the result
    for index in range(0, len(positions)):
        result += positions[index] - mtm[index]
    # Return the result
    return result
            