#!/usr/bin/python
import unittest
import TDD
import random
class Test(unittest.TestCase):

    def test_test(self):
        self.assertTrue(True)
    def test_f1_arg0(self):
        w=TDD.f1(0)
        self.assertEqual(w,0)
    def test_f1_arg1(self):
        w=TDD.f1(1)
        self.assertEqual(w,1)
    def test_f1_arg2(self):
        w=TDD.f1(2)
        self.assertEqual(w,4)
    def test_f1_arg21(self):
        w=TDD.f1(2,1)
        self.assertEqual(w,5)
    def test_f1_arg23(self):
        w=TDD.f1(2,3)
        self.assertEqual(w,7)
    def test_f2_string1(self):
        w=TDD.f2('ala')
        self.assertEqual(w,'a')
    def test_f2_string2(self):
        w=TDD.f2([1,2,3])
        self.assertEqual(w,1)
    def test_f2_string3(self):
        w=TDD.f2([])
        self.assertEqual(w,'BUUUUM')
    def test_f3_dic1(self):
        w=TDD.f3(1)
        self.assertEqual(w,'jeden')
    def test_f3_dic2(self):
        w=TDD.f3(2)
        self.assertEqual(w,'dwa')
    def test_f3_dic3(self):
        w=TDD.f3(3)
        self.assertEqual(w,'trzy')
    def test_f3_dic4(self):
        w=TDD.f3(random.choice(range(4,1000)))
        self.assertEqual(w,'other')
    def test_f4_1(self):
        w=TDD.f4('ala')
        self.assertEqual(w,'ala ma kota')
    def test_f4_2(self):
        w=TDD.f4('kot')
        self.assertEqual(w,'kot ma kota')
    def test_f4_3(self):
        w=TDD.f4('kot','psa')
        self.assertEqual(w,'kot ma kota i psa')
    def test_f4_4(self):
        w=TDD.f4('kot','mysz')
        self.assertEqual(w,'kot ma kota i mysz')
    def test_f5_1(self):
        w=TDD.f5(0)
        self.assertEqual(w,'[]')



if __name__ == '__main__':
    unittest.main()
