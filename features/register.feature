@register

Feature: New user registration
As a User
I should be able to create new account

    @generated_user
   Scenario: [SUNNY] Create a new user with unique name and valid credentials
    Given app is open
    When I click register button
    And I fill sign up form with generated credentials
    And I stop the music form playing in the background
    And I press submit button on sign up form
    Then User with generated credentials should exist in application database

  Scenario: [RAINY] Logging with previously registered user's credentials
    Given app is open
    When I click register button
    And I fill sign up form with credentials of already registered user
    And I stop the music form playing in the background
    And I press submit button on sign up form
    Then Registration should fail


""""
   @rainy_scenarios
   Scenario: [RAINY] Create a new user with weak password
    Given app is opened
    When I click button with partial text "register"
    And I put 'empty_user' and 'weakpass' field on sign up form
    And I press submit button on sign up form
    Then there should be no user named 'empty_user'

   @rainy_scenarios
   Scenario: [RAINY] Create a new user with empty login
    Given app is opened
    When I click button with partial text "register"
    And I put ' ' and 'weakpass' field on sign up form
    And I press submit button on sign up form
    Then there should be no user named 'empty_user'

   @rainy_scenarios
   Scenario: [RAINY] Create a new user with empty password
    Given app is opened
    When I click button with partial text "register"
    And I put 'empty_user' and ' ' field on sign up form
    And I press submit button on sign up form
    Then there should be no user named 'empty_user'

   @rainy_scenarios
   Scenario: [RAINY] Create a new user with already existing name
    Given app is opened
    When I click button with partial text "register"
    And I put valid credentials from configuration file on sign up form
    And I press submit button on sign up form
    Then I should recieve 'register' error