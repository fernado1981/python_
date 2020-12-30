Feature: Available flights

  @test
  Scenario: The user can find a flight from Philadelphia to New York
    Given the user is on the search page "blazedemo"
    When the user selects a departure city "Philadelphia"
    And the user selects a destination city "New York"
    And the user tap on Find Flights button
    Then flights are presented on the search result page