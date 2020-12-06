import logging
import re
import sys
from time import sleep
from socket import *

from features.utils.base_page import BasePage
from features.utils.smart_driver import *
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.mobileby import By,MobileBy
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import os
from socket import *

class AddAccount(BasePage):

    settings = (MobileBy.ACCESSIBILITY_ID,"Settings")
    accounts = (By.ID,"com.monefy.app.lite:id/accounts_imagebutton")
    add_accounts = (By.ID,"com.monefy.app.lite:id/imageButtonAddCategory")
    add_name = (By.ID,"com.monefy.app.lite:id/editTextCategoryName")
    initial_account_balance = (By.ID,"com.monefy.app.lite:id/initialAmount")
    account_category = (By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.GridView/android.widget.FrameLayout[7]/android.widget.FrameLayout")
    save_account = (By.ID,"com.monefy.app.lite:id/save")
    open_navigation = (MobileBy.ACCESSIBILITY_ID,"Open navigation")
    validate_account = (By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[3]/android.widget.LinearLayout")
    account_name = "Test User"
    account_balance_value = "500"
    click_on_balance = (By.ID,"com.monefy.app.lite:id/balance_amount")
    test_user = (By.XPATH,"//hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.LinearLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.ExpandableListView/android.widget.RelativeLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView[1]"
)
    added_user = "Balance 'Test User'"



    def select_setting(self):
        try:
            if self.is_element_found(*self.settings) == True:
                self.get_element(*self.settings).click()



            else:
                logging.error("The settings element could not be clicked")


        except timeout:
            print("webdriver timedout while waiting for the settings element")




    def click_on_account(self):
        try:

            if self.is_element_found(*self.accounts) == True:
                self.get_element(*self.accounts).click()
                self.get_element(*self.add_accounts).click()

            else:
                logging.error("The user could not add the account")


        except timeout:
            print("webdriver timedout while waiting for the accounts element")



    def add_account_details(self):
        try:
            if self.is_element_found(*self.add_name) == True:
                self.get_element(*self.add_name).click()
                self.send_keys(self.account_name,*self.add_name)
                self.get_element(*self.initial_account_balance)
                self.send_keys(Keys.CLEAR,*self.initial_account_balance)
                self.send_keys(self.account_balance_value,*self.initial_account_balance)
                self.hide_keyboard()
                self.get_element (*self.account_category).click()
                self.get_element(*self.initial_account_balance).click()


            else:
                logging.error("Sorry! could not add the account details")


        except timeout:
            print("webdriver could not find the element add name")



    def choose_account_category(self):
         try:
             if self.is_element_found(*self.save_account) == True:
                 self.get_element(*self.save_account).click()

             else:
                 logging.error("unable to choose the accounts")

         except timeout:
             print("webdriver could not find the element for account category")




    def validate_account_added(self):
        if self.is_element_found(*self.click_on_balance)== True:
            self.get_element(*self.click_on_balance).click()
            added_user = self.get_element(*self.test_user)
            if added_user.text == self.added_user:
                return True


            else:
               return False

        else:
            logging.error("Unable to find the element")
















