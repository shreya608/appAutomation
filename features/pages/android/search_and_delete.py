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
from socket import timeout
from selenium.webdriver.common.keys import Keys


logger = logging.getLogger('behaving')




class SearchDelete(BasePage):

    search_tab = (MobileBy.ACCESSIBILITY_ID, "Search records")
    edit_search = (By.ID, "com.monefy.app.lite:id/et_search")
    selected_element_id = (By.ID, "com.monefy.app.lite:id/title_text_view")
    delete = (MobileBy.ACCESSIBILITY_ID, "Delete")
    empty_result = (By.ID, "com.monefy.app.lite:id/empty_results_text_view")
    empty_text = "No records have been found"
    search_text = "deposits"
    #search_icon = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ImageView[1]"
    searched_item = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ListView/android.view.ViewGroup"



    def click_on_search(self):

     try:

        if self.is_element_found(*self.search_tab) == True:
            self.get_element(*self.search_tab).click()
            self.send_keys(self.search_text,*self.edit_search)
            self.run_script()



        else:
            logging.error("unable to click on the search tab")


     except timeout:
         print("webdriver timedout while looking for the search tab")




    def select_searched_item(self):
        try:
            if self.is_element_found(*self.searched_item)== True:
             self.get_element(*self.searched_item).click()


            else:
                logging.error("unable to find the serached item")

        except timeout:
            print("webdriver timedout while looking for the serached item")




    def delete_searched_item(self):

        try:

            if self.is_element_found(*self.delete)== True:
                self.get_element(*self.delete).click()
                empty_screen = self.get_element(*self.empty_result)

            if empty_screen.contains(self.empty_text):
                 return True


        except timeout:
            print("webdriver timedout while seraching for the delete tab")
