# Created by Vic at 6/10/19
Feature: Test Scenarios for Search functionality

  Scenario: User can search for a product
    Given Open Google page
    When Input Heater into search field
    And Click on search icon
    Then Product results for Heater are shown
    And First result contains Heater