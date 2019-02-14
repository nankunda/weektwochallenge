import unittest
from vowels.countvowels import vowelcount
class testcountingvowels(unittest.TestCase):
def countvowels_test(self):
    self.assertTupleEqual(vowelcount('hi anita'), ('ai',4))
    def testinputstring(self):
        with self.assertRaises(Type error):
            vowelcount([1,2,3,4])