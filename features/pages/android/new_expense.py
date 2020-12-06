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

class ExpensePage(BasePage):
    print("Reached the expense page")
    # summary page
    click_expense_tab = (By.ID, "com.monefy.app.lite:id/expense_button")
    button_keyboard_5 = (By.ID, "com.monefy.app.lite:id/buttonKeyboard5")
    button_keyboard_8 = (By.ID, "com.monefy.app.lite:id/buttonKeyboard8")
    choose_category = (By.ID, "com.monefy.app.lite:id/keyboard_action_button")
    choose_food_image = (By.ID,"com.monefy.app.lite:id/imageView")
    balance_tab = (By.ID,"com.monefy.app.lite:id/balance_amount")
    amount_text = (By.ID,"com.monefy.app.lite:id/amount_text")
    searched_text = 'Balance -$58.00'





    def func_click_expense_tab(self):
        if self.is_element_found(*self.click_expense_tab) == True:

           self.get_element(*self.click_expense_tab).click()
           return True

        else:
            return False




    def new_expense_page(self):
        if self.is_element_found(*self.amount_text) == True:
            pass
        else:
            logging.error("STDOUT: Can't find the text to add the expenses")

        return


    def input_expense(self):
        self.get_element(*self.button_keyboard_5).click()
        self.get_element(*self.button_keyboard_8).click()
        if self.is_element_found(*self.choose_category) == True:
            self.get_element(*self.choose_category).click()
            self.get_element(*self.choose_food_image).click()

        else:
            logging.error("STDOUT: Can't find the choose category tab")

        return

    def is_expense_dispalyed(self):
        expense = self.get_element(*self.balance_tab)
        if expense.text == self.searched_text:
            sys.stdout.write("\n\n the value of the expense is ${0}" .format(self.searched_text))
            return True

        else:
         return False













