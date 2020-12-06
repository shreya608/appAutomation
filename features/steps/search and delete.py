import os
import sys

from appium import webdriver
from behave import given, when, then, step
from time import sleep

PAGE_NAVIGATION_TIMER    = 3
IDLE_TIMER               = 2

@given(u'the user clicks to search')
def step_impl(context):
    try:
        context.SearchDelete.click_on_search()
        return
    except Exception as e:
        raise e
    finally:
        sleep (PAGE_NAVIGATION_TIMER)

@when(u'the searched item is visible and the user selects it')
def step_impl(context):
    try:
        context.SearchDelete.select_searched_item()
        return
    except Exception as e:
        raise e
    finally:
        sleep (PAGE_NAVIGATION_TIMER)


@then(u'the user is able to delete the item')
def step_impl(context):

    assert context.SearchDelete.delete_searched_item() is True
