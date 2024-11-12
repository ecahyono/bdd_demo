Feature: Login Feature

Scenario: Success Login with correct credential
  Given I am on the loggin page
  And I fill my credential
  When I am click Sign in Button
  Then I Shoud be Logged in


Scenario: Failed Login with Wrong credential
  Given I am on the loggin page
  And I fill wrong credential
  When I am click Sign in Button
  Then I Shoud be Not Logged in and see the error message
