# Created by Gurov Viacheslav at 30.10.2019
Feature: Today's deal
  #hw6.1_hw6.2_today_deal


  Scenario: User can switch the windows and add product the cart
    #1
    Given Amazon today deal page
    #2
    When Store original windows
    #3
    When Click on Open Deals
    #4
    When Switch to the new openly window
    #5
    When Today's Deals are shown
    #6
    When Add product to cart
    #7
#    When Add product to cart
    #8
    When User can close new window and switch back to original
    #9
    When Refresh page
    #10
    When Click on cart
    #11
    When Cart has one item in it
    #12
    When Verify there is one item