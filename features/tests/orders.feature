# Created by Gurov Viacheslav at 07.10.2019
Feature: Tests for Orders functionality
  #hw6.1_following_lana

  Scenario: Logged out user sees Sign in page when click on it
    Given Open Amazon page
    When Click Amazon Orders Link
    Then Verify Sign In page is open

   Scenario: 'Your Shopping Cart is empty' shown if no product added
    Given Open Amazon page
    When Click on cart icon
    Then Verify 'Your Shopping Cart is empty.' text present

#================================================TOOLTIP===========================================================

#  Scenario: Sign In tooltip appears and disappears
#    Given Open Amazon page
#    Then Verify SignIn tooltip is present and clickable
#    When Wait until SignIn tooltip disappears
#    Then Verify SignIn tooltip is not clickable
