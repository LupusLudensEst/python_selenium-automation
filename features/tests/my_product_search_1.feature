# Created by Gurov Viacheslav at 05.10.2019
Feature: Google search test

  Scenario: Test google search
    Given I am on google search page
    When I type in text to search
    And I hit the search button
    Then I should be on the search results page
