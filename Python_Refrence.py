#!/usr/bin/env python3
#!/usr/bin/env python3  # Tells Linux to run this script using Python 3 interpreter

# ---------------------------------------------------------------------------- #
# لو هنعمل سكريبت python يشتغل على لينكس لازم نضيف السطر ده فى الاول
# #!/usr/bin/env python3  # Shebang line for Linux compatibility
# زيه زى ال bash script #!/bin/bash  # Equivalent shebang for Bash scripts
# ---------------------------------------------------------------------------- #

# print Function
print("Hello, World!")  # Prints "Hello, World!" to the console
# ---------------------------------------------------------------------------- #
# Variables
name = "Kyrillos"  # Assigns the string "Kyrillos" to the variable 'name'
age = 30  # Assigns the integer 30 to the variable 'age'
print(f"my name is {name} and I am {age} years old.")  # Prints a formatted string using variables

x = 10  # Assigns 10 to variable 'x'
y = 5  # Assigns 5 to variable 'y'
print(x + y)  # Addition: prints the result of x + y
# ---------------------------------------------------------------------------- #
# Data Types
name = "Kyrillos"  # String data type
age = 30  # Integer data type
height = 5.9  # Float data type
is_student = True  # Boolean data type

print(type(name))  # Prints the type of 'name' → str
print(type(age))  # Prints the type of 'age' → int
print(type(height))  # Prints the type of 'height' → float
print(type(is_student))  # Prints the type of 'is_student' → bool
# ---------------------------------------------------------------------------- #
# Type Conversion
age = "30"  # Assigns string "30" to 'age'
print(type(age))  # Prints type → str
age = int(age)  # Converts 'age' to integer
print(type(age))  # Prints type → int
# ---------------------------------------------------------------------------- #
# User Input
name = input("Enter your name: ")  # Prompts user to enter their name
age = input("Enter your age: ")  # Prompts user to enter their age
print(f"Hello, {name}. You are {age} years old.")  # Prints greeting with input
# ---------------------------------------------------------------------------- #
# Conditional Statements
age = int(input("Enter your age: "))  # Gets age as integer
if age < 18:  # Checks if age is less than 18
    print("You're a minor")  # Message for minors
elif age == 18:  # Checks if age is exactly 18
    print("Just became an adult")  # Message for transition
else:  # If age is greater than 18
    print("You're an adult")  # Message for adults
# ---------------------------------------------------------------------------- #
# Loops
# for loop
for index in range(10):  # Loops from 0 to 9
    print(index)  # Prints each index

# while loop
count = 0  # Initializes counter
while count < 5:  # Loops while count is less than 5
    print(count)  # Prints current count
    count += 1  # Increments count
# ---------------------------------------------------------------------------- #
# Functions
def greet(name):  # Defines a function that takes a name
    print(f"Hello, {name}!")  # Prints greeting

greet("Kyrillos")  # Calls the function with "Kyrillos"
# ---------------------------------------------------------------------------- #
# Lists
fruits = ["apple", "banana", "cherry"]  # Creates a list of fruits
print(fruits[0])  # Accesses the first element
fruits.append("orange")  # Adds "orange" to the list
print(fruits)  # Prints the updated list
fruits.remove("banana")  # Removes "banana" from the list
print(fruits)  # Prints the list after removal
print(len(fruits))  # Prints the number of items in the list
# ---------------------------------------------------------------------------- #
# Tuples
my_tuple = (1, 2, 3)  # Creates a tuple
print(my_tuple[0])  # Accesses the first element
# ---------------------------------------------------------------------------- #
# Sets
my_set = {1, 2, 3}  # Creates a set
my_set.add(4)  # Adds 4 to the set
my_set.remove(2)  # Removes 2 from the set
print(my_set)  # Prints the updated set
# ---------------------------------------------------------------------------- #
# Dictionaries
person = {"name": "Kyrillos", "age": 30, "city": "Cairo"}  # Creates a dictionary
print(person["name"])  # Accesses the value of 'name'
person["age"] = 31  # Updates the age
person["job"] = "Engineer"  # Adds a new key-value pair
del person["city"]  # Deletes the 'city' key
print(person)  # Prints the updated dictionary
print(len(person))  # Prints the number of key-value pairs
# ---------------------------------------------------------------------------- #
# List Comprehension
squares = [x * x for x in range(10)]  # Creates a list of squares
print(squares)  # Prints the list
# ---------------------------------------------------------------------------- #
# Lambda Functions
square = lambda x: x * x  # Defines a lambda function to square a number
print(square(5))  # Calls the lambda function with 5
# ---------------------------------------------------------------------------- #
# Classes and Objects
class Person:  # Defines a class named Person
    def __init__(self):  # Constructor method
        self.name = "Kyrillos"  # Sets name attribute
        self.age = 30  # Sets age attribute

    def greet(self):  # Method to greet
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")  # Prints greeting

person1 = Person()  # Creates an object of Person
person1.greet()  # Calls the greet method
# ---------------------------------------------------------------------------- #
# Inheritance
class Animal:  # Base class
    def speak(self):  # Method in base class
        print("Animal speaks")  # Prints message

class Dog(Animal):  # Derived class
    def speak(self):  # Overrides speak method
        print("Dog barks")  # Prints dog-specific message

animal = Animal()  # Creates Animal object
dog = Dog()  # Creates Dog object
animal.speak()  # Calls Animal's speak
dog.speak()  # Calls Dog's speak
# ---------------------------------------------------------------------------- #
# Decorators
def my_decorator(func):  # Defines a decorator
    def wrapper():  # Inner function
        print("Before")  # Runs before original function
        func()  # Calls original function
        print("After")  # Runs after original function
    return wrapper  # Returns the wrapper

@my_decorator  # Applies the decorator
def say_hello():  # Defines a function
    print("Hello!")  # Prints greeting

say_hello()  # Calls the decorated function
# ---------------------------------------------------------------------------- #
# Context Manager
class MyFile:  # Custom context manager class
    def __enter__(self):  # Called when entering 'with' block
        print("Opening file")  # Prints message
        return self  # Returns the object

    def __exit__(self, exc_type, exc_value, traceback):  # Called when exiting
        print("Closing file")  # Prints message

with MyFile():  # Uses the context manager
    print("Inside context")  # Prints message inside block
# ---------------------------------------------------------------------------- #
# File Handling
with open("example.txt", "w") as file:  # Opens file for writing
    file.write("Hello, World!\n")  # Writes a line

with open("example.txt", "r") as file:  # Opens file for reading
    content = file.read()  # Reads content
    print(content)  # Prints content

with open("example.txt", "a") as file:  # Opens file for appending
    file.write("Appending a new line.\n")  # Adds a line
# ---------------------------------------------------------------------------- #
# Exception Handling
try:  # Start of try block
    num1 = int(input("Enter first number: "))  # Gets first number
    num2 = int(input("Enter second number: "))  # Gets second number
    result = num1 / num2  # Performs division
    print(f"The result is: {result}")  # Prints result
except ValueError:  # Handles invalid input
    print("Invalid input. Please enter a valid number.")  # Error message
except ZeroDivisionError:  # Handles division by zero
    print("Error: Division by zero is not allowed.")  # Error message
except Exception as e:  # Handles other errors
    print(f"An unexpected error occurred: {e}")  # Prints error
# ---------------------------------------------------------------------------- #
# Modules and Packages
import math  # Imports math module
print(math.sqrt(16))  # Prints square root of 16
print(math.factorial(5))  # Prints factorial of 5
print(math.pi)  # Prints value of pi

import random  # Imports random module
print(random.randint(1, 10))  # Prints random integer between 1 and 10
print(random.choice(["apple", "banana", "cherry"]))  # Prints random item from list
# ---------------------------------------------------------------------------- #
# JSON Handling
import json  # Imports the JSON module to work with JSON data

data = {"name": "Kyrillos", "age": 30}  # Creates a dictionary with name and age
json_str = json.dumps(data)  # Converts the dictionary to a JSON-formatted string
parsed = json.loads(json_str)  # Parses the JSON string back into a dictionary
print(parsed["name"])  # Prints the value associated with the key "name"

# ---------------------------------------------------------------------------- #
# Date and Time
import datetime  # Imports the datetime module to work with dates and times

now = datetime.datetime.now()  # Gets the current date and time
print(now.strftime("%Y-%m-%d %H:%M:%S"))  # Formats and prints the date/time as a string

# ---------------------------------------------------------------------------- #
# Regular Expressions
import re  # Imports the regular expressions module

text = "There are 12 apples and 30 bananas."  # Sample text containing numbers
matches = re.findall(r"\d+", text)  # Finds all digit sequences in the text
print(matches)  # Prints the list of matched numbers (e.g., ['12', '30'])

# ---------------------------------------------------------------------------- #
# Command-line Arguments
import sys  # Imports the sys module to access command-line arguments

print("Script name:", sys.argv[0])  # Prints the name of the script file
print("Arguments:", sys.argv[1:])  # Prints the list of arguments passed to the script

# ---------------------------------------------------------------------------- #
# Threading
import threading  # Imports the threading module to run tasks in parallel
import time  # Imports the time module to add delays

def print_numbers():  # Defines a function to print numbers
    for i in range(5):  # Loops from 0 to 4
        print(f"Number: {i}")  # Prints the current number
        time.sleep(1)  # Pauses for 1 second

def print_letters():  # Defines a function to print letters
    for letter in ["A", "B", "C", "D", "E"]:  # Loops through a list of letters
        print(f"Letter: {letter}")  # Prints the current letter
        time.sleep(1)  # Pauses for 1 second

thread1 = threading.Thread(target=print_numbers)  # Creates a thread to run print_numbers
thread2 = threading.Thread(target=print_letters)  # Creates a thread to run print_letters

thread1.start()  # Starts the first thread
thread2.start()  # Starts the second thread

thread1.join()  # Waits for thread1 to finish
thread2.join()  # Waits for thread2 to finish

# ---------------------------------------------------------------------------- #
# OS Commands
import os  # Imports the OS module to interact with the operating system
import platform  # Imports the platform module to detect the OS type

def clear_screen():  # Defines a function to clear the terminal screen
    if platform.system() == "Windows":  # Checks if the OS is Windows
        os.system("cls")  # Clears the screen using Windows command
    else:  # If the OS is not Windows (Linux/macOS)
        os.system("clear")  # Clears the screen using Unix command

clear_screen()  # Calls the function to clear the screen
print(f"Operating System: {platform.system()}")  # Prints the name of the operating system
print(f"Python Version: {platform.python_version()}")  # Prints the current Python version

# ---------------------------------------------------------------------------- #
# End of the script
# ---------------------------------------------------------------------------- #

