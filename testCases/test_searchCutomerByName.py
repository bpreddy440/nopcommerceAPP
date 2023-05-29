import string
import time

from selenium import webdriver
from pageObjects.Addcustomerpage import AddCustomer
import pytest
from pageObjects.LoginPage import LoginPage
from uilitites.readProperties import ReadConfig
from uilitites.customLogger import LogGen
import random
from pageObjects.SearchCustomersPage import SearchCustomer


class Test_SearchCustomerByName_005:
    baseURL = ReadConfig.getAplicationURL()
    username = ReadConfig.getUserEmial()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_searchCustomerByName(self, setup):
        self.logger.info("**********search customer by name **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("******* login successfull***************")
        self.logger.info("*******starting search by name *************")
# creting search customer object
        searchcust = SearchCustomer(self.driver)
        searchcust.setFirstName("Victoria")
        searchcust.setLastName("Terces")
        searchcust.clickSearch()
        time.sleep(5)
        status = searchcust.searchCustomerByName("Victoria Terces")
        assert  True==status
        self.logger.info("************* search by name test passed*****8888")
        self.driver.close()



