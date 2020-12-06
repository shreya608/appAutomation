import os

from appium import webdriver

#from appium import Saucelabs
#from appium import SauceTestCase
#from appium import on_platforms
#from sauceclient import SauceClient
from features.pages.android.new_expense  import ExpensePage
from features.pages.android.new_income import IncomePage
from features.pages.android.date_filter import ExpenseByDate
from features.pages.android.add_account import AddAccount
from features.pages.android.search_and_delete import SearchDelete




CWD = os.getcwd()
SCREEN_SHOTS_PATH = CWD + "/reports/screenshots/"

__driver_configs = {}

def driver_setup(host, port, appium_version, platform_name, platform_version,
                 device_name, browser_name, device_orientation, test_name, app_package,app_activity):
    __driver_configs['host'] = host
    __driver_configs['port'] = port
    __driver_configs['appium_version'] = appium_version
    __driver_configs['platform_name'] = platform_name
    __driver_configs['platform_version'] = platform_version
    __driver_configs['device_name'] = device_name
    __driver_configs['browser_name'] = browser_name
    __driver_configs['device_orientation'] = device_orientation
    __driver_configs['test_name'] = test_name
    __driver_configs['app_package'] = app_package
    __driver_configs['app_activity'] = app_activity


def start_driver(context):
    try:
        context.driver = webdriver.Remote(
        command_executor='http://%s:%s/wd/hub' % (__driver_configs.get('host'),__driver_configs.get('port')),
        desired_capabilities={
            'platformName': __driver_configs.get('platform_name'),
            'platformVersion': __driver_configs.get('platform_version'),
            'deviceName': __driver_configs.get('device_name'),
            'appPackage':  __driver_configs.get('app_package'),
            'appActivity': __driver_configs.get('app_activity'),
            'noReset': True,
            'fullReset': False
        })

        context.platform = __driver_configs.get('platform_name')
        if context.platform == 'Android':

            context.ExpensePage = ExpensePage(context.driver)
            context.IncomePage = IncomePage(context.driver)
            context.ExpenseByDate = ExpenseByDate(context.driver)
            context.AddAccount = AddAccount(context.driver)
            context.SearchDelete = SearchDelete(context.driver)
        else:
            raise RuntimeError('Unrecognized platform: {}'.format(context.platform))

    except Exception,e:
        raise e

def take_screenshot(context, filename):
    # ts = time.time()
    # st = time.ctime(ts)
    # screenshot_file =  SCREEN_SHOTS_PATH + filename + st + ".PNG"
    
    context.driver.save_screenshot(filename)

def cleanup_driver(context):
    context.driver.quit()

def teardown_driver(context):
    context.driver.quit()
