
import unittest
from utils import *
from cookie_processor import CookieProcessor

class CookieProcessorTest(unittest.TestCase):
    def setUp(self):
        self.CookieProcessor = CookieProcessor()
        filename = "test.csv"
        self.CookieProcessor.read_data(filename)

    def test_max_item(self):
        dict1 = {"a":1, "b":2, "c":3}
        dict2 = {"a":1, "b":3, "c":3}
        dict3 = {"a":1, "b":3, "c":3, "d":1, "e":3}
        self.assertEqual(["c"], self.CookieProcessor.find_max_items(dict1))
        self.assertEqual(["b","c"], self.CookieProcessor.find_max_items(dict2))
        self.assertEqual(["b","c","e"], self.CookieProcessor.find_max_items(dict3))
   

    def test_read_data(self):
        dict_r = {"2018-12-09":{"A":2,"S":1,"5":1},"2018-12-08":{"S":1,"4":1,"f":1},"2018-12-07":{"4":1}}
        self.assertEqual(dict_r,self.CookieProcessor.cookie_dict)

    def test_find_most(self):
        res = ["A"]
        res2 = ["S","4","f"]
        res3 = []
        self.assertEqual(res, self.CookieProcessor.find_most_active_cookie("2018-12-09"))
        self.assertEqual(res2, self.CookieProcessor.find_most_active_cookie("2018-12-08"))
        self.assertEqual(res3, self.CookieProcessor.find_most_active_cookie("2018-12-05"))


class ValidDateTest(unittest.TestCase):

    def test_valid_date(self):

        test_list= ["2018-12-09",
                    "2018-9-9",
                    "20-12-09",
                    "2021-11-25",
                    "2018/12/09",
                    "a-b-c"]
        self.assertEqual(True, valid_date(test_list[0]))
        self.assertEqual(False, valid_date(test_list[1]))
        self.assertEqual(False, valid_date(test_list[2]))
        self.assertEqual(True, valid_date(test_list[3]))
        self.assertEqual(False, valid_date(test_list[4]))
        self.assertEqual(False, valid_date(test_list[5]))



if __name__ == "__main__":
	unittest.main()