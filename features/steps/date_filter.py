import os
import sys

from appium import webdriver
from behave import given, when, then, step
from time import sleep

PAGE_NAVIGATION_TIMER    = 3
IDLE_TIMER               = 2



@given(u'the user selects the navigation bar')
def step_impl(context):
    try:
        context.ExpenseByDate.date_filter()
        return
    except Exception as e:
        raise e
    finally:
        sleep (PAGE_NAVIGATION_TIMER)


@when(u'the user selects the filter by week')
def step_impl(context):
    try:
        context.ExpenseByDate.filter_week()
        return
    except Exception as e:
        raise e
    finally:
        sleep( PAGE_NAVIGATION_TIMER)



@then(u'the week for which expense is added should be visible')
def step_impl(context):

    assert context.ExpenseByDate.validate_change_filter() is True
