# Created by rapid at 12/11/2019
Feature: Test case using BDD that opens www.discountmugs.com, enter e-mail into cleared field, click on sign-up btn, verify the given text is on the page

  Scenario Outline: Opens https://www.discountmugs.com page, enter e-mail into cleared field, click on sign-up btn, verify the given text is on the page
    Given Open discountmugs page
    Then Enter the e-mail into the field
    Then Click on the sign up btn
    Then Assert that given text is on the page