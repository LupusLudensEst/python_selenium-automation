# Created by Gurov Viacheslav at 07.10.2019
Feature: Tests for Orders functionality
  # Enter feature description here

  Scenario: Logged out user sees Sign in page when click
    Given Open Amazon page
    When Click Amazon Orders Link
    Then Verify Sign In page is opened