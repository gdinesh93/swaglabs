from selenium import webdriver
from selenium.webdriver.common.by import By

class Checkout:
    lnk_backpack_lnktxt="Sauce Labs Backpack"
    btn_addtocart_xpath="//*[@class='btn btn_primary btn_small btn_inventory']"
    btn_shoppingcart_xpath="//*[@id='shopping_cart_container']/a"
    btn_checkout_xpath="//*[@id='checkout']"
    txt_firstname_xpath="//*[@id='first-name']"
    txt_lastname_xpath="//*[@id='last-name']"
    txt_postcode_xpath="//*[@id='postal-code']"
    btn_continue_xpath="//*[@id='continue']"
    btn_finish_xpath="//*[@id='finish']"
    lnk_selectitem_xpath="//*[@id='item_4_title_link']/div"
    #txtcomplete_xpath="//*[@class='complete-text']"

    def __init__(self,driver):
        self.driver=driver

    def selectitem(self):
        self.driver.find_element(By.XPATH,self.lnk_selectitem_xpath).click()

    def addtocard(self):
        self.driver.find_element(By.XPATH,self.btn_addtocart_xpath).click()
    def checkout(self):
        self.driver.find_element(By.XPATH,self.btn_shoppingcart_xpath).click()
        self.driver.find_element(By.XPATH,self.btn_checkout_xpath).click()
    def enterdetails(self,fname,lname,pcode):
        self.driver.find_element(By.XPATH,self.txt_firstname_xpath).send_keys(fname)
        self.driver.find_element(By.XPATH,self.txt_lastname_xpath).send_keys(lname)
        self.driver.find_element(By.XPATH,self.txt_postcode_xpath).send_keys(pcode)
    def finish(self):
        self.driver.find_element(By.XPATH,self.btn_continue_xpath).click()
        self.driver.find_element(By.XPATH,self.btn_finish_xpath).click()



