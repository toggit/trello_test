import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# import time
# import sys
# import logging
# import traceback


class PythonTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.addCleanup(self.browser.quit)

    def testPageTitle1(self):
        self.browser.get("http://www.python.org")
        assert "Welcome2" not in self.browser.title

    def testPageTitle2(self):
        self.browser.get("http://www.python.org")
        assert "Welcome" in self.browser.title

    def testPageSearch(self):
        self.browser.get("http://www.python.org")
        elem = self.browser.find_element_by_name("q")
        elem.clear()
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in self.browser.page_source


if __name__ == '__main__':

    print("tests running....")
    unittest.main(exit=False,verbosity=2)
    # print(unittest.TestLoader().loadTestsFromTestCase(PythonTestCase).)

    print("tests finish!")

