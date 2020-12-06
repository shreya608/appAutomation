import allure
import hashlib
import os
import sys

from allure_commons.types import AttachmentType
from appium import webdriver
import time
from time import sleep
from features.utils.smart_driver import *
from logger import logging

IDLE_TIMER    =  3

global gCWD , gSCREEN_SHOTS_PATH
gCWD = os.getcwd()
gSCREEN_SHOTS_PATH = CWD + "/reports/screenshots/"


"""
before_step(context, step), after_step(context, step)
    These run before and after every step.
    The step passed in is an instance of Step.

before_scenario(context, scenario), after_scenario(context, scenario)
    These run before and after each scenario is run.
    The scenario passed in is an instance of Scenario.

before_feature(context, feature), after_feature(context, feature)
    These run before and after each feature file is exercised.
    The feature passed in is an instance of Feature.

before_tag(context, tag), after_tag(context, tag)

"""
logger = logging.getLogger('environment')

#Hooks
def before_all(context):
    context.config.setup_logging()
    driver_setup(context.config.userdata.get("appium_host", "unknown"),
                 context.config.userdata.get("appium_port", "unknown"),
                 context.config.userdata.get("appium_version", "unknown"),
                 context.config.userdata.get("platform_name", "unknown"),
                 context.config.userdata.get("platform_version", "unknown"),
                 context.config.userdata.get("device_name", "unknown"),
                 context.config.userdata.get("browser_name", "unknown"),
                 context.config.userdata.get("device_orientation", "unknown"),
                 context.config.userdata.get("test_name", "unknown"),
                 context.config.userdata.get("app_package", "unknown"),
                 context.config.userdata.get("app_activity", "unknown"))
    start_driver(context)

def after_all(context):
    #TODO
    #uninstall the app on cloude device
    #context.driver.remove_app(context.config.userdata.get("app_uri"));
    pass

def before_feature(context, feature):
    pass

def before_scenario(context, scenario):
    #start_activity()
    #Android ONLY
    #get_current_activity()
    pass

def after_scenario(context, scenario):
    #TODO
    pass

#def after_feature(context, feature):
 #   cleanup_driver(context)

def before_step(context, step):
    pass

def after_step(context, step):
    if step.status == "failed":
        ts = time.time ()
        st = time.ctime (ts)
        screenshot_file = gSCREEN_SHOTS_PATH + step.name + "_" + st + ".png"
        take_screenshot (context, screenshot_file)
        allure.attach (context.driver.get_screenshot_as_png (), name="Screenshot", attachment_type=AttachmentType.PNG)
        sleep (IDLE_TIMER)
    pass

def after_scenario(context, scenario):
    logging.info('scenario steps %s' % scenario.steps)
    return scenario

def before_tag(context, tag):
    pass

def after_tag(context, tag):
    pass
