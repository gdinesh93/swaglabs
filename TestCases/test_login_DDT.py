import pytest
from selenium import webdriver
from PageObjects.Loginpage import Login
from selenium.webdriver.chrome.service import Service
from Utilities.readproperties import Readconfig
from Utilities.customlogger import Loggen
from Utilities import XLutils
import time
class Test_002_DDT_Login:
    baseurl=Readconfig.getapplicationurl()
    path=".//TestData/SwagLabsCredentials.xlsx"
    logger=Loggen.log()

    def test_login_ddt(self,setup):
        self.logger.info("+++++++++++++++Test_002_DDT_Login+++++++++++++++++")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp=Login(self.driver)
        self.rows=XLutils.getrowcount(self.path,'Sheet1')
        lst_status=[]
        for r in range(2,self.rows+1):
            self.username=XLutils.readdata(self.path,'Sheet1',r,1)
            self.password=XLutils.readdata(self.path,'Sheet1',r,2)
            self.exp=XLutils.readdata(self.path,'Sheet1',r,3)
            self.lp.setusername(self.username)
            self.lp.setpassword(self.password)
            self.lp.login()
            act_urlafterlogin=self.driver.current_url
            if act_urlafterlogin=='https://www.saucedemo.com/inventory.html':
                if self.exp=="Pass":
                    self.logger.info("+++++++++++++++Test_login is passed+++++++++++++++++")
                    time.sleep(5)
                    self.lp.logout()
                    lst_status.append("Pass")
                elif self.exp=="Fail":
                    self.logger.error("+++++++++Test is failed+++++++++")
                    self.lp.logout()
                    lst_status.append("Fail")
            elif act_urlafterlogin != 'https://www.saucedemo.com/inventory.html':
                if self.exp == "Pass":
                    self.logger.error("+++++++++++++++Test_login is Failed+++++++++++++++++")
                    self.lp.logout()
                    lst_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("+++++++++Test is Passed+++++++++")
                    lst_status.append("Pass")
        if "Fail" not in lst_status:
            assert True
            self.logger.info("++++++++++Entire Test Is Passed++++++++")
            self.driver.close()
        else:
            assert False
            self.logger.info("++++++Entire Test is Failed+++++++")
            self.driver.close()