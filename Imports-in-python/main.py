from utils.Discounts import get10Discount, get50Discount
from recipes.recipe1 import recipe1 as myRecipe1 # named import

price = get10Discount(100)
print(price)


price = get50Discount(100)
print(price)


recipe = myRecipe1()
print(recipe)