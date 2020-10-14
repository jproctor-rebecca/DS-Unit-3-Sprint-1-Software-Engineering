'''
person class
'''
'''
build a person class
'''

# create person class
class Person:
  # instantiate class attributes
  '''
  age is an integer value
  height is an integer value
  weight is an integer value
  '''
  def __init__(self, name='Doe', age=0, height=0, weight=0):
    self.name = name
    self.age = int(age)
    self.height = int(height)
    self.weight = int(weight)

  # create method 1
  '''
  returns user greeting with user name
  '''
  def greets(self):
    print('Hello! Please enter the following information: ')
    n = input('What is your name? ')

    user_name = Person(name=n)

    return f'Hello, {user_name.name}! My name is {self.name}, nice to meet you. '

  # create method 2
  '''
  increments age by one year
  '''
  def had_birthday(self, age):
    self.age = age + 1
    return age

  # create method 3
  '''
  returns user positive message with user weight info
  '''
  def pos_weight_message(self):
    n = input('What is your name? ')
    w = input('What is your weight? ')
    user_name = Person(name=n, weight=w)

    return f'Hello, {user_name.name}! Congratualtions on only weighing {user_name.weight} lbs. '
