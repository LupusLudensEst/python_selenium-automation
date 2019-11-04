# Created by Gurov Viacheslav at 30.10.2019
Feature: Today's deal
  #hw6.2_hw6.2_today_deal


  Scenario: User can switch the windows and add product the cart
    Given Amazon today deal page
    When Store original windows
    When Click on Open Deals
    When Switch to the new openly window
    When Today's Deals are shown
    And Click on product name
    And Add product to cart
    And User can close new window and switch back to original
    And Refresh page
    And Click on cart
    When Cart has one item in it
    When Verify there is one item