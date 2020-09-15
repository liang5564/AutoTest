#coding=utf-8
import unittest

class FirstCase02(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('所有case执行之前的前置')

    @classmethod
    def tearDownClass(cls):
        print('所有case执行之后的后置')

    def setUp(self):
        print('这是case的前置条件')

    def tearDown(self):
        print('这是case的后置条件')

    @unittest.skip('不执行第1条case')
    def test_first001(self):
        print('这是第001条case')

    def test_first002(self):
        print('这是第002条case')

    def test_first003(self):
        print('这是第003条case')

if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(FirstCase02('test_first002'))
    suite.addTest(FirstCase02('test_first001'))
    suite.addTest(FirstCase02('test_first003'))
    unittest.TextTestRunner().run(suite)