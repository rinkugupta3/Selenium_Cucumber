# "And" in the feature file is used to indicate an additional action within the same scenario,
# while the "Then" steps in the Python code define the expected outcomes.
# This aligns with the correct usage of "And" and "Then" in BDD.

Feature: OrangeHRM Login Test

  Scenario: Open webpage
    Given I am on the OrangeHRM login page

  Scenario: Input valid userid and password
    When I enter valid credentials

  Scenario: Click login button
    When I click the login button

  Scenario: User directed to dashboard home page
    Then I should be redirected to the dashboard page

  Scenario: Click logout
    Then I log out from the dashboard page

  Scenario: Close browser and quit
    And I close the browser

    