import logging
import re
import sys
from time import sleep
from socket import *

from features.utils.base_page import BasePage
from features.utils.smart_driver import *
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.mobileby import By,MobileBy
from dotenv import load_dotenv
import os


class ExpenseByDate(BasePage):
    open_navigation = (MobileBy.ACCESSIBILITY_ID,"Open navigation")
    filter_by_week = (By.ID,"com.monefy.app.lite:id/month_period_button")
    week_element = (By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.widget.TextView[2]")
    week_text = 'December'




    def date_filter(self):

      try:

        if self.is_element_found(*self.open_navigation) == True:
            self.get_element(*self.open_navigation).click()


        else:
            logging.error("Unable to find the element")

      except timeout:

             print("The webdriver timed out while waiting for the navigation element")




    def filter_week(self):
        try:

            if self.is_element_found(*self.filter_by_week) == True:
                self.get_element(*self.filter_by_week).click()


            else:
                logging.error("Unable to click on the week filter")


        except timeout:
            print ("The webdriver timed out while waiting for the week filter")



    def validate_change_filter(self):

        week = self.get_element (*self.week_element)
        print("element received",week.text)
        if week.text == self.week_text:
            sys.stdout.write ("\n\n the week filter is working and has value ${0}".format (self.week_text))
            return True

        else:
            return False

