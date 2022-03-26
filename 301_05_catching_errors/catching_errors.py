#Project from 301_02_soup

import webbrowser
import requests

class Ingredient():
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def get_info(self):
        self.wiki = f"https://en.wikipedia.org/wiki/{self.name}"
        response = requests.get(self.wiki)
        webbrowser.open(self.wiki)
        
    def __str__(self):
        return f"The info is here: {self.wiki}.\n{self.amount} {self.name}s avaialble."

    def cook(self, menu):
        self.menu = menu
        recipe_wiki = f"https://en.wikipedia.org/wiki/{self.name}_{self.menu}"
        response = requests.get(recipe_wiki)
        webbrowser.open(recipe_wiki)

        
p = Ingredient("strawberry", "3")
p.get_info()
p.cook("sauce")
print(p)