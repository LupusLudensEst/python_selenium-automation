# Created by Gurov Viacheslav at 01.11.2019
Feature: Test for Amazon Search functionality

  Scenario: Scenario: User can open and close Today's deals under $25 with 1 item in cart
    Given Open Amazon page
    When Store original window
    And Click to open Deals under 25
    And Switch to the newly opened window
    Then Todays Deals are shown
    And Open the product
    And Open the first product
    And Click Add to card buttom
    And Click second buttom
    And user can close new window and switch back to original
    And User refresh page
    And Verify cart has item