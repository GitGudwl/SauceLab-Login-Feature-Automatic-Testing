Feature:Logout
  As a user
  I want to be able to logout from my account
  So that I can securely exit my session


  Scenario: Successful logout with valid credentials
    Given I am logged in and on the dashboard page with "standard_user" username and "secret_sauce" password
    When I press the logout button
    Then I should be navigated back to the login page