import pytest
from selenium import webdriver
from PageObjects.Loginpage import Login
from selenium.webdriver.chrome.service import Service
from Utilities.readproperties import Readconfig
from Utilities.customlogger import Loggen


class Test_001:
    baseurl=Readconfig.getapplicationurl()
    username=Readconfig.getusername()
    password=Readconfig.getpassword()
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


    def test_login(self,setup):
        self.logger.info("+++++++++++++++test login started+++++++++++++++++")

        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp=Login(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.login()
        act_urlafterlogin=self.driver.current_url
        if act_urlafterlogin=='https://www.saucedemo.com/inventory.html':
            assert True
            self.driver.close()
            self.logger.info("+++++++++++++++Test_login is passed+++++++++++++++++")

        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
            assert False
            self.driver.close()
            self.logger.error("+++++++++++++++Test login is failed+++++++++++++++++")
