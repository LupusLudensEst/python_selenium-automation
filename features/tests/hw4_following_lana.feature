# Created by Gurov Viacheslav at 13.10.2019
Feature: Test for Amazon search functionality
  # HW3.4b

  Scenario: User can search for a product
  Given Open page Amazon
    When Search for a Brain Stimulator
    And Click on search
    And Open the first product search result
    And Click on Add to Cart button
    Then Verify cart has 1 item