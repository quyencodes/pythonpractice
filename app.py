# print statement
# print("hello world")

# variables
# pascal case
# character_name = "John"
# character_age = 35
# is_Male = True

# print("There once was a man named", character_name + ", ")
# print("he was", str(character_age), "years old. ")

# character_name = "Mike"
# print("He really liked the name", character_name + ", ")
# print("but didn't like being", str(character_age) + ".")

# phrase = "Giraffe Academy"
# print(phrase.replace("Giraffe", "Elephant"))

# from math import *

# my_num = -5
# print(sqrt(36))

# name = input("Enter your name: ")
# age = input("Enter your age: ")
# print("Hi " + name + "! You are " + age)

# num1 = input("Enter a number: ")
# num2 = input("Enter another number: ")

# result = float(num1) + float(num2)
# print(result)

# Mad Libs Game
# color = input("Enter a color: ")
# plural_noun = input("Enter a plural noun: ")
# celebrity = input("Enter a celebrity name: ")

# print("Roses are " + color)
# print(plural_noun + " are blue")
# print("I love " + celebrity)

# Lists
# lucky_numbers = [8, 4, 15, 16, 23, 42]
# friends = ["Kevin", "Karen", "Jim", "Oscar", "Tony"]
# friends.extend(lucky_numbers)
# friends.append("Creed")
# friends.insert(1, "Kelly")
# friends.remove("Jim")
# friends.clear()
# friends.pop()
# lucky_numbers.reverse()
# friends2 = friends.copy()
# print(friends2)

# Tuples (immutable data structure)
# coordinates = (4, 5)
# print(coordinates)

# Functions
# def say_hi(name, age):
#   print("Hello " + name + ", you are " + age)

# name = input("Enter a name please: ")
# age = input("Enter an age: ")
# say_hi(name, age)

# Functions - return statements (continued)

# def cube(num):
#   return num * num * num

# result = cube(4)
# print(result)

# def max_num(num1, num2, num3):
#   if num1 >= num2 and num1 >= num3:
#     return num1
#   elif num2 >= num1 and num2 >= num3:
#     return num2
#   else:
#     return num3

# print(max_num(3, 40, 5))

# num1 = float(input("Enter first number: "))
# op = input("Enter operator: ")
# num2 = float(input("Enter second number: "))

# if op == "+":
#   print(num1 + num2)
# elif op == "-":
#   print(num1 - num2)
# elif op == "*":
#   print(num1 * num2)
# elif op == "/":
#   print(num1 / num2)
# else:
#   print("Invalid operator")

# Dictionaries
# monthConversions = {
#   "Jan": "January",
#   "Feb": "February",
#   "Mar": "March",
#   "Apr": "April",
#   "May": "May",
#   "Jun": "June",
#   "Jul": "July",
#   "Aug": "August",
#   "Sep": "September",
#   "Oct": "October",
#   "Nov": "November",
#   "Dec": "December"
# }
# print(monthConversions.get("Luv", "Not a valid key"))

# i = 1
# while i <= 10:
#   print(i)
#   i += 1

# print("Done with loop")

# secret_word = "giraffe"
# guess = ""
# guess_count = 0
# guess_limit = 3
# out_of_guesses = False

# while guess != secret_word and not(out_of_guesses):
#   if guess_count < guess_limit:
#     guess = input("Enter guess: ")
#     guess_count += 1
#   else:
#     out_of_guesses = True

# if out_of_guesses:
#   print("Out of guesses, you lose")
# else:
#   print("You win!")

# for letter in "Giraffe Academy":
  # print(letter)

# friends = ["Jim", "Karen", "Kevin"]
# for index in range(len(friends)):
#   if index == 0:
#     print("first iteration")
#   else:
#     print("not first")


# def raiseToPower(base_num, pow_num):
#   result = 1
#   for i in range(pow_num):
#     result *= base_num
#   return result

# print(raiseToPower(3, 2))

# number_grid = [
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9],
#   [0]
# ]

# for i in number_grid:
#   for j in i:
#     print(j)

# vowels -> g

# def translate(phrase):
#   translation = ""
#   for letter in phrase:
#     if letter.lower() in "aeiou":
#       if letter.isupper():
#         translation = translation + "G"
#       else:
#         translation = translation + "g"
#     else:
#       translation = translation + letter
#   return translation

# print(translate(input("Enter a phrase: ")))

# error handling
# try:
#   # value = 10/0
#   number = int(input("Enter a number: "))
#   print(number)
# except ZeroDivisionError as err:
#   print(err)
# except ValueError:
#   print("Invalid input")

# open("employee.txt", "w")
# open("employee.txt", "a")
# open("employee.txt", "r+")
# employee_file = open("employee.txt", "r")
# for employee in employee_file.readlines():
#   print(employee)
# print(employee_file.readlines())
# employee_file.close()

# employee_file = open("employee.txt", "a")
# employee_file.write("\nToby - Human Resources")
# employee_file.close()

# Modules and Pip