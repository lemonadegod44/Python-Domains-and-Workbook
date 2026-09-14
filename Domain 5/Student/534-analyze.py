import unittest

class TestMain(unittest.TestCase):
    
    def test_values(self):
        a = 'vilnius'
        b = ['vilnius','riga','tallinn']
        self.assertIn(a,b)

if __name__ == '__main__':
    unittest.main()  