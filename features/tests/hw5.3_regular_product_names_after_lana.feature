# Created by Gurov Viacheslav at 27.10.2019
Feature: Test for verify every product on the page has a text Regular and a product name
  # HW5.3.after_lana

  Scenario: Verify every product on the page has a text Regular and a product name
    Given Open Amazon wholefoodsdeals page as Lana did
    Then Verify every product on the page has a text Regular and a product name as Lana did