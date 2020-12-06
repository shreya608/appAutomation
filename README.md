## Task1:
https://github.com/shreya608/appAutomation/blob/master/charters/Charters.md#charters

## Task2:
## Structure of the framework

#### behave.ini
is where all the desired capabilities of app are added. To run the app add the desired capabilities here.

#### feature
Contains feature files, steps implementaion files and environment file.

###### steps
1. Contains step files for all the above feature files
2. Contains all Given, When, Then, step implementation functions.

###### environment.py
Includes BDD Hooks functions(before_all, after_all, before_scenario, after_scenario, before_step, after_step, before_tag, after_tag) definition.

###### Feature file. BDD cucumber test scenarios files.
> pages/Android: Each file stands for one specific page on Android App. Element(Object) ID, operation on page are defined in this file.


**utils:** Utility tool folder. It contains some non-page related operation for example: initialize web driver, base page.

**Reports**
This folder will be generated after "run.sh" script. It will contain screenshot and test report .json format files.

#### How to run
Setup the running ENV
Open a terminal and run "./run.sh"

> **Note:** Ideally it should work above python 3.0 versions but if it doesn't work then try running it on 2.7

> **Automated Flows:**
1. I would write my automation focussing on user journey rather than on individual test cases.
2. User launches the app
3. Adds an expense and checks if it is properly added.
4. Adds an Income and checks if it is properly added.
5. User checks the Balance on the Chart page
6. User navigates to the right panel to add an account and then checks if it is added properly.
7. User had added a wrong Income so he wants to delete it for which he uses search functionality to search it.
8. Once the item is searched the user deletes the Income and checks if the income was deleted successfully.
9. User also tries to check the expense on monthly basis so he goes to left panel and selects month and verifies the data.

**Note:** 
1. As the .apk file was not available in the assignment document, so the app data were not getting cleared as it was run with the same app everytime. 
2. For the automatetd flow -8, the app searches the element but because the searched element was not accessible by xpath(Screenshot attached) the step fails. It can be made accessible by adding the resource id and then the test would work.
3. For automated flow -9, the same problem. the elements were not accessible by either the xpath or the id.

![Alt text](/./screenshots/ScreenshotReport1.png?raw=true "Dashboard")
![Alt text](/./screenshots/ScreenshotReport2.png?raw=true "Dashboard")




