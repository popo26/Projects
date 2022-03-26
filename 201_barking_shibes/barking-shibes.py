# Use a quotes API, e.g. http://quotes.stormconsultancy.co.uk/random.json
# to fetch a random quote. Then use string manipulation to convert it to
# Doge speech (https://blogs.unimelb.edu.au/sciencecommunication/2016/10/22/how-to-speak-doge/)
# Create a tiny webpage that displays a doge image together
# with the altered quote. You can get an image URL from another API:
# http://shibe.online/api/shibes
# Write the code logic to make the API calls and assign the output to
# `doged_quote` and `doge_image_url` respectively.
# Then write the `html` string to a `.html` file and look at it in your browser.

import requests

quote_URL = "http://quotes.stormconsultancy.co.uk/random.json"

shiba_URL = "http://shibe.online/api/shibes?count=1"

response = requests.get(quote_URL)
data = response.json()
quote_data = data["quote"]
print(quote_data)

response2 = requests.get(shiba_URL)
data2 = response2.json()
shiba_img_URL = data2[0]
print(shiba_img_URL)

with open("index.html", "w") as file:
    file.write(f"<h1>{quote_data}</h1>\n<img src={shiba_img_URL}>")


 
    




