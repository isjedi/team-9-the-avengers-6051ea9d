*** Settings ***
Documentation   I want to move my character. If they attempt to move past a boundary, the move results in no change in position.
Test Template   Move character
Library         MoveLibrary.py

*** Test Cases ***      StartingX   StartingY   Direction   EndingX EndingY
Move in middle of board 0           0           NORTH       0       1
Move on edge of board   0           0           SOUTH       0       0
Move NORTH              4           4           NORTH       4       5
Move SOUTH              4           4           SOUTH       4       3
Move EAST               4           4           EAST        5       4
Move WEST               4           4           WEST        3       4
Invalid entry           4           4           NULL        4       4


*** Keyboards ***
Move character
    [Arguments]     ${startingX}    ${startingY}    ${direction}    ${endingX}  ${endingY}
    Initialize character xposistion with    ${startingX}
    Initialize character yposistion with    ${startingY}
    Move in direction   ${direction}
    Character xposition should be   ${endingX}
    Character yposition should be   ${endingY}

