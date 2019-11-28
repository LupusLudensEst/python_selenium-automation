# Created by Gurov Viacheslav at 28.11.2019
Feature: Lingocard_text_on_main_page
  # Just practice with lingocard.com

  Scenario: Verify if there is text on the page and ham menu has 3 items inside
    Given Open Lingocard page
    Then Verify if "International Educational Platform" is on page
    Then Verify if there are 11 boxes in the hamburger menu