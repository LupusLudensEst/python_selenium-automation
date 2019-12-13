# Created by Vic at 12/12/2019
Feature: #Guest explores Ports of Departure
  # Guest explores Ports of Departure

  Scenario: Guest explores Ports of Departure
    Given a Guest
    And I am on Homepage
    And I navigated to "Ports" page
    When I search for "Honolulu" port
    Then Map zoomed to show selected port
    And Port is on the middle of the map
    And Port displayed as "Port Of Departure"
