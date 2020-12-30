Feature: OrangeHRM Dashboard

  @test
  Scenario: Login table to OrangeHRM
    Given the user is on the search page "orangehrmlive"
    When put username "<name>" and password "<pwd>"
      |name | pwd     |
      |admin| admin123|
    And Click on login button
    Then User must succesfully login to the Dashboard page