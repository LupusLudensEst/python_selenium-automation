# Created by Gurov Viacheslav at 28.10.2019
Feature: Tests for Sign In Functionality
  #hw6.1

  Scenario: Sign In page can be opened by clicking on Sign In tooltip
    Given Open Amazon page
    When Click on the Sign in icon Enter
    Then Verify Sign In page is open

#  Scenario: Sign In tooltip appears and disappears
#    Given Open Amazon page
#    Then Verify SignIn tooltip is present and clickable
#    When Wait until SignIn tooltip disappears
#    Then Verify SignIn tooltip is not clickable