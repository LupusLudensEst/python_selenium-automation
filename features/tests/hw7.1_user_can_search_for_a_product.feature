# Created by Gurov Viacheslav at 04.11.2019
Feature: hw7.1

  Scenario: User can search for a product
    Given Open Amazon page
    When Search for dress
    Then Search results for "dress" is shown