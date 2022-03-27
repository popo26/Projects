#Project from 301_02_soup

from urllib.error import HTTPError
import webbrowser
import requests
from requests.exceptions import ConnectionError, HTTPError

#Custom exception in case the server is down.
class ServerDownError(Exception):
    def __init__(self):
        self.message = "Server is not available."
  

class Ingredient():
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def get_info(self):
        self.wiki = f"https://en.wikipedia.org/wiki/{self.name}"
        try:
            response = requests.get(self.wiki)
            #Raising custom exception
            if response.status_code == 503:
                raise ServerDownError()
            webbrowser.open(self.wiki)
        except ConnectionError as c:
            print(f"\nCheck if you have the Internet. Can't retrieve wiki page requested.")
            print(f"ConnectionError: {c}")
        except ServerDownError as s:
            print(s.message)
        except NameError as n:
            print("\nCheck if you entered correct URL on line22.")
            print(f"NameError: {n}")
        except TypeError as t:
            print("\nCheck if you entered URL info on line22.")
            print(f"TypeError: {t}")
        
    def __str__(self):
        try:
            return f"\nThe info is here: {self.wiki}.\n{self.amount} {self.name}s avaialble."
            # print(f"\nThe info is here: {self.wiki}.\n{self.amount} {self.name}s avaialble.")
        except AttributeError as a:
            return f"\nCheck if you ran required method, which is get_info().\nAttributeError: {a}"
        except TypeError as t:
            return f"\nTypeError: Make sure you used 'return' instead of 'print' in str dunder method."

    def cook(self, menu):
        self.menu = menu
        recipe_wiki = f"https://en.wikipedia.org/wiki/{self.name}_{self.menu}"
        try:
            response = requests.get()
            #Raising custom exception
            if response.status_code == 503:
                raise ServerDownError()
            webbrowser.open(recipe_wiki)
        except ConnectionError as c:
            print(f"\nCheck if you have the Internet. Can't retrieve wiki page requested.")
            print(f"ConnectionError: {c}")
        except ServerDownError as s:
            print(s.message)
        except NameError as n:
            print("\nCheck if you entered correct URL on line57.")
            print(f"NameError: {n}")
        except TypeError as t:
            print("\nCheck if you entered URL info on line57.")
            print(f"TypeError: {t}")
        

        
p = Ingredient("strawberry", "3")
p.get_info()
# p.cook("sauce")
print(p)