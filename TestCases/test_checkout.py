import pytest
from selenium import webdriver
from PageObjects.Loginpage import Login
from selenium.webdriver.chrome.service import Service
from Utilities.readproperties import Readconfig
from Utilities.customlogger import Loggen
from PageObjects.CheckoutPage import Checkout
import time


class Test_002:
    baseurl=Readconfig.getapplicationurl()
    username=Readconfig.getusername()
    password=Readconfig.getpassword()
    itemname=Readconfig.getitemname()
    fname=Readconfig.getfname()
    lname=Readconfig.getlname()
    pcode=Readconfig.getpcode()
    logger=Loggen.log()

    def test_homepagetitle(self,setup):
        self.logger.info("+++++++++++++++Test_HomePageTitle+++++++++++++++++")
        self.logger.info("+++++++++++++++verifyinghomepage+++++++++++++++++")

        self.driver = setup
        self.driver.get(self.baseurl)
        act_title=self.driver.title
        if act_title=="Swag Labs":
            assert True
            self.driver.close()
            self.logger.info("+++++++++++++++Test_HomePageTitle is passed+++++++++++++++++")

        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"homepagetitle.png")
            assert False
            self.driver.close()
            self.logger.error("+++++++++++++++Test_HomePageTitle is failed+++++++++++++++++")


    def test_checkout(self,setup):
        self.logger.info("+++++++++++++++test checkout started+++++++++++++++++")

        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp=Login(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.login()
        self.ct=Checkout(self.driver)
        self.ct.selectitem()
        self.ct.addtocard()
        time.sleep(3)
        self.ct.checkout()
        self.ct.enterdetails(fname=self.fname, lname=self.lname,pcode=self.pcode)
        time.sleep(3)
        self.ct.finish()

        url_of_placing_order=self.driver.current_url
        if url_of_placing_order=='https://www.saucedemo.com/checkout-complete.html':
            assert True
            self.driver.close()
            self.logger.info("+++++++++++++++Test_checkout is passed+++++++++++++++++")

        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_checkout.png")
            assert False
            self.driver.close()
            self.logger.error("+++++++++++++++Test checkout is failed+++++++++++++++++")
