# Created by Gurov Viacheslav at 09.10.2019
Feature: Test case using BDD that opens amazon.com, clicks on the cart icon and verifies that Your Shopping Cart is empty
  # HW3.2

  Scenario: Opens amazon.com, clicks on the cart icon and verifies the Your Shopping Cart is empty
    Given Open Amazon page
    When Click on the shopping cart icon
    Then Verify that the shopping cart is empty
