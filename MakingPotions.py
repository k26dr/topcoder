# SRM 433 R1D2L3
__author__ = 'kedar'

# NOTE: The easy way to do the price calculations is with pointers since you're
# simply figuring out unknown quantities from known ones through combinations, but
# because Python doesn't have pointers, we have to do it the hard way

class MakingPotions:

    # recipe -> (potion, formula)
    def _potionFormula(self, recipe: str):
        equal=recipe.index('=')
        return recipe[0:equal], recipe[equal+1:]

    # formula -> list(addend)
    def _getAddends (self, formula: str):
        return formula.split('+')

    # addend -> (ingredient, amount)
    def _splitAddend (self, addend: str):
        for i,c in enumerate(addend):
            if not(c.isdigit()):
                return addend[i:], int(addend[0:i])

    # list(ingredient, amount) -> price
    # undefined price is -1
    def _combineIngredients(self, ingredients: list, prices: dict):
        total=0
        for name, amount in ingredients:
            if name not in prices or prices[name] == -1:
                return -1
            total += prices[name] * amount
        return total

    # recipe -> price
    # combination of previous functions
    def _recipePrice(self, recipe: str, prices: dict):
        (potion, formula) = self._potionFormula(recipe)
        self._getAddends(formula)
        price = self._combineIngredients([self._splitAddend(a) for a in self._getAddends(formula)], prices)
        return potion, price

    # main function
    def getCost(self, recipes, marketGoods, cost):
        prices={}
        for i in range(len(marketGoods)):
            prices[marketGoods[i]] = cost[i]
        while True:
            cont=False
            for recipe in recipes:
                potion, price = self._recipePrice(recipe, prices)
                if potion not in prices or price < prices[potion] or price != prices[potion] == -1:
                    cont=True
                    prices[potion] = price
            if cont is False:
                break

        if "LOVE" not in prices:
            return -1
        elif prices["LOVE"] > 1000000000:
            return 1000000001
        return prices["LOVE"]

# tests
m = MakingPotions()
tests = []
answers = []

tests.append({'cost': [100, 1, 30], 'recipes': ['LOVE=5WATER+3HONEY'], 'marketGoods': ['LOVE', 'WATER', 'HONEY']})
answers.append(95)

tests.append({'cost': [2, 6, 9], 'recipes': ['LOVE=2WATER+4HONEY+2BEER', 'BEER=1HOP+3WATER+1HOP'],
         'marketGoods': ['WATER', 'HONEY', 'HOP']})
answers.append(76)

tests.append({'marketGoods': ["ORANGEJUICE", "APPLEJUICE"], 'cost': [6, 4],
              'recipes': ["JUICEMIX=1ORANGEJUICE+1APPLEJUICE"]})
answers.append(-1)

tests.append({'marketGoods': ["WATER", "HONEY", "HOP"], 'cost': [1,22,17],
              'recipes': ["LOVE=7WATER+3HONEY", "LOVE=2HONEY+2HOP"]})
answers.append(73)

tests.append({'marketGoods': ["OIL", "WATER"], 'cost': [60, 70],
              'recipes': ["FIRSTPOTION=1OIL+1SECONDPOTION", "SECONDPOTION=4WATER+1FIRSTPOTION", "LOVE=1FIRSTPOTION+1SECONDPOTION"]})
answers.append(-1)

tests.append({'marketGoods': ["HONEYBIT"], 'cost': [100],
            'recipes': ["LOVE=6HONEYMEGABYTE","HONEYMEGABYTE=2HONEYFIFTYTWELVEKBYTES",
            "HONEYFIFTYTWELVEKBYTES=8HONEYSIXTYFOURKBYTES","HONEYSIXTYFOURKBYTES=8HONEYEIGHTKBYTES",
            "HONEYEIGHTKBYTES=8HONEYKBYTE","HONEYKBYTE=2EIGHTBYEIGHTWORDS","EIGHTBYEIGHTWORDS=8EIGHTWORDS",
            "EIGHTWORDS=8HONEYWORD","HONEYWORD=8HONEYBYTE","HONEYBYTE=8HONEYBIT"] })
answers.append(1000000001)

tests.append({'marketGoods': ["WATER"], 'cost': [1], 'recipes': ["LOVE=1LOVE"]})
answers.append(-1)

tests.append({'marketGoods': ["MILK","WATER","HOP"], 'cost': [6,1,14],
            'recipes': ["NECTAR=4HOP+2MILK","LOVE=5MILK+3BEER","LOVE=2WATER+1LOVE","LOVE=2MIX+1NECTAR",
            "MIX=1MILK+1WATER+1HOP","BEER=5WATER+2HOP","LOVE=1NECTAR+3WATER+3HOP","NECTAR=3BEER+1MILK+2MILK"]})
answers.append(110)

for i in range(len(tests)):
    print(m.getCost(**tests[i]))
    assert m.getCost(**tests[i]) == answers[i]

print("Passed all tests")









