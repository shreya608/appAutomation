# Charters

Charters for Monify App.

#### Charter 01
**Explore:** Expense Tab
**with:** various inputs for Add new expense
**to discover:** whether the user is able to add expenses by  selecting different categories from the expense tab
**Time Alotted:** 60 minutes
**Priority:** High
**Findings:** After user adds a new expense popup is displayed about the success message but when user click on Cancel to close that popup, the added expense is removed, I think this is little confusing as the user will not know what is the cancel button actually for.

#### Charter 02
**Explore:** Expense Tab
**with:** various inputs for Edit existing expense
**to discover:** whether the user is able to edit already created expenses
**Time Alotted:** 60 minutes
**Priority:** Medium
**Findings:** When user clicks on any expense category from the chart, the previously selected value is not displayed. However user can see the selected value the edit the data when he clicks on Balance and then navigate to the category he wants to edit.

#### Charter 03
**Explore:** Expense Tab
**with:** various inputs for 'Delete existing expense`
**to discover:** whether the user is able to delete already created expenses
**Time Alotted:** 60 minutes
**Priority:** High
**Findings:** Same issue as in **charter 02**, User can't delete the any value by directly clicking on a category.

#### Charter 04
**Explore:** Income Tab
**with:** various inputs for Add new income
**to discover:** whether the user is able to add income by  selecting different income categories
**Time Alotted:** 30 minutes
**Priority:** High
**Findings:** Except the finding in Charter 1 rest everything worked well.

#### Charter 05
**Explore:** Income Tab
**with:** various inputs for Edit existing income
**to discover:** whether the user is able to edit already created incomes
**Time Alotted:** 30 minutes
**Priority:** Medium
**Findings:** Everything working fine

#### Charter 06
**Explore:** Income Tab
**with:** various inputs for Delete existing income
**to discover:** whether the user is able to delete already created income
**Time Alotted:** 30 minutes
**Priority:** High
**Findings:** Everything working fine

#### Charter 07
**Explore:** Chart Screen
**with:** the data entered in **charter 01** to **charter 06**
**to discover:** whether the correct expense is getting displated in the chart
**Time Alotted:** 40 minutes
**Priority:** High
**Findings:** Sometimes Expense button is displayed as 'Expense' and sometimes its displayed as '-'. Sometimes Income button is displayed as 'Income' and sometimes its displayed as '+'

#### Charter 08
**Explore:** Chart Screen
**with:** the data entered in **charter 01** to **charter 06**
**to discover:** whether correct percentage is getting displayed for each expense categories
**Time Alotted:** 60 minutes
**Priority:** High
**Findings:** Everything working fine

#### Charter 09
**Explore:** Chart Screen
**with:** the data entered in **charter 01** to **charter 06**
**to discover:** whether the correct value is displayed for total income and total expense
**Time Alotted:** 30 minutes
**Priority:** High
**Findings:** Everything working fine

#### Charter 10
**Explore:** Chart Screen
**with:** Search records
**to discover:** all the added records are searchable
**Time Alotted:** 60 minutes
**Priority:** Medium
**Findings:** Everything working fine

#### Charter 11
**Explore:** the left side bar
**with:** different data range options
**to discover:** the expense for a day, week, month, year, all, with date range or a particular date
**Time Alotted:** 60 minutes
**Priority:** High
**Findings:** 1. If user selects date range from 'Interval' then the expenses are displayed in that particular date range but after this if user tries to selct 'Day` option then it doesn't get reset to current date.
2. Also I feel future date selection should be disabled in 'Interval' date selection.
3. When user selects 'All' option then on expense chart screen date range is displayed from current date to some random date.
4. By default current date marked in a any calender is 1 day before the current date. Eg when testing of the app was done on 5th December, in all the calender controls highlighted date was 4th December

#### Charter 12
**Explore:** the Right side bar
**with:** categories option
**to discover:** the icons for each categories can be changed only if user subscribe for Monify Pro option.
**Time Alotted:** 10 minutes
**Priority:** Medium
**Findings:** Everything working fine

#### Charter 13
**Explore:** the Right side bar
**with:** categories option
**to discover:** different categories can be merged by the user
**Time Alotted:** 30 minutes
**Priority:** Low
**Findings:** Everything working fine

#### Charter 14
**Explore:** the Right side bar
**with:** categories option
**to discover:** the categories can be disabled and enabled
**Time Alotted:** 30 minutes
**Priority:** Low
**Findings:** Everything working fine

#### Charter 15
**Explore:** the Right side bar
**with:** categories Account
**to discover:** different accounts can be added to the app.
**Time Alotted:** 60 minutes
**Priority:** High
**Findings:** 1. When user creates an account and add some amount to it, the whole balance money gets added to it and if the user unchecks the 'included in the balance' option then entire balance money gets removed.
2. Also if user deletes the added account the whole balance money gets removed.

#### Charter 16
**Explore:** the Right side bar
**with:** categories option
**to discover:** amount can be transfered from 1 account to another account within the app
**Time Alotted:** 60 minutes
**Priority:** High
**Findings:** Everything working fine

#### Charter 17
**Explore:** the Right side bar
**with:** categories Currencies
**to discover:** the currencies can be changed.
**Time Alotted:** 10 minutes
**Priority:** Medium
**Findings:** Everything working fine

#### Charter 18
**Explore:** the Right side bar
**with:** categories Currencies
**to discover:** the currencies can only be changed if user opts for Monify Pro option
**Time Alotted:** 10 minutes
**Priority:** Medium
**Findings:** Everything working fine

#### Charter 19
**Explore:** the Right side bar
**with:** categories Settings
**to discover:** the currencies can select different Balace Mode
**Time Alotted:** 15 minutes
**Priority:** Low
**Findings:** Everything working fine

#### Charter 20
**Explore:** the Right side bar
**with:** categories Settings
**to discover:** user can select different languages from the list of languages available
**Time Alotted:** 30 minutes
**Priority:** Low
**Findings:** Everything working fine

#### Charter 21
**Explore:** the Right side bar
**with:** categories Settings
**to discover:** the other General Settings for the app
**Time Alotted:** 60 minutes
**Priority:** Medium
**Findings:** Everything working fine

#### Charter 22
**Explore:** the Right side bar
**with:** categories Settings
**to discover:** the Upgrade to Pro option which provides extra features like theme change, connect to google drive, dropbox and some fetures mentioned in above Charts
**Time Alotted:** 30 minutes
**Priority:** Medium
**Findings:** Everything working fine

**Note:** *All the charters that are marked as priority **High** will be considered to explored first because either those are linked the the basic and main functionality of the application or linked with the revenue generation.
All high priority charters constitutes the basic functional completeness of this app.*

> **Risks:** As this application tracks each and every expense of an individual, data security is the biggest challenge. As the app is also accessing google drive and dropbox access it has access to other accounts as well, so special care needs to be done with special password and finger print protection so that if a person looses the phone, he should not loose the entire data.

