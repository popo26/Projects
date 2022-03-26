from bs4 import BeautifulSoup
import requests
import json


class SearchMenu():
    def __init__(self, *name):
        self.name = input("\nWhat ingredients?\nSeparate by commas: ").lower()
        self.relevant_list = []
        self.relevant_link = []
        self.final_menu_list = []

    def recipe(self):
        #Get html file from the URL
        #Once json data is saved in 'recipe.json', comment out.
        base_url = "https://codingnomads.github.io/recipes/"
        response = requests.get(base_url)
        data = response.text

        #dump data to json file
        with open("recipe.json", "w") as file:
            json.dump(data,file)

        #read data from json file
        file = open("recipe.json", "r")
        data = json.load(file)

        soup = BeautifulSoup(data, "html.parser")

        relevant_anchor_tags = soup.select(selector="li a")

        #List of all the texts for anchor tags
        text_list = []
        for item in relevant_anchor_tags: 
            text = item.getText().lower()
            text_list.append(text)

        #Catch varieties of space input by user.
        name_list1 = self.name.split(",") 
        name_list2 = []
        for name in name_list1:
            if name.startswith(" ") and name.endswith(" "):
                fixed_name = name.strip(" ")
                name_list2.append(fixed_name)        
            elif name.startswith(" "):
                fixed_name = name.lstrip(" ")
                name_list2.append(fixed_name)
            elif name.endswith(" "):
                fixed_name = name.rstrip(" ")
                name_list2.append(fixed_name)
            else:
                name_list2.append(name)   

        relevant_index_list = []
        for text in text_list:
            for n in name_list2:
                if n in text:
                    self.relevant_list.append(text)
                    relevant_index = text_list.index(text) #Indexes of the relevant items in whole list(text_list)
                    relevant_index_list.append(relevant_index)

        #Using set() to remove duplicate from index
        index_set = set(relevant_index_list)
        final_index_list = sorted(list(index_set))
 
        #Find each link related to the menu by using index retrieved by above index list
        #Reorder menu_list, whose order is messed up due to using set
        for index in range(len(relevant_anchor_tags)):
            for i in range(len(final_index_list)):
                if final_index_list[i] == index:
                    link = 'https://codingnomads.github.io/recipes/' + relevant_anchor_tags[index].get('href')
                    self.relevant_link.append(link)
                    menu = relevant_anchor_tags[index].getText()
                    self.final_menu_list.append(menu)

        file.close()


    def __str__(self):
        backslash_n = "\n"
        return f"\n\nYour choice of ingredients are {self.name}.\n\nRelated results are:\n\n{backslash_n.join(self.final_menu_list)}\n\nLinks are:\n\n{backslash_n.join(self.relevant_link)}\n"
     
    def __repr__(self):
        return f"Menu: {self.final_menu_list}.\nLinks: {self.relevant_link}"
        

s = SearchMenu()
s.recipe()
print(s)
