# learning the functions
def greet(name):
    print(f'Bonjour! {name}')
    print(f'Gutten morgen {name}')
    print(f'Good morning {name}')
greet("Michael")


#life in a week function
def life_in_weeks(years):
    years_left = 90 - years
    weeks_left = years_left * 52
    print(f'You have {weeks_left} weeks left.')

life_in_weeks(27)


#functions with more than one input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")
greet_with("Michael", "Bomso")

#positional and keyword argument
def greet_with(name, location):
    print(f'Hello {name}')
    print(f'What is it like in {location}')
greet_with(location = "Bomso", name = "Michael Baffour")