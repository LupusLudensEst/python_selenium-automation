# Created by Gurov Viacheslav at 14.10.2019
Feature: Test for hamburger menu functionality
  # HW4.1

  Scenario: Amazon Music has 6 menu items
    Given Open Amazon page
    #Done in hw4.3_hamburger_menu.py
    When Click on hamburger menu
    Then Click on Amazon music menu item
    Then 6 menu items are present
