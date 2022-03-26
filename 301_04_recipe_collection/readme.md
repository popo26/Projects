PROJECT: Recipe Collection
Over the previous sections, you've learned about the concepts of OOP in Python, and how everything is an object in Python. Then you applied object-oriented programming when you used different requests and BeautifulSoup() objects to scrape information from the Internet.

For this project, your task is to create a CLI that takes as an input the names of ingredients from a user. Then, your code will fetch the recipe information from the CodingNomads recipe collection, and search through the text of the recipes to find ones that include the provided ingredients.

Feel free to integrate your custom Ingredient() and Soup() classes into the code base, to get some additional practice in working with your custom Python classes.

Info: Remember to be respectful when scraping the web. To minimize the amount of pressure your script puts on the website, and to make the script also work without an Internet connection, you can fetch the information once and save it to a file structure or a database. You can learn more about how to do that in the Python APIs and Databases and the SQL & Databases courses.
You might get by with a str.find() method to check through the content of the recipes. However, if you want to build a more sophisticated project, you could for example experiment with including amounts of ingredients, and finding whether the provided amount a user has is sufficient for cooking a recipe.

In the next lesson, you'll find some optional information about advanced string matching techniques using regular expressions in Python, that can help you to achieve that goal.