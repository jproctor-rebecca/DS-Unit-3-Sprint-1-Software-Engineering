'''
unit test
'''


import unittest
from study_guide import Person
from study_guide import Worker


class TestPeople(unittest.TestCase):

    # assertion test - verify instance of age
    # 1-120
    def test_age(self):
        # instantiate person object
        per = Person(age=30)
        # test object
        self.assertTrue(per.age > 0 and per.age < 120)
    
if __name__ == '__main__':
    unittest.main()


    def test_worker(self):
        #instantiate worker object

    


# Verify that an instance of person has an age between 0 and 120 when first instantiated
# Verify the same thing with a worker instance
# Verify the worker greet method uses the personal_title of the person passed to it.
#Write your own unit test