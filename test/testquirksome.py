import unittest
import quirksome

class AddTest(unittest.TestCase):



    def setUp(self):
        '''Verify environment is setup properly'''
        pass

    def test_2zeros(self):
        '''Verify that 2 zeros with 5 is 05'''
        qs = quirksome.QuirkSome()
        self.assertEqual(qs.add_zeros(5,2), "05")

    def test_4zeros(self):
        '''Verify that 2 zeros with 5 is 0005'''
        qs = quirksome.QuirkSome()
        self.assertEqual(qs.add_zeros(5, 4), "0005")

    def test_quirksome_2_digits_81(self):
        '''Verify that 2 digits and 81 is true'''
        qs = quirksome.QuirkSome()
        self.assertTrue(qs.found_square(8,1,"81"))

    def test_quirksome_0_and_1_digits(self):
        '''Verify that 2 digits and 81 is true'''
        qs = quirksome.QuirkSome()
        self.assertEqual(qs.value(0),"")
        self.assertEqual(qs.value(1),"")

    def test_quirksome_minus_digits(self):
        '''Verify that 2 digits and 81 is true'''
        qs = quirksome.QuirkSome()
        self.assertEqual(qs.value(-1), "")
        self.assertEqual(qs.value(-100), "")

if __name__ == '__main__':
    unittest.main()