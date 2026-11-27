# # learning the functions
# def greet(name):
#     print(f'Bonjour! {name}')
#     print(f'Gutten morgen {name}')
#     print(f'Good morning {name}')
# greet("Michael")


# #life in a week function
# def life_in_weeks(years):
#     years_left = 90 - years
#     weeks_left = years_left * 52
#     print(f'You have {weeks_left} weeks left.')

# life_in_weeks(27)


# #functions with more than one input
# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}")
# greet_with("Michael", "Bomso")

# #positional and keyword argument
# def greet_with(name, location):
#     print(f'Hello {name}')
#     print(f'What is it like in {location}')
# greet_with(location = "Bomso", name = "Michael Baffour")


# Love Calculator
def calculate_love_score(name1, name2):
    combined_names = (name1 + name2).lower()

    true_count = 0
    for letter in "true":
        true_count += combined_names.count(letter)

    love_count = 0
    for letter in "love":
        love_count += combined_names.count(letter)

    score = int(str(true_count) + str(love_count))
    print(score)

calculate_love_score("Michael", "Erica")


