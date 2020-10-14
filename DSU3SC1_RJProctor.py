'''
Lambda School

Data Science
Unit 3 
Sprint Challenge

Rebecca Jeannine Proctor
files included as part of assignment:
DS_unit3_sprint1_challenge.md

DSU3SC1_RJProctor.py
DSU3SC1_part2_RJProctor.py
DSU3SC1_TEST_RJProctor.py

'''

import unittest
import random


# Part 1

'''
build a product class
'''

# create product class
class Product:
  # instantiate class attributes
  '''
  age is an integer value
  weight is an integer value
  flammibility is a float value
  identifier is a unique interger value randomly selected value between 1000000 to 9999999
  '''
  def __init__(self, identifier, name, price=10, weight=20, flammibility=0.5):
    self.identifier = random.randint(1000000, 9999999)
    self.name = str(name)
    self.price = int(price)
    self.weight = int(weight)
    self.flammibility = float(flammibility)

# Part 2

  # create method 1
  '''
  calculates the price divided by the weight
  returns a user message based on the results of the calculation
  '''
  def stealablity(self):
    print('Hello! Please enter the following information: ')
    n = input('What is your product name? ')
    p = input('What is your product price? ')
    w = input('What is your product weight? ')

    user_product = Product(name=n, price=p, weight=w)

    ratio = price / weight

    if ratio > 0.5:
        return f'Thank you. {user_name.name} is Not so stealable. '

        if ratio >= 0.5 and ratio < 1:
            return f'Thank you. {user_name.name} is Kinda stealable. '

        else: 
            return f'Thank you. {user_name.name} Very stealable. '

# create method 2
  '''
  calculates the flammability times the weight
  returns a user message based on the results of the calculation
  '''
  def explode(self):
    print('Hello! Please enter the following information: ')
    n = input('What is your product name? ')
    f = input('What is your product flammibility? ')
    w = input('What is your product weight? ')

    user_product = Product(name=n, flammibility=p, weight=w)

    ratio_2 = flammibility * weight

    if ratio_2 > 10:
        return f'Thank you. {user_name.name} will ...fizzle! '

        if ratio_2 <= 10 and ratio_2 > 50:
            return f'Thank you. {user_name.name} will ...go Boom! '

        else: 
            return f'Thank you. {user_name.name} will ...go BaBoom! '

# Part 3

# inheritance class
class BoxingGlove(Product):
  '''
  creates child BoxingGlove class that inherits from parent Product class
  assigns additional attributes characteristic of BoxingGlove class
  
  '''
  # instantiate BoxingGlove class
  def __init__(self, identifier, name, price=10, weight=10, flammibility=0.5):
    super().__init__(identifier, name, price, weight, flammibility)

    # Note: parent methods 1-2 are available to the child class and do NOT have 
    # to be re-created to be used as-is


  # create method 3 
  # replaces explode method for BoxingGloves subclass only
  '''
  calculates the flammability times the weight
  returns a user message based on the results of the calculation
  '''
  def explode(self):
    print('Hello! Please enter the following information: ')
    n = input('What is your Boxing Gloves product name? ')
    f = input('What is your product flammibility? ')
    w = input('What is your product weight? ')

    user_product_2 = BoxingGlove(name=n, flammibility=p, weight=w)

    if user_product_2 == BoxingGlove(name=n, flammibility=p, weight=w):
        return f"Well, it's a pair of {user_name_2.name} ... "

  
  # create method 4
  # method for subclass BoxingGloves only
  '''
  calculates the flammability times the weight
  returns a user message based on the results of the calculation
  '''
  def punch(self):
    print('Hello! Please enter the following information: ')
    n = input('What is your product name? ')
    w = input('What is your product weight? ')

    user_product_3 = Product(name=n, weight=w)

    ratio_3 = flammibility * weight

    if ratio_3 > 5:
        return f'That tickles! '

        if ratio_3 <= 5 and ratio_3 > 15:
            return f'Hey, that hurt! '

        else: 
            return f'OUCH! '







  





    



