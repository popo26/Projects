import requests
import webbrowser
import os
from dotenv import load_dotenv
import json
import time

load_dotenv()

API_KEY = os.getenv("API_KEY")

class Ingredient():
    def __init__(self,**amount):
        self.amount = amount

    # def __str__(self):
    #     return f"Your ingredients are {[k for k in self.amount.keys()]}. Amount is {[v for v in self.amount.values()]}"

class Spice(Ingredient):
    ### EXTENDED TASK 1:
    # take the amount of each Ingredient() into account. How can you work that into creating a recipe the user can actually cook?
    # Ai firstly used *name only to take ingredient names without amount(However without *(args) I could still take in multiple ingredients. So not sure what is the benefit of using *(args)here). Then i, ntroduced **amount, noticed I don't need *name since **amount covers both ingredient names and quantity so I removed *name.
    ###
    def __init__(self, **amount):
        super().__init__(amount=amount)
        self.spice_amount = amount
        self.meal_titles = []
        self.source_urls = []
        self.dictionary = {}
        self.better_ing_list = []
        self.recipe_ids = []
    
    def __str__(self):
        return f"Your spices are {[k for k in self.spice_amount.keys()]}. Amount is {[v for v in self.spice_amount.values()]}"

class Soup(Spice):
    def __init__(self, **amount):
        super().__init__(amount=amount) 
             
        self.amount = input("\nWhat ingredients would you like to use?\nType name=number separated by commas.\ne.g. 'potato=3': ")
        # print(type(self.amount))  --> I thought kwargs will create a dictionary but it is creating a string
        print("Check the example of input syntax. e.g, potato=3.")

        #Create a dictionary of ingredients(keys) and amount(values)
        try:
            self.dictionary = dict((x.strip(), y.strip()) for x, y in (element.split('=') for element in self.amount.split(', ')))
        except ValueError:
            (print("\nPlease make sure the ingredient entry is like this: e.g.potato=2"))

        #Create a list of keys(ingredients)
        self.recipe_ids = []
        self.ingredients_list = []
        self.missing_ing_lines = []
        for k in self.dictionary.keys():
            self.ingredients_list.append(k)

    def cook(self):
        ###EXTENDED TASK2:
        # interface with a recipe API instead of concatenating a web search URL. Receive the API response data, format it, and display it as command-line output.
        ###
        spoonacular_url = f"https://api.spoonacular.com/recipes/findByIngredients?apiKey={API_KEY}&ingredients={self.ingredients_list}&number=3"
        response = requests.get(spoonacular_url)
        data = response.json()
        meal_photos = []
        missing_items = []
        missing_count = []

        for i in range(len(data)):
            self.meal = data[i]["title"]
            self.meal_titles.append(self.meal)
            meal_photo = data[i]["image"]
            meal_photos.append(meal_photo)
            id = data[i]["id"]
            self.recipe_ids.append(id)
            missing_ingredient_count = data[i]["missedIngredientCount"]
            missing_count.append(missing_ingredient_count)
            # webbrowser.open(meal_photo) #Uncomment if you want to see the meal photos
            missing = []
            for m in range(missing_ingredient_count):
                missing_ingredients = data[i]["missedIngredients"][m]["name"]
                missing.append(missing_ingredients)
            missing_items.append(missing)


        #Print out missing ingredients for each menu.
        for index in range(len(self.meal_titles)):
            bakslash_n = '\n'
            line = (f"\nThere are {missing_count[index]} missing ingredients for \"{self.meal_titles[index]}\", which are ...\n{bakslash_n.join(missing_items[index])}")
            self.missing_ing_lines.append(line)


        #Check quantity of used ingredients
        self.required_quantity_used_ingredients = []

        x = data
        for i in range(len(x)):
            each_menu = []
            for item in data[i]["usedIngredients"]:
                for i2 in range(len(data[i]["usedIngredients"])):
                    qua_unit = []
                    a = str(item["amount"])
                    u = item["unit"]
                    n = item["name"]
                    qua_unit.append(n)
                    qua_unit.append(a)
                    qua_unit.append(u)
                each_menu.append(qua_unit)
            self.required_quantity_used_ingredients.append(each_menu)
        # print('\nThe ingredients user has VS the required quantity for this recipe:')
        # print(self.required_quantity_used_ingredients)

        #For readability for user
        for menu in self.required_quantity_used_ingredients:
            one = []
            for each_ing in menu:
                two = []
                ing = "-".join(each_ing)
                two.append(ing)
                one.append(two)
            self.better_ing_list.append(one)
      
        #Get source_URLs for each recipe
        for i in range(len(self.recipe_ids)):
            spoonacular_recipe_url = f"https://api.spoonacular.com/recipes/{self.recipe_ids[i]}/information?apiKey={API_KEY}"
            response = requests.get(spoonacular_recipe_url)
            data = response.json()
            recipe_url = data["sourceUrl"]
            self.source_urls.append(recipe_url)
       
    def __str__(self):
        backslash_n = '\n'
        return f"\nYour ingredients are {[k for k in self.dictionary.keys()]}.\nAmount is {[v for v in self.dictionary.values()]}.\n\nMy 3 suggestions for recipes are: \n(1){self.meal_titles[0]}***🥄***{self.source_urls[0]}\n**********The required quanty of ingredients you currently have are **********\n**********{[item for item in self.better_ing_list[0]]}\n\{self.missing_ing_lines[0]}\n\n(2){self.meal_titles[1]}***🥄***{self.source_urls[1]}\n**********The required quanty of ingredients you currently have are **********\n**********{[item for item in self.better_ing_list[1]]}\n{self.missing_ing_lines[1]}\n\n(3){self.meal_titles[2]}***🥄***{self.source_urls[2]}\n**********The required quanty of ingredients you currently have are **********\n**********{[item for item in self.better_ing_list[2]]}\n{self.missing_ing_lines[0]}\n\n"

#!!Ai wants to add missing ingredient info under def __str__!!

###TASK3:
#create child classes to Soup() that have specific qualities.

class Information(Soup):

    def calory(self):
        #super().cook() # Without inheriting cook method I can't retrieve outputs

        spoonacular_url = f"https://api.spoonacular.com/recipes/findByIngredients?apiKey={API_KEY}&ingredients={self.ingredients_list}&number=3"
        response = requests.get(spoonacular_url)
        data = response.json()
        meal_photos = []

        for i in range(len(data)):
            self.meal = data[i]["title"]
            self.meal_titles.append(self.meal)
            meal_photo = data[i]["image"]
            meal_photos.append(meal_photo)
            id = data[i]["id"]
            self.recipe_ids.append(id)

        #Here down is original
        calory_info_list = []
        calory_info_dict = {
                "calories": "",
                "fat": "",
                "protein": "",
            }
        for i in range(len(self.recipe_ids)):
            spoonacular_nutrition_url = f"https://api.spoonacular.com/recipes/{self.recipe_ids[i]}/nutritionWidget.json?apiKey={API_KEY}"
            response = requests.get(spoonacular_nutrition_url)
            data = response.json()
            calory_info_dict["calories"] = data["calories"]
            calory_info_dict["fat"] = data["fat"]
            calory_info_dict["protein"] = data["protein"]
            calory_info_list.append(calory_info_dict)

        print(f"\n\n{self.meal_titles[0]} info:\n==========Total Calories: {calory_info_list[0]['calories']}==========\n==========Total Fat: {calory_info_list[0]['fat']}==========\n==========Total Protein: {calory_info_list[0]['protein']}==========.\n\n{self.meal_titles[1]} info:\n==========Total Calories: {calory_info_list[1]['calories']}==========\n==========Total Fat: {calory_info_list[1]['fat']}==========\n==========Total Protein: {calory_info_list[1]['protein']}==========.\n\n{self.meal_titles[2]} info:\n==========Total Calories: {calory_info_list[2]['calories']}==========\n==========Total Fat: {calory_info_list[2]['fat']}==========\n==========Total Protein: {calory_info_list[2]['protein']}==========.")

    def gluten(self):
        super().cook()

        spoonacular_url = f"https://api.spoonacular.com/recipes/findByIngredients?apiKey={API_KEY}&ingredients={self.ingredients_list}&number=3"
        response = requests.get(spoonacular_url)
        data = response.json()
        meal_photos = []

        for i in range(len(data)):
            self.meal = data[i]["title"]
            self.meal_titles.append(self.meal)
            meal_photo = data[i]["image"]
            meal_photos.append(meal_photo)
            id = data[i]["id"]
            self.recipe_ids.append(id)

        #Here down original
        self.gultenfree_infos = []
        gulten_dict = {
            "gulten_free": "",
        }
        for i in range(len(self.recipe_ids)):
            spoonacular_info_url = f"https://api.spoonacular.com/recipes/{self.recipe_ids[i]}/information?apiKey={API_KEY}"
            response = requests.get(spoonacular_info_url)
            data = response.json()
            gulten_info = data["glutenFree"]
            gulten_dict["gulten_free"] = gulten_info
            self.gultenfree_infos.append(gulten_dict)

        print(f"\n\n{self.meal_titles[0]} has gulten: {self.gultenfree_infos[0]['gulten_free']}.\n{self.meal_titles[1]} has gulten: {self.gultenfree_infos[1]['gulten_free']}.\n{self.meal_titles[2]} has gulten: {self.gultenfree_infos[2]['gulten_free']}.")

# soup = Soup()
# soup.cook()
# print(soup)

info = Information()
info.cook()
print(info)

info.calory() # why print out "missing ingredients" line when cook() is overwritten
#time.sleep(3)
info.gluten() # why print out "missing ingredients" line when cook() is overwritten


##Work in Progress, 2 parent classes have no meaning.
#If I dont add (self.name and) self.spice_name - due to MRO, before it gets self.spice_name it goes to API link and erros due to not able to find self.spice_name since it goes to cook() before get the attribute
#Feel like not fully understood args and kwargs.self.name works without *name.

#if daily 150 points ran out. Try again tomorrow


