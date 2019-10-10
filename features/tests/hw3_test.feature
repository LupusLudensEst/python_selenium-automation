# Created by Gurov Viacheslav at 06.10.2019
Feature: Google search test
# HW3

  Scenario: Test google search
    Given I am on google search page
    When I type in text to search
    And I hit search button
    Then I should be on the search results page
