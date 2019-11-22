# Created by Gurov Viacheslav at 17.11.2019
Feature: Test for product page
  #8.*

  Scenario: Size tooltip is shown upon hovering over Add To Cart button
    Given Open Amazon B074TBCSC8 page
    When Hover over Add To Cart button
    Then Veryfy size selection tooltip is shown

