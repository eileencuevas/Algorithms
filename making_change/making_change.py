#!/usr/bin/python

import sys


def making_change(amount, denominations, cache=None):
    # first pass attempt:

    # if amount < 0:
    #     return 0
    # elif amount == 0:
    #     return 1
    # elif not denominations:
    #     return 0
    # else:
    #     return making_change(amount, denominations[:-1]) + making_change(amount - denominations[-1], denominations)

    # second pass attempt, with cache
    if not cache:
        cache = {int: 0 for int in range(amount + 1)}
        cache[0] = 1

    for coin in denominations:
        for higher_amount in range(coin, amount + 1):
            difference = higher_amount - coin
            cache[higher_amount] += cache[difference]

    return cache[amount]


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print("There are {ways} ways to make {amount} cents.".format(
            ways=making_change(amount, denominations), amount=amount))
    else:
        print("Usage: making_change.py [amount]")
