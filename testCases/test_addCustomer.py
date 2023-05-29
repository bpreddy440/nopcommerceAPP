import string
from selenium import webdriver
from pageObjects.Addcustomerpage import AddCustomer
import pytest
from pageObjects.LoginPage import LoginPage
from uilitites.readProperties import ReadConfig
from uilitites.customLogger import LogGen
import random


class Test_003_AddCustomer:
    baseURL = ReadConfig.getAplicationURL()
    username = ReadConfig.getUserEmial()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addCustomer(self, setup):
        self.logger.info("**********test 003 add customer**********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("***** login successfull **********")
        self.logger.info("***** starting add customer test **********")
        # creating object for addCustomer class
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomerMenuItem()
        self.addcust.clickOnAddNew()

        self.logger.info("********* providing user info******************")

        self.email = random_generator() + "@gmail.com"
        print(self.email)
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setFirstName("Paddu")
        self.addcust.setLastName("Reddy")
        self.addcust.setGender("Male")
        self.addcust.setDob("7/05/1985")
        self.addcust.setCompanyName("busyQA")
        self.addcust.setNewsLetter("Your Store Name")
        self.addcust.setCustomerRoles("Guests")
        #self.addcust.setManagerOfVendor("Vendor 2")
        self.addcust.setAdminComment("This is for testing......")
        self.addcust.clickOnSave()

        self.logger.info("********* saving customer info ************8")
        self.logger.info("********* add custome rvalidation ************8")

        self.msg = self.driver.find_element_by_tag_name("body").txt

        print(self.msg)
        if "customer has been added sucessfully." in self.msg:
            assert True
            self.logger.info("******* Add customer test passed ********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")
            self.logger.error("*************** Add customer test Failed *************")
            assert False

        self.driver.close()
        self.logger.info("***** Ending Home page title test ******")


#thi is for randomly password generate function
def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

