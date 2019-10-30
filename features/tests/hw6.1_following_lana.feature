# Created by Gurov Viacheslav at 29.10.2019
Feature: Tests for Orders functionality
  #hw6.1_following_lana

  Scenario: Sign In tooltip appears and disappears1
    Given Open Amazon page
    Then Verify SignIn tooltip is present and clickable1
    When Wait until SignIn tooltip disappears1
    Then Verify SignIn tooltip is not clickable1