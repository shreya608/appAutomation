import os
import sys

from appium import webdriver
from behave import given, when, then, step
from time import sleep

PAGE_NAVIGATION_TIMER    = 3
IDLE_TIMER               = 2

@given(u'the expense tab is visible and the user clicks on it')
def step_impl(context):

        print("I am here to click on expense tab")
        assert context.ExpensePage.func_click_expense_tab() is True




@then(u'the new expense page is visible')
def step_impl(context):
    try:
        context.ExpensePage.new_expense_page()
        return
    except Exception as e:
        raise e
    finally:
        sleep(PAGE_NAVIGATION_TIMER)


@when(u'the user add the expense')
def step_impl(context):
    try:
        context.ExpensePage.input_expense()
        return
    except Exception as e:
        raise e
    finally:
        sleep (PAGE_NAVIGATION_TIMER)


@then(u'validate if the expense balance gets updated')
def step_impl(context):
    assert context.ExpensePage.is_expense_dispalyed() is True
