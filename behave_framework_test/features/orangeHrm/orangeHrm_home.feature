Feature: OrangeHRM outline

  @test
  Scenario: Login to OrangeHRM with valid parameters
    Given the user is on the search page "orangehrmlive"
    When Enter username "admin" and password "admin123"
    And Click on login button
    Then User must succesfully login to the Dashboard page

  @test
  Scenario: Logo presence on OrangeHRM home page
    Given the user is on the search page "orangehrmlive"
    When the user verify the title page "OrangeHRM"
    Then verify that the logo present on page

  @test
  Scenario Outline: Login table Examples valid to OrangeHRM
    Given the user is on the search page "orangehrmlive"
    When insert username "<name>" and password "<pwd>"
    And Click on login button
    Then User must succesfully login to the Dashboard page

    Examples:
      |name     | pwd     |
      |admin    | admin123|

  @test
  Scenario Outline: Login table Examples invalid to OrangeHRM
    Given the user is on the search page "orangehrmlive"
    When insert username "<name>" and password "<pwd>"
    And Click on login button
    Then User must unsuccesfully login to the Dashboard page

    Examples:
      |name     | pwd       |
      |admin    | admin1    |
      |admin1   | admin123  |
      |admin    | admin     |