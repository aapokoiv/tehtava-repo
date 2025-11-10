*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  aapo
    Set Password  aapo1234
    Set Password Confirmation  aapo1234
    Click Button  Register
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  aa
    Set Password  aapo1234
    Set Password Confirmation  aapo1234
    Click Button  Register
    Register Should Fail With Message  Username should be atleast 3 characters long

Register With Valid Username And Too Short Password
    Set Username  aapo
    Set Password  aapo1
    Set Password Confirmation  aapo1
    Click Button  Register
    Register Should Fail With Message  Password should be atleast 8 characters long

Register With Valid Username And Invalid Password
    Set Username  aapo
    Set Password  aapoaapo
    Set Password Confirmation  aapoaapo
    Click Button  Register
    Register Should Fail With Message  Password should include numbers or special characters

Register With Nonmatching Password And Password Confirmation
    Set Username  aapo
    Set Password  aapoaapo1
    Set Password Confirmation  aapoaapo2
    Click Button  Register
    Register Should Fail With Message  Passwords don't match

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Click Button  Register
    Register Should Fail With Message  User with username kalle already exists

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page
