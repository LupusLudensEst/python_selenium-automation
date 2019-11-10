# Created by Gurov Viacheslav at 10.11.2019
Feature: Test case using BDD that opens amazon.com, clicks on Amazon Orders link and verifies that Sign In page is opened
  # HW3.3

  Scenario: Logged out user sees Sign in page when clicking Orders
    Given Open Amazon page
    When Click Amazon Orders link
    Then Verify Sign In page is open
