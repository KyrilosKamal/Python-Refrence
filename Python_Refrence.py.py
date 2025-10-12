#!/usr/bin/env python3

# ---------------------------------------------------------------------------- #
# لو هنعمل سكريبت python يشتغل على لينكس لازم نضيف السطر ده فى الاول
# #!/usr/bin/env python3
# زيه زى ال bash script #!/bin/bash
# ---------------------------------------------------------------------------- #

# print Function
# print("Hello, World!")
# ---------------------------------------------------------------------------- #
# Variables
# name = "Kyrillos"
# age = 30
# print(f"my name is {name} and I am {age} years old.")

# x = 10
# y = 5
# print(x + y)  # Addition
# ---------------------------------------------------------------------------- #
# Data Types
# name = "Kyrillos"  # String
# age = 30  # Integer
# height = 5.9  # Float
# is_student = True  # Boolean

# print(type(name))  # <class 'str'>
# print(type(age))  # <class 'int'>
# print(type(height))  # <class 'float'>
# print(type(is_student))  # <class 'bool'>
# ---------------------------------------------------------------------------- #
# Type Conversion
# age = "30"
# print(type(age))  # <class 'str'>
# age = int(age)
# print(type(age))  # <class 'int'>
# ---------------------------------------------------------------------------- #
# User Input
# name = input("Enter your name: ")
# age = input("Enter your age: ")
# print(f"Hello, {name}. You are {age} years old.")
# ---------------------------------------------------------------------------- #
# Conditional Statements
# age = int(input("Enter your age: "))
# if age < 18:
#     print("You're a minor")
# elif age == 18:
#     print("Just became an adult")
# else:
#     print("You're an adult")
# ---------------------------------------------------------------------------- #
# Loops
# for loop
# for index in range(10):
#     print(index)

# while loop
# count = 0
# while count < 5:
#     print(count)
#     count += 1
# ---------------------------------------------------------------------------- #
# Functions
# def greet(name):
#     print(f"Hello, {name}!")

# greet("Kyrillos")
# ---------------------------------------------------------------------------- #
# Lists
# fruits = ["apple", "banana", "cherry"]
# print(fruits[0])  # Accessing elements
# fruits.append("orange")  # Adding elements
# print(fruits)
# fruits.remove("banana")  # Removing elements
# print(fruits)
# print(len(fruits))  # Length of the list
# ---------------------------------------------------------------------------- #
# Tuples
# my_tuple = (1, 2, 3)
# print(my_tuple[0])
# ---------------------------------------------------------------------------- #
# Sets
# my_set = {1, 2, 3}
# my_set.add(4)
# my_set.remove(2)
# print(my_set)
# ---------------------------------------------------------------------------- #
# Dictionaries
# person = {"name": "Kyrillos", "age": 30, "city": "Cairo"}
# print(person["name"])  # Accessing values
# person["age"] = 31  # Modifying values
# person["job"] = "Engineer"  # Adding key-value pairs
# del person["city"]  # Removing key-value pairs
# print(person)
# print(len(person))  # Length of the dictionary
# ---------------------------------------------------------------------------- #
# List Comprehension
# squares = [x * x for x in range(10)]
# print(squares)
# ---------------------------------------------------------------------------- #
# Lambda Functions
# square = lambda x: x * x
# print(square(5))
# ---------------------------------------------------------------------------- #
# Classes and Objects
# class Person:
#     def __init__(self):
#         self.name = "Kyrillos"
#         self.age = 30

#     def greet(self):
#         print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# person1 = Person()
# person1.greet()
# ---------------------------------------------------------------------------- #
# Inheritance
# class Animal:
#     def speak(self):
#         print("Animal speaks")

# class Dog(Animal):
#     def speak(self):
#         print("Dog barks")

# animal = Animal()
# dog = Dog()
# animal.speak()
# dog.speak()
# ---------------------------------------------------------------------------- #
# Decorators
# def my_decorator(func):
#     def wrapper():
#         print("Before")
#         func()
#         print("After")
#     return wrapper

# @my_decorator
# def say_hello():
#     print("Hello!")

# say_hello()
# ---------------------------------------------------------------------------- #
# Context Manager
# class MyFile:
#     def __enter__(self):
#         print("Opening file")
#         return self

#     def __exit__(self, exc_type, exc_value, traceback):
#         print("Closing file")

# with MyFile():
#     print("Inside context")
# ---------------------------------------------------------------------------- #
# File Handling
# with open("example.txt", "w") as file:
#     file.write("Hello, World!\n")

# with open("example.txt", "r") as file:
#     content = file.read()
#     print(content)

# with open("example.txt", "a") as file:
#     file.write("Appending a new line.\n")
# ---------------------------------------------------------------------------- #
# Exception Handling
# try:
#     num1 = int(input("Enter first number: "))
#     num2 = int(input("Enter second number: "))
#     result = num1 / num2
#     print(f"The result is: {result}")
# except ValueError:
#     print("Invalid input. Please enter a valid number.")
# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed.")
# except Exception as e:
#     print(f"An unexpected error occurred: {e}")
# ---------------------------------------------------------------------------- #
# Modules and Packages
# import math
# print(math.sqrt(16))
# print(math.factorial(5))
# print(math.pi)

# import random
# print(random.randint(1, 10))
# print(random.choice(["apple", "banana", "cherry"]))
# ---------------------------------------------------------------------------- #
# JSON Handling
# import json
# data = {"name": "Kyrillos", "age": 30}
# json_str = json.dumps(data)
# parsed = json.loads(json_str)
# print(parsed["name"])
# ---------------------------------------------------------------------------- #
# Date and Time
# import datetime
# now = datetime.datetime.now()
# print(now.strftime("%Y-%m-%d %H:%M:%S"))
# ---------------------------------------------------------------------------- #
# Regular Expressions
# import re
# text = "There are 12 apples and 30 bananas."
# matches = re.findall(r"\d+", text)
# print(matches)
# ---------------------------------------------------------------------------- #
# Command-line Arguments
# import sys
# print("Script name:", sys.argv[0])
# print("Arguments:", sys.argv[1:])
# ---------------------------------------------------------------------------- #
# Threading
# import threading
# import time

# def print_numbers():
#     for i in range(5):
#         print(f"Number: {i}")
#         time.sleep(1)

# def print_letters():
#     for letter in ["A", "B", "C", "D", "E"]:
#         print(f"Letter: {letter}")
#         time.sleep(1)

# thread1 = threading.Thread(target=print_numbers)
# thread2 = threading.Thread(target=print_letters)
# thread1.start()
# thread2.start()
# thread1.join()
# thread2.join()
# ---------------------------------------------------------------------------- #
# OS Commands
# import os
# import platform

# def clear_screen():
#     if platform.system() == "Windows":
#         os.system("cls")
#     else:
#         os.system("clear")

# clear_screen()
# print(f"Operating System: {platform.system()}")
# print(f"Python Version: {platform.python_version()}")
# ---------------------------------------------------------------------------- #
# End of the script
# ---------------------------------------------------------------------------- #
