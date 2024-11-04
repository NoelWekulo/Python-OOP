class Car:
    def __init__(self, make, model, year):
        self.make = make  # Attribute
        self.model = model
        self.year = year

    def start_engine(self):  # Method
        print(f"The {self.make} {self.model}'s engine has started.")

my_car = Car("Toyota", "Corolla", 2020)
my_car.start_engine()

# Exercise 1: Define a Book Class
# Create a class named Book with the following requirements:
#
# Attributes:
# title (string)
# author (string)
# year (integer)
# Method:
# description: This should print "Title by Author, published in Year".

class Book:
    def __init__(self,title,author,year):
        self.title = title
        self.author = author
        self.year = year
    def display_info(self):
        print(f"{self.title} by {self.author},published in {self.year}.")

my_book = Book("Chains can be unchained","Prophet Steve Omondi",2024)
my_book.display_info()

# Exercise 2: Define a Student Class with Class and Instance Attributes
# Create a class Student with the following:
#
# Class Attribute:
# school_name (e.g., "Greenwood High") which is shared by all students.
# Instance Attributes:
# name (string)
# grade (integer)
# Method:
# introduce: Print "Hi, I am Name from Grade at School_name."

class Student:
    def __init__(self,name:str,grade:int,school_name="Loreto High School"):
        self.name=name
        self.grade=grade
        self.school_name=school_name
    def introduce(self):
        print(f"Hi,Iam {self.name} from grade {self.grade} at {self.school_name}")
my_student=Student("Noel Wekulo",7)
my_student.introduce()

# Exercise 3: Define a BankAccount Class
# Create a BankAccount class with:
#
# Attributes:
# account_holder (string)
# balance (float, default is 0.0)
# Methods:
# deposit: Add a specified amount to the balance.
# withdraw: Deduct a specified amount from the balance, only if sufficient funds are available.
# display_balance: Print "Account Holder: account_holder, Balance: balance".

class BankAccount:
    def __init__(self, account_holder, balance=0.0):
        self.account_holder = account_holder  # Name of the account holder
        self.balance = balance  # Initial balance, default is 0.0

    def deposit(self, amount):
        """Adds the specified amount to the account balance."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance is ${self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Deducts the specified amount from the balance if enough funds are available."""
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew ${amount}. New balance is ${self.balance}.")
            else:
                print("Insufficient funds for this withdrawal.")
        else:
            print("Withdrawal amount must be positive.")

    def display_balance(self):
        """Displays the account holder and the current balance."""
        print(f"Account Holder: {self.account_holder}, Balance: ${self.balance}")


# Example Usage
account = BankAccount("John Doe")
account.deposit(500)       # Deposits $500 into the account
account.withdraw(200)      # Withdraws $200 from the account
account.display_balance()   # Displays the account balance

# Exercise 1: Circle Class
# Create a class named Circle with the following requirements:
#
# Attributes:
# radius (float)
# Methods:
# area: Returns the area of the circle using the formula
# 𝜋
# ×
# radius
# 2
# π×radius
# 2
#  .
# circumference: Returns the circumference using
# 2
# ×
# 𝜋
# ×
# radius
# 2×π×radius.

import math
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return math.pi*self.radius*self.radius
    def circum(self):
        return 2*math.pi*self.radius
circle1=Circle(21)
print(f"the area is:{circle1.area():.2f}")
print(f"the circumference is:{circle1.circum():.2f}")


