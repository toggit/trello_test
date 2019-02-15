import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
# import sys
# import logging
# import traceback


class PythonTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.addCleanup(self.browser.quit)

    # def testPageTitle1(self):
    #     self.browser.get("https://www.hist.org.il/")
    #     assert "	ביחד בשבילך - מועדון ההטבות החברתי הראשון בישראל" not in self.browser.title
    #
    # def testLogin(self):
    #     self.browser.get("https://www.hist.org.il/")
    #     # enter ID:
    #     elem = self.browser.find_element_by_name("txtHistadrutTz")
    #     elem.clear()
    #     elem.send_keys("000000000")
    #     # enter PASS:
    #     elem = self.browser.find_element_by_name("txtForHistadrutPassword")
    #     elem.clear()
    #     elem.send_keys("000000000")
    #     self.browser.find_element_by_name("Button1").click()
    #     if self.browser.current_url != "https://www.hist.org.il/HomePage.aspx":
    #         self.browser.get("https://www.hist.org.il/HomePage.aspx")
    #     # time.sleep(3)
    #     elem = self.browser.find_element_by_id("ctl00_LabelIDOrName")
    #     self.assertEqual("איוונה", elem.text)

    def testShopping(self):
        #Login
        self.browser.get("https://www.hist.org.il/")
        self.browser.find_element_by_id("txtHistadrutTz").send_keys("000000000")
        self.browser.find_element_by_id("txtForHistadrutPassword").send_keys("000000000")
        self.browser.find_element_by_id("Button1").click()

        self.browser.get("https://www.hist.org.il/business.aspx?catnumber=274")
        time.sleep(2)
        elem = self.browser.find_element_by_id("ctl00_ContentPlaceHolder2_DataListVariants_ctl03_Number")
        elem.clear()
        elem.send_keys("3")
        # time.sleep(3)
        self.browser.find_element_by_id("ctl00_ContentPlaceHolder2_ButtonAddToBasket").click()
        time.sleep(3)
        self.assertEqual("https://www.hist.org.il/ShopingBasket.aspx", self.browser.current_url)


if __name__ == '__main__':

    print("tests running....")
    unittest.main(exit=False, verbosity=2)
    # print(unittest.TestLoader().loadTestsFromTestCase(PythonTestCase).)

    print("tests finish!")

