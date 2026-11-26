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