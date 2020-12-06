import os
import sys

from appium import webdriver
from behave import given, when, then, step
from time import sleep

PAGE_NAVIGATION_TIMER    = 3
IDLE_TIMER               = 2


@given(u'the user clicks on settings')
def step_impl(context):
    try:
     context.AddAccount.select_setting()
     return
    except Exception as e:
        return e

    finally:
        sleep(PAGE_NAVIGATION_TIMER)

@then(u'the user selects account to add a new account')
def step_impl(context):
    try:
        context.AddAccount.click_on_account()
        return
    except Exception as e:
        return e
    finally:
        sleep(PAGE_NAVIGATION_TIMER)


@then(u'the user add the new account details')
def step_impl(context):
    try:
        context.AddAccount.add_account_details()
        return
    except Exception as e:
        return e
    finally:
        sleep(PAGE_NAVIGATION_TIMER)


@when(u'the user chooses the account category')
def step_impl(context):
    try:
        context.AddAccount.choose_account_category()
        return
    except Exception as e:
        return e

    finally:
        sleep(PAGE_NAVIGATION_TIMER)


@then(u'the new account should be visible')
def step_impl(context):

     assert context.AddAccount.validate_account_added()


