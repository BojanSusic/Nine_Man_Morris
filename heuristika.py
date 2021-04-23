from igra import *

def getNumberOfPieces(player,board):
    pieces=0
    for position in board:
        if player==position:
            pieces+=1
    return pieces



def position_number_heuristic(board, isState1):

    movedPartsHuman = concrete_move_number(board, "1")
    movedPartsAi = concrete_move_number(board, "2")

    if not isState1:
        possibleMovesBlack = len(faza23(board))
        if movedPartsAi <= 2 or possibleMovesBlack == 0:
            evaluation = float('inf')
        elif movedPartsHuman <= 2:
            evaluation = float('-inf')
        else:
            evaluation = 200 * (movedPartsHuman - movedPartsAi)
    else:
        evaluation = 100 * (movedPartsHuman - movedPartsAi)

    return evaluation

def human_vs_ai_heuristic(board, isState1):
    evaluation = 0

    movedPartsHuman = concrete_move_number(board, "1")
    movedPartsAi = concrete_move_number(board, "2")

    possibleMillHuman = brojMogucihMill(board, "1")
    possibleMillAi = brojMogucihMill(board, "2")

    potentialMillHuman = nizKamencicaKojiFormirajuPotencijalniMill(board, "1")
    potentialMillAi = nizKamencicaKojiFormirajuPotencijalniMill(board, "2")



    if not isState1:
        possibleMovesHuman = len(faza23(board))
        if movedPartsAi <= 2 or possibleMovesHuman == 0:
            evaluation = float('inf')
        elif movedPartsHuman <= 2:
            evaluation = float('-inf')
        else:
            if (movedPartsHuman < 4):
                evaluation += 100 * possibleMillHuman
                evaluation += 200 * potentialMillAi
            else:
                evaluation += 200 * possibleMillHuman
                evaluation += 100 * potentialMillAi
            evaluation -= 25 * possibleMovesHuman
            evaluation += 50 * (movedPartsHuman - movedPartsAi)
    else:
        if movedPartsHuman < 4:
            evaluation += 100 * possibleMillHuman
            evaluation += 200 * potentialMillAi
        else:
            evaluation += 200 * possibleMillHuman
            evaluation += 100 * potentialMillAi
        evaluation += 50 * (movedPartsHuman - movedPartsAi)

    return evaluation
