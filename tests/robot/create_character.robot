*** Settings ***
Documentation       I want to create a new custom character, setting only their name.

Library             CreateCharacterLibrary.py

Test Template       Create character


*** Test Cases ***    characterNameInput    characterNameOutput
Provided name    Erin    Erin
Default name    ${EMPTY}    Character


*** Keywords ***
Create character
    [Arguments]    ${characterNameInput}    ${characterNameOutput}
    Provide character name    ${characterNameInput}
    Create the character
    Character name is    ${characterNameOutput}
