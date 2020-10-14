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

# Part 5

'''
assert and unittest
'''

import unittest
from DSU3SC1_RJProctor import Product
from DSU3SC1_part2_RJProctor import generate_products, adj, nouns


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    # assertion test - verify instance of flammibility
    # 0.0-1.0
    def test_flammibility(self):
        # instantiate default test flammibility object
        flamm = Product(flammibility=0.5)
        # test object
        self.assertEqual(flamm.flammibility, 0.5)

    # assertion test - verify method of explode
    # user print statements
    def test_explode(self):
        # instantiate default test explode method
        expl = Product(name, flammibility, weight)
        # test object
        self.assertEqual(expl, 'Thank you. {user_name.name} will ...go BaBoom! ')

        

class AcmeReportTests:
    def test_default_num_products():
        '''
        checks for list of 30 products
        '''
        # instantiate default test object
        prods = Products(name)
        prod_len = len(prods)

        # test object
        self.assertEqual(prod_len, 30)


    def test_legal_names():
        '''
        checks for composition
        1 adjective, 1 noun
        '''
        # instantiate default test object
        ln = Product(name)

        # test object
        self.assertIn(ln.name, adj)
        self.assertIn(ln.name, noun)
        

# if the name of the file is entered into the terminal, do this operation
if __name__ == '__main__':
    unittest.main()


# Part 6 PEP8 Review
# coded in VSC, in compliance


# Part 7

'''
  What, in your opinion, is an important part of code reviews? That is, what is
  something you pay attention to when you review code, and that you appreciate
  when others do the same for your code?
'''
# I look for consistency. Look at every line of code that you have been assigned to review. 
# Some things like data files, generated code, or large data structures you can scan over 
# sometimes, but don't scan over a human-written class, function, or block of code and assume 
# that what's inside of it is okay. Look for key things, such as… Structure. You can do 
# automated checks (e.g., static analysis) for some of the things — e.g., structure and 
# logic. But others — e.g., design and functionality — require a human reviewer to evaluate.
# I think formatting style and documentation for readibility, collaboration and reproduction
# are very important.

'''
  We have an awful lot of computers here, and it gets pretty confusing with
  slightly different things running on all of them. How could containers help us
  improve this situation?
'''

# Containers are any object that holds an arbitrary number of other objects. 
# Generally, containers provide a way to access the contained objects and to 
# iterate over them. Examples of containers include tuple , list , set , dict;
# these are the built-in containers. Using containers would allow you to create 
# objects once, access and maintain them from any physical space.