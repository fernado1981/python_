Feature: OrangeHRM

  @test
  Scenario: Logo presence on OrangeHRM home page
    Given the user is on the search page "orangehrmlive"
    When the user verify the title page "OrangeHRM"
    Then verify that the logo present on page