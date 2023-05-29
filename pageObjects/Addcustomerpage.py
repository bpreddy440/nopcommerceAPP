import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium import webdriver


class AddCustomer:

    lnkCustomers_menu_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a/p"
    linkCustomers_menuitem_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a/p"
    btnAddnew_xpath = "/html/body/div[3]/div[1]/form[1]/div/div/a"
    txtEmail_xpath = "//*[@id='Email']"
    txtPassword_xpath = "//*[@id='Password']"
    txtFirstName_xpath = "//*[@id='FirstName']"
    txtLastName_xpath = "//*[@id='LastName']"
    rdMaleGender_id = "Gender_Male"
    rdFemaleGender_id = "Gender_Female"
    txtDob_xpath = "//*[@id='DateOfBirth']"
    txtCompanyName_xpath = "//*[@id='Company']"
    txtCustomerRoles_xpath = "//*[@id='customer-info']/div[2]/div[10]/div[2]/div/div[1]/div/div"
    lstitemAdministrators_xpath = "//*[@id='SelectedCustomerRoleIds_listbox']/li[1]"
    lstitemForumAdministrators_xpath = "//*[@id='SelectedCustomerRoleIds_listbox']/li[2]"
    lstitemGuests_xpath = "//*[@id='SelectedCustomerRoleIds_listbox']/li[3]"
    lstitemRegistered_xpath = "//*[@id='SelectedCustomerRoleIds_listbox']/li[4]"
    lstitemVendors_xpath = "//*[@id='SelectedCustomerRoleIds_listbox']/li[5]"
    txtNewsLetter_xpath = "//*[@id='customer-info']/div[2]/div[9]/div[2]/div/div[1]/div/div"
    lstitemYourStoreName_xpath = "//*[@id='SelectedNewsletterSubscriptionStoreIds_listbox']/li[1]"
    lstitemTestStore2_xpath = "//*[@id='SelectedNewsletterSubscriptionStoreIds_listbox']/li[2]"
    txtAdminComment_xpath = "//*[@id='AdminComment']"
    drpmgrofVendor_xpath = "//*[@id='VendorId']"
    btnSave_xpath = "/html/body/div[3]/div[1]/form/div[1]/div/button[1]"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomerMenu(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_menu_xpath).click()

    def clickOnCustomerMenuItem(self):
        self.driver.find_element(By.XPATH, self.linkCustomers_menuitem_xpath).click()

    def clickOnAddNew(self):
        self.driver.find_element(By.XPATH, self.btnAddnew_xpath).click()

    def setEmail(self, email):
        self.driver.find_element(By.XPATH, self.txtEmail_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.txtPassword_xpath).send_keys(password)

    def setFirstName(self, firstname):
        self.driver.find_element(By.XPATH, self.txtFirstName_xpath).send_keys(firstname)

    def setLastName(self, lastname):
        self.driver.find_element(By.XPATH, self.txtLastName_xpath).send_keys(lastname)

    def setDob(self, dob):
        self.driver.find_element(By.XPATH, self.txtDob_xpath).send_keys(dob)

    def setCompanyName(self, companyname):
        self.driver.find_element(By.XPATH, self.txtCompanyName_xpath).send_keys(companyname)

    def setCustomerRoles(self, role):
        self.driver.find_element(By.XPATH, self.txtCustomerRoles_xpath).click()
        time.sleep(3)
        if role == 'Registered':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemRegistered_xpath)
        elif role == 'Administrators':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemAdministrators_xpath)
        elif role == 'Guests':
            # here user can be Registered or guest only one
            time.sleep(3)
            self.driver.find_element(By.XPATH, "//*[@id='SelectedCustomerRoleIds_taglist']/li[1]/span[2]").click()
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemGuests_xpath)
        elif role == 'Vendors':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemVendors_xpath)

        else:
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemGuests_xpath)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def setNewsLetter(self, newsletter):
        self.driver.find_element(By.XPATH, self.txtNewsLetter_xpath).click()
        time.sleep(3)
        if newsletter == 'Your Store Name':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemYourStoreName_xpath)
        elif newsletter == 'Test Store 2':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemTestStore_xpath)
        else:
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemYourStoreName_xpath)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def setManagerOfVendor(self, value):
        drp = Select(self.driver.find_element(By.XPATH, self.drpmgrofVendor_xpath))
        drp.select_by_value(value)

    def setGender(self, gender):
        if gender == 'Male':
            self.driver.find_element(By.ID, self.rdMaleGender_id).click()
        elif gender == 'Female':
            self.driver.find_element(By.ID, self.rdFemaleGender_id).click()
        else:
            self.driver.find_element(By.ID, self.rdMaleGender_id).click()

    def setAdminComment(self, admincomment):
        self.driver.find_element(By.XPATH, self.txtAdminComment_xpath).send_keys(admincomment)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH, self.btnSave_xpath).click()
