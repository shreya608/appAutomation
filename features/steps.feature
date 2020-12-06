@Android
Feature: Validate the monefy app by adding expenses and income

  Scenario: check if the new balance gets added
    Given the expense tab is visible and the user clicks on it
    Then the new expense page is visible
    When the user add the expense
    Then validate if the expense balance gets updated



  Scenario: check if the new income gets added
    Given the income tab is visible and the user clicks on it
    Then  the new income page is visible
    When  the user add the income
    Then  Validate if the total balance gets updated



  Scenario: check if the new account gets added
    Given the user clicks on settings
    Then  the user selects account to add a new account
    Then  the user add the new account details
    When  the user chooses the account category
    Then  the new account should be visible


  Scenario: check if the date filter is working
    Given the user selects the navigation bar
    When  the user selects the filter by week
    Then  the week for which expense is added should be visible


  Scenario: check if the search and delete is working
    Given the user clicks to search
    When  the searched item is visible and the user selects it
    Then  the user is able to delete the item









