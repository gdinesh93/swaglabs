from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class Login:
    textbox_username_id="//*[@id='user-name' or @name='user-name']"
    textbox_password_id="password"
    btn_login_id="login-button"
    btn_menu_id="react-burger-menu-btn"
    lnk_logout_id="//*[@id='logout_sidebar_link']"

    def __init__(self,driver):
        self.driver=driver

    def setusername(self,username):
        self.driver.find_element(By.XPATH,self.textbox_username_id).clear()

        self.driver.find_element(By.XPATH,self.textbox_username_id).send_keys(username)

    def setpassword(self, password):
        self.driver.find_element(By.ID,self.textbox_password_id).clear()

        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def login(self):
        self.driver.find_element(By.ID,self.btn_login_id).click()

    def logout(self):
        self.driver.find_element(By.ID,self.btn_menu_id).click()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH,self.lnk_logout_id).click()



