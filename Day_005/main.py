#CREATING A PASSWORD GENERATOR
import random


letter = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXTZ")
num = list("0123456789")
symbol = list('!@#$%&*(),')

password = ""

print("Welcome to the PyPassword Generator!")
letter_input = int(input("How many letters will you like in your password?\n"))
symbol_input = int(input("How many symbols will you like?\n"))
number_input = int(input("How many numbers would you like?\n"))