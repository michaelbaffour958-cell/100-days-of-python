#CREATING A PASSWORD GENERATOR
import random


letter = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXTZ")
num = list("0123456789")
symbol = list('!@#$%&*(),')

print("Welcome to the PyPassword Generator!")
letter_input = int(input("How many letters will you like in your password?\n"))
symbol_input = int(input("How many symbols will you like?\n"))
number_input = int(input("How many numbers would you like?\n"))

password = ""

for char in range(letter_input):
    password += random.choice(letter)

for char in range(symbol_input):
    password += random.choice(symbol)

for char in range(number_input):
    password += random.choice(num)

print(f'This is your password: {password}')