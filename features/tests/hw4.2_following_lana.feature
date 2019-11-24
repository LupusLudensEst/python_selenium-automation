# Created by Gurov Viacheslav at 13.10.2019
Feature: Test for Amazon search functionality
  # HW4.2

  Scenario: User can search for a product
  Given Open Amazon page
    When Search for a Brain Stimulator
    And Click on search
    And Open the first product search result
    And Click on Add to Cart button
    Then Verify cart has 0 item