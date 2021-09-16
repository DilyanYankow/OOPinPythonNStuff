# dictionary comprehensions = create dictionaries using an expression
#                               can replace loops and certain lambda functions
# dictionary =  {key: expression for (key, value) in iterable}

cities_in_F = {'New York': 32, 'Boston': 70, 'Los Angeles': 100, "Chicago": 50}

cities_in_C = {key: value*5/9 for (key, value) in cities_in_F.items()}

sunny_weather = {key: value for (key, value) in cities_in_F.items() if value == "Sunny"}


# desc_cities = {key: ("Warm" if value >=40 else "cold") for (key, value) in cities_in_F.items() if value == "Sunny"}

def check_temp(value):
    if value >=70:
        return "hot"

desc_cities = {key: ("Warm" if value >=40 else "cold") for (key, value) in cities_in_F.items()}
print(desc_cities)