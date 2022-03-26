import requests

min_len = 4
max_len = 6
URL = f"https://uzby.com/api.php?min={min_len}&max={max_len}"



# Collect the name from your player

user_name = input("What is your name?: ")

# Check whether it meets the length requirements for the API call

if len(user_name) > 3 and len(user_name) < 7: 
    print("OK")
else:
    print("it should be between 4 and 6 characteres.")

# Ping the Uzby API to create a new random name for your player,

response = requests.get(URL)
random_name = response.text

#   using the length of their given name as input

len_random_name = len(random_name)

# Inform the player about their in-game name

print(f"your in-game name is {random_name}!")