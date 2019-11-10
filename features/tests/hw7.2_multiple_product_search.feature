# Created by Gurov Viacheslav at 08.11.2019
Feature: Multiple product search

  Scenario Outline: User can search for a product
    Examples:
    |keyword|expected_result|
    |dress  |"dress"        |
    |shoes  |"shoes"        |
    |toys   |"toys"         |

    Given Open Amazon page
    When Search for <keyword>
    Then Search results for <expected_result> is shown