#!/usr/bin/python

import argparse


def find_max_profit(prices):
    # this keeps track of how much we've spent
    purchase_price = prices[0]
    # this keeps track of the current max profit
    profit = prices[1] - purchase_price

    # start at index 1 because we've already done the first computation
    for price in prices[1:]:
        # returns the bigger number
        profit = max(price - purchase_price, profit)
        # returns the smaller number
        purchase_price = min(purchase_price, price)

    return profit


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
