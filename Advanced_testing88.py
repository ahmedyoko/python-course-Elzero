#...................................................
# Advanced lesson => unit testing with unittest اختبار وحدات من الكود
#...................................................
# Test runner :
#      the module that run the unit testing(unittest,pytest)
#...................................................
# Test case :
#   smallest unit of testing 
#   use assert methods to check for actions and responses 
# Test suite :
#   collection of multiple tests or test cases
# Test report :
#   A full report contain failure or succeed
#...................................................
# unittest : 
#    Add test into classes as methods
#    use a series of special assertion methods
# https://docs.python.org/3/library/unittest.html
#...................................................
# show assertion error:
# assert 3 * 8 == 24 , "Should Be 24"
# assert 3 * 8 == 23 , "Should Be 24" # AssertionError: Should Be 24

def test_case_one() :
    assert 5 * 10 == 50 , "Should Be 50"
def test_case_two() :
    # assert 5 * 50 == 240 , "Should Be 250"
    assert 5 * 50 == 250 , "Should Be 250"

if __name__=="__main__" :
    test_case_one()
    test_case_two()
    print("All cases passed")


import unittest
class MyTestCase(unittest.TestCase):
    def test_one(self):
        self.assertTrue(100 > 97 , "should be True")
    def test_two(self):
        self.assertEqual(40+60,100,"Should Be 100")
    def test_three(self):
        self.assertGreater(100,80,"should be True")

if __name__=="__main__" :
    unittest.main()
