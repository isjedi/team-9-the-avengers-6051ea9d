*** Settings ***
Documentation       I want to move my character. If they attempt to move past a boundary,
...                 the move results in no change in position.
...                 https://drive.google.com/file/d/1zpHwTt2c3L4T9hN_fNEqJ4US4r7dObik/view?usp=drive_link 

Library             MoveLibrary.py

Test Template       Move character


*** Test Cases ***    StartingX    StartingY    StartingMoveCount    Direction    EndingX    EndingY    EndingMoveCount
Move in the middle of the board    0    0    1    NORTH    0    1    2
Move on the edge of the board    0    0    5    SOUTH    0    0    6
Move NORTH    4    4    5    NORTH    4    5    6
Move SOUTH    4    4    5    SOUTH    4    3    6
Move WEST    4    4    6    WEST    3    4    7
Move EAST    4    4    0    EAST    5    4    1
Invalid Move    4    4    2    Z    4    4    2


*** Keywords ***
Move character
    [Arguments]
    ...    ${startingX}
    ...    ${startingY}
    ...    ${startingMoveCount}
    ...    ${direction}
    ...    ${endingX}
    ...    ${endingY}
    ...    ${endingMoveCount}
    Initialize character xposition with    ${startingX}
    Initialize character yposition with    ${startingY}
    Initialize character moveCount with    ${startingMoveCount}
    Move in direction    ${direction}
    Character xposition should be    ${endingX}
    Character yposition should be    ${endingY}
    Character moveCount should be    ${endingMoveCount}
