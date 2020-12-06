import logging
import re
import sys
from time import sleep

from features.utils.base_page import BasePage
from features.utils.smart_driver import *
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.mobileby import By,MobileBy
from dotenv import load_dotenv
import os


logger = logging.getLogger('behaving')

class IncomePage(BasePage):
    click_income_tab = (By.ID, "com.monefy.app.lite:id/income_button")
    button_keyboard_5 = (By.ID, "com.monefy.app.lite:id/buttonKeyboard5")
    button_keyboard_8 = (By.ID, "com.monefy.app.lite:id/buttonKeyboard8")
    button_keyboard_0 = (By.ID, "com.monefy.app.lite:id/buttonKeyboard0")
    choose_category = (By.ID, "com.monefy.app.lite:id/keyboard_action_button")
    choose_food_image = (By.ID, "com.monefy.app.lite:id/imageView")
    balance_button = (By.ID, "com.monefy.app.lite:id/balance_amount")
    income_text = (By.ID, "com.monefy.app.lite:id/amount_text")
    searched_text = 'Balance $522.00'



    def func_click_income_tab(self):
        if self.is_element_found(*self.click_income_tab) == True:
         self.get_element(*self.click_income_tab).click()

        else:
           logging.error("Unable to find the click_income_tab")
        return


    def new_income_page(self):
        if self.is_element_found (*self.income_text) == True:
            pass
        else:
            logging.error("STDOUT: Can't find the text to add the income")

        return


    def input_income(self):
        self.get_element(*self.button_keyboard_5).click()
        self.get_element(*self.button_keyboard_8).click()
        self.get_element(*self.button_keyboard_0).click()
        if self.is_element_found(*self.choose_category) == True:
            self.get_element(*self.choose_category).click()
            self.get_element(*self.choose_food_image).click()

        else:
            logging.error("STDOUT: Can't find the choose category tab")

        return

    def is_income_dispalyed(self):

        income =self.get_element(*self.balance_button)
        if income.text == self.searched_text:
            sys.stdout.write("\n\n the value of the total expense is ${0}" .format(self.searched_text))
            return True

        else:
         return False






