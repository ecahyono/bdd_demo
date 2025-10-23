Feature: Login Feature

Scenario: Success Login with correct credential
  Given I am on the login page
  And I fill my credential
  When I click Sign in Button
  Then I Should be Logged in


Scenario: Failed Login with Wrong credential
  Given I am on the login page
  And I fill wrong credential
  When I click Sign in Button
  Then I Should be Not Logged in and see the error message
