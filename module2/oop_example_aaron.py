'''
live example of creating a class
Aaron G
'''

import pandas as pd


class MyDataFrame(pd.DataFrame):
    '''
    returns the number of cells in a dataframe
    '''
    def num_cells(self):
        return self.shape[0] * self.shape[1]

# test in command line
# data = [[2,3][-7,2]]
# df = pd.DataFrame(data)
# df
# type(df)
# my_df = MyDataFrame(data)
# my_df.shape
# my_df.num_cells()


class BasicClass:
    pass

# test in command line
#   my_object = BasicClass()


class AnotherClass:
    pass


class Complex:
# complex numbers
    # constuctor
    # method
    def __init__(self, real_part, imaginary_part):
        # fields of self
        self.r = real_part
        self.i = real_imaginary

# instantiate a number in the repl to test
# x = Complex(3,2)

    # method
    '''
    add complex numbers
    '''
    def add(self, other_complex):
        self.r += other_complex.r
        self.i += other_complex.i

# to test in command line
# Complex(3,2)
# x.add(y) 

    # method
    '''
    define how python will represent/print 
    your object when you look at it on an repl
    --as string--
    '''
    def __repr__(self):
        return '({}, {})'.format(self.r, self.i)


class SocialMediaUser:
    def __init__(self, name):
        self.name = name
        self.upvotes = 0

    def receive_upvote(self):
        self.upvotes += 1

    def is_popular(self):
         return self.upvotes > 100

# test in command line
# bob.name
# jane.name
# bob.upvotes
# jane.upvotes
# bob.receives_upvotes()
# jane.upvotes
# bob.is_popular()
# for i in range(1000):
#    jane.receive_upvote()
# jane.is_popular()
# jane.upvotes


class Animal:
    '''
    general representation of animals

    weight is an integer value
    '''
    def __init___(self, name, weight, diet):
        self.name = str(name)
        self.weight = int(weight)
        self.diet = str(diet)

    def run(self):
        return 'Vroom!'

    def eat(self, food):
        return f'{food} is delicious, yum!'

# test in command line
# joe_the_gazelle = Animal('Joe', 120, 'veggies')
# joe_the_gazelle.name
# joe_the_gazelle.diet
# joe_the_gazelle.weight
# joe_the_gazelle.run
# joe_the_gazelle.eat('kale')


class Tiger(Animal):
    '''
    represents tigers as a subclass of animals
    '''
    def __init___(self, name, weight, diet, num_stripes):
        super().__init___(self, name, weight, diet)
        self.num_stripes = num_stripes

# test in command line
# tony_the_tiger = Tiger('Tony', 140, 'ceral')
# tony_the_tiger.run
# tony_the_tiger.name
# tony_the_tiger.eat('cereal')

# Note: joe_the_gazelle returns as an Animal object
# and tony_the_tiger returns as a Tiger object
    
    def say_great(self):
        return "It's GREEAAAAT!"
        
    def run(self):
        return 'Scamperwhoosh!'

# test in command line
# tony = Tiger('Tony', 140, 'ceral', 37)
# tony.name
# tony.weight
# tony.run
# tony.diet
# tony.num_stripes
# tony.run()
# tony.say_great()

# Code Style and Review
# PEP 8 allows for collaboration by having a consistant
    # standard style 

# agreement about how to format code

# Code review
# can you follow low or layout?
# can you understand logic/reasoning for what it is doing?
# could you build with (import and use) or extend it 
#    (as a developer adding more to the codebase)?
# comments should focus on style, design, construction
#   and GitHub functionality for stretch goal 
# (exemplar-) sklearn/n/cluster/tests/test_hierachical.py (merged code review)





    



