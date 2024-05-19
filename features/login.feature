Feature: Login
    As a user
    I want to be able to login to my account
    So that I can access my personalized content
    Scenario Outline: Attempted login with valid and invalid credentials
        Given I am on the login page
        When I fill in "username" with "<username>"
        And I fill in "Password" with "<password>"
        And I press "Login"
        Then I should see "<message_type>" with this "<message>"

        Examples:
            | username      | password        | message_type | message                                                                   |
            | standard_user | secret_sauce    | positive     | Products                                                                  |
            | standard      | bond123         | negative     | Epic sadface: Username and password do not match any user in this service |
            |               |                 | negative     | Epic sadface: Username and password are required                          |
            | standard_user | standarduser321 | negative     | Epic sadface: Username and password do not match any user in this service |
            | standard_user |                 | negative     | Epic sadface: Password is required                                        |
            | standard_bond | secret_sauce    | negative     | Epic sadface: Username and password do not match any user in this service |
            |               | secret_sauce    | negative     | Epic sadface: Username is required                                        |
            | standard_bond |                 | negative     | Epic sadface: Password is required                                        |
            |               | standarduser321 | negative     | Epic sadface: Username is required                                        |
