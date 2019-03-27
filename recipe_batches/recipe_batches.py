#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    batches_by_ingredient = []
    for recipe_ingredient in recipe:
        if recipe_ingredient in ingredients:
            batches = ingredients[recipe_ingredient] / \
                recipe[recipe_ingredient]
            batches_by_ingredient.append(math.floor(batches))
        else:
            batches_by_ingredient.append(0)
            break  # you only need to loop for as long as there's enough ingredients
    return min(batches_by_ingredient)


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
