import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from uilitites.readProperties import ReadConfig
from uilitites.customLogger import LogGen
from uilitites import XLUtils


class Test_002_DDT_Login:
    baseURL = ReadConfig.getAplicationURL()
    path = ".//TestData/sample.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("***************** test 002 ddt login ******************")
        self.logger.info("***************** verifying login test ******************")
        self.driver = setup
        self.driver.get(self.baseURL)
        # create object for Login
        self.lp = LoginPage(self.driver)
        self.rows = XLUtils.getRowCount(self.path, sheetName='Sheet1')
        print("no of rows in excel", self.rows)
        lst_status = []
        for r in range(2, self.rows+1):
            self.user = XLUtils.readdata(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readdata(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readdata(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)
            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == 'pass':
                    self.logger.info("******passed")
                    self.lp.clickLogout()
                    lst_status.append('pass')
                if self.exp == 'fail':
                    self.logger.info("***** failed")
                    self.lp.clickLogout()
                    lst_status.append('fail')

            elif act_title != exp_title:
                if self.exp == 'pass':
                    self.logger.info("******failed")
                    self.lp.clickLogout()
                    lst_status.append('fail')
                if self.exp == 'fail':
                    self.logger.info("***** passed")
                    self.lp.clickLogout()
                    lst_status.append('pass')

        if 'fail' not in lst_status:
            self.logger.info("***** login ddt test passed *****")
            self.driver.close()
            assert True
        else:
            self.logger.info("***** login ddt test failed *****")
            self.driver.close()
            assert False

        self.logger.info("***************ddt test login finished***********")

