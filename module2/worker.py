'''
worker class
'''

# inheritance class
class Worker(Person):
  '''
  creates child Worker class that inherits from parent Person class
  assigns additional attributes characteristic of Worker class
  income is an integer value
  '''
  # instantiate Worker class
  def __init__(self, name='Doe', age=0, height=0, weight=0, company='xyz', job_title='xyz', personal_title='xyz', income=0, training=False):
    super().__init__(name, age, height, weight)
    self.company = company
    self.job_title = job_title
    self.personal_title = personal_title
    self.income = int(income)
    self.training = training

  # Note: parent methods 1-3 are available to the child class and do NOT have 
  # to be re-created to be used as-is

  # create method 4 
  # replaces greets method for Worker class only
  '''
  returns user greeting with user title and user name
  '''
  def greets(self):
    print('Hello! Please enter the following information: ')
    n = input('What is your name? ')
    pt = input('What is your personal title? Dr., Mr., Mrs., Ms., or Miss ')
    user_name_2 = Worker( name=str(n), personal_title=str(pt))

    return f'Hello, {user_name_2.personal_title} {user_name_2.name}! My name is {self.personal_title} {self.name}. I work for {self.company}. '

  

#import numpy as np
import random 

# lists for function
name = ['Rebecca', 'Jeannine', 'Taylor']
company =['Lambda', 'Google', 'GitHub', 'Exxon' ]
personal_title = ['Dr.', 'Mr.', 'Mrs.', 'Ms.', 'Miss']
job_title = ['Engineer', 'Analyst', 'Consultant']
training = ['True', 'False']

# instantiate 10 Workers
def bunch_of_workers():
  a_name = random.choice(name)
  a_age = random.randint(16, 120)
  a_height = random.randint(5, 501)
  a_weight = random.randint(50, 500)
  a_company = random.choice(company)
  a_job_title = random.choice(job_title)
  a_personal_title = random.choice(personal_title)
  a_income = random.randint(0, 1000000000)
  a_training = random.choice(training)
  a_worker = Worker(a_name, a_age, a_height, a_weight, a_company, a_job_title, a_personal_title, a_income, a_training)
  # worker.append(a_worker)
  return a_worker

  