import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from uilitites.readProperties import ReadConfig
from uilitites.customLogger import LogGen


class Test_001_Login:
    baseURL = ReadConfig.getAplicationURL()
    username = ReadConfig.getUserEmial()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_homePageTitle(self, setup):

        self.logger.info("***************** test home page title******************")
        self.logger.info("***************** verifying Homepage******************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title

        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("***************** home page title test passed ******************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            self.logger.error("***************** home page title failed******************")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("***************** verifying login test ******************")
        self.driver = setup
        self.driver.get(self.baseURL)
        # create object for Login
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title

        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("***************** login test passed ******************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.error("***************** login test failed ******************")
            assert False
