#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    possible_plays = ['rock', 'paper', 'scissors']
    total_results = []  # will return a list completed with all possible plays

    # rounds control when the recursive function ends. It should be set to n
    # results is an empty list that records all plays
    def returns_plays(rounds, results=[]):
        if rounds == 0:
            # adds completed list to total_results when loop is done
            return total_results.append(results)
        for play in possible_plays:  # runs for each item in the list
            returns_plays(rounds - 1, results + [play])

    returns_plays(n)  # initializes the helper function or else it doesn't run
    return total_results


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
