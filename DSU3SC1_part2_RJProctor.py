'''
Lambda School

Data Science
Unit 3 
Sprint Challenge

Rebecca Jeannine Proctor
files included as apart of assingment:
DS_unit3_sprint1_challenge.md

DSU3SC1_RJProctor.py
DSU3SC1_part2_RJProctor.py
DSU3SC1_TEST_RJProctor.py

'''

import unittest
import random
import numpy as np

# Part 4
'''
gererate random products
print summary reports
use Product class
'''
# lists for function - 30 count
adj = ['Awesome', 'Baby', 'Giant', 'Token', 'Peacekeeper']
noun = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', 'Revenge']

# create method 5 
def generate_products(num_products=30):
    a_identifier = random.randint(1000000, 9999999)
    a_name = random.choice(adj) + " " + random.choice(noun)
    a_price = random.randint(16, 120)
    a_weight = random.randint(50, 500)
    a_flammibility = random.uniform(0.0, 1.0)  
        # this metric's scale was not described in the instructions
        # are we using a percent or the national fire scale 
        # if a percent then the limits should be (0.0, 1,0)
        # if we are using the national fire scale we could have used
        # random.randint(0, 4)
    a_report = Product(a_identifier, a_name, a_price, a_weight, a_flammibility)
    products.append(a_animal)
    return products

# instantiate list
products = []
      
    
# create method 6
'''
calculates unique values
'''
def inventory_report(products):
    # plug all items int a set - all items that go into set are unique values
    unique_vals = set()
    for val in len(products):
        unique_vals.add(products[val].name)
        len(unique_vals)

    # average price
    p_list_price = [p.price for p in products]
    avg_price = np.mean(p_list_price)

    # average weight
    p_list_weight = [p.weight for p in products]
    avg_wgh = np.mean(p_list_weight)

    # average flammibility
    p_list_flammibility = [p.price for p in products]
    avg_flam = np.mean(p_list_flammibility)   

    return (len(unique_vals), avg_price, avg_wgh, avg_flam)
    
print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
print('Unique product names: ', len(unique_vals))
print('Average price: ', avg_price)
print('Average weight: ', avg_wgh)
print('Average flammability: ', avg_flam)

# if the name of the file is entered into the terminal, do this operation
if __name__ == '__main__':
    inventory_report(generate_products())
