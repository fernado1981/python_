Feature: OrangeHRM

  Scenario: Logo presence on OrangeHRM home page
    Given the user is on the search page "orangehrmlive"
    When the user verify the title page "OrangeHRM"
    Then verify that the logo present on page

  Scenario: Login to OrangeHRM with valid parameters
    Given the user is on the search page "orangehrmlive"
    When Enter username "admin" and password "admin123"
    And Click on login button
    Then User must succesfully login to the Dashboard page