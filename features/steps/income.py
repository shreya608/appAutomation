import os
import sys

from appium import webdriver
from behave import given, when, then, step
from time import sleep

PAGE_NAVIGATION_TIMER    = 3
IDLE_TIMER               = 2

@given(u'the income tab is visible and the user clicks on it')
def step_impl(context):
    try:
        print("I am trying to click income")
        context.IncomePage.func_click_income_tab()
        return
    except Exception as e:
        raise e
    finally:
        sleep(PAGE_NAVIGATION_TIMER)

@then(u'the new income page is visible')
def step_impl(context):
    try:
        context.IncomePage.new_income_page()
        return
    except Exception as e:
        raise e
    finally:
        sleep(PAGE_NAVIGATION_TIMER)


@when(u'the user add the income')
def step_impl(context):
    try:
        context.IncomePage.input_income()
        return
    except Exception as e:
        raise e
    finally:
        sleep (PAGE_NAVIGATION_TIMER)


@then(u'Validate if the total balance gets updated')
def step_impl(context):
    assert context.IncomePage.is_income_dispalyed() is True