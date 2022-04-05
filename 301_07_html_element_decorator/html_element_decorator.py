

def tagify(tag):
    def decorator(function):
        def wrapper(*args):
            function_output = function(*args)
            print(f"<{tag}>{function_output}</{tag}>")
            return function(*args)
        return wrapper
    return decorator


@tagify("p")  
def greet(name):
    return f"Hello, {name}"

@tagify("div")
def lorem():
    return "Lorem ipsum dolor sit amet, ..."

@tagify("h1")
def ingredients(red, green, yellow):
    return f"Ingredients are {red}, {green}, and {yellow}."



print(greet("Bessy"))
print(lorem())
print(ingredients("red capsicum", "coriander", "banana"))