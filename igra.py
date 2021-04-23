import copy


def concrete_move_number(board, value):
    return board.count(value)

def inverse_board(board):
    inverse = []
    for position in board:
        if position == "1":
            inverse.append("2")
        elif position == "2":
            inverse.append("1")
        else:
            inverse.append("X")
    return inverse



def isMill(player, board, position1, position2):
    if ((board[position1] == player) and (board[position2] == player)):
        return True
    return False



def player_have_mill(position, board):
    player = board[position]
    if (player != "X"):
        return haveBoardMill(position, board, player)
    return False


def nearPositionOnBoard(position):
    positions = [[1, 3], [0, 2, 9], [1, 4], [0, 5, 11], [2, 7, 12], [3, 6], [5, 7, 14], [4, 6], [9, 11],
                [1, 8, 10, 17], [9, 12], [3, 8, 13, 19], [4, 10, 15, 20], [11, 14], [6, 13, 15, 22], [12, 14],
                [17, 19], [9, 16, 18], [17, 20], [11, 16, 21], [12, 18, 23], [19, 22], [21, 23, 14], [20, 22]]
    return positions[position]

def haveBoardMill(position, board, player):
    mill = [
        (isMill(player,board, 1, 2) or isMill(player, board, 3, 5)),
        (isMill(player,board, 0, 2) or isMill(player, board, 9, 17)),
        (isMill(player,board, 0, 1) or isMill(player, board, 4, 7)),
        (isMill(player,board, 0, 5) or isMill(player, board, 11, 19)),
        (isMill(player,board, 2, 7) or isMill(player, board, 12, 20)),
        (isMill(player,board, 0, 3) or isMill(player, board, 6, 7)),
        (isMill(player,board, 5, 7) or isMill(player, board, 14, 22)),
        (isMill(player,board, 2, 4) or isMill(player, board, 5, 6)),
        (isMill(player,board, 9, 10) or isMill(player, board, 11, 13)),
        (isMill(player,board, 8, 10) or isMill(player, board, 1, 17)),
        (isMill(player,board, 8, 9) or isMill(player, board, 12, 15)),
        (isMill(player,board, 3, 19) or isMill(player, board, 8, 13)),
        (isMill(player,board, 20, 4) or isMill(player, board, 10, 15)),
        (isMill(player,board, 8, 11) or isMill(player, board, 14, 15)),
        (isMill(player,board, 13, 15) or isMill(player, board, 6, 22)),
        (isMill(player,board, 13, 14) or isMill(player, board, 10, 12)),
        (isMill(player,board, 17, 18) or isMill(player, board, 19, 21)),
        (isMill(player,board, 1, 9) or isMill(player, board, 16, 18)),
        (isMill(player,board, 16, 17) or isMill(player, board, 20, 23)),
        (isMill(player,board, 16, 21) or isMill(player, board, 3, 11)),
        (isMill(player,board, 12, 4) or isMill(player, board, 18, 23)),
        (isMill(player,board, 16, 19) or isMill(player, board, 22, 23)),
        (isMill(player,board, 6, 14) or isMill(player, board, 21, 23)),
        (isMill(player,board, 18, 20) or isMill(player, board, 21, 22)),
    ]
    return mill[position]


def ukloniKamencic(kopija_ploce, lista_ploca):
    for kamencic in range(len(kopija_ploce)):
        if (kopija_ploce[kamencic] == "2"):
            if not player_have_mill(kamencic, kopija_ploce):
                nova_ploca = copy.deepcopy(kopija_ploce)
                nova_ploca[kamencic] = "X"
                lista_ploca.append(nova_ploca)
    return lista_ploca


def brojMogucihMill(board, player):
    i = 0

    for position in range(len(board)):
        if (board[position] == "X"):
            if haveBoardMill(position, board, player):
                i += 1
    return i

def faza1(ploca):
    lista_ploca = []

    for kamencic in range(len(ploca)):
        if (ploca[kamencic] == "X"):
            kopija_ploce = copy.deepcopy(ploca)
            kopija_ploce[kamencic] = "1"

            if (player_have_mill(kamencic, kopija_ploce)):
                lista_ploca = ukloniKamencic(kopija_ploce, lista_ploca)
            else:
                lista_ploca.append(kopija_ploce)
    return lista_ploca

def faza2(ploca):
    lista_ploca = []

    for kamencic in range(len(ploca)):
        if (ploca[kamencic] == "1"):
            susjedne_pozicije = nearPositionOnBoard(kamencic)

            for pozicija in susjedne_pozicije:
                if (ploca[pozicija] == "X"):
                    kopija_ploce = copy.deepcopy(ploca)
                    kopija_ploce[kamencic] = "X"
                    kopija_ploce[pozicija] = "1"

                    if player_have_mill(pozicija, kopija_ploce):
                        lista_ploca = ukloniKamencic(kopija_ploce, lista_ploca)
                    else:
                        lista_ploca.append(kopija_ploce)
    return lista_ploca

def faza3(ploca):
    lista_ploca = []

    for kamencic in range(len(ploca)):
        if (ploca[kamencic] == "1"):

            for novo_mjesto in range(len(ploca)):
                if (ploca[novo_mjesto] == "X"):
                    kopija_ploce = copy.deepcopy(ploca)

                    kopija_ploce[kamencic] = "X"
                    kopija_ploce[novo_mjesto] = "1"

                    if (player_have_mill(novo_mjesto, kopija_ploce)):
                        lista_ploca = ukloniKamencic(kopija_ploce, lista_ploca)
                    else:
                        lista_ploca.append(kopija_ploce)
    return lista_ploca


# U slucaju da jedan od igraca ostane sa 3 figure na tabli prelazi se na fazu 3.
def faza23(ploca):
    if (concrete_move_number(ploca, "1") == 3):
        return faza3(ploca)
    else:
        return faza2(ploca)


def heruistickaEvaluacijaFaza23(ploca):
    brojBelih = concrete_move_number(ploca, "1")
    brojCrnih = concrete_move_number(ploca, "2")
    mills = brojMogucihMill(ploca, "1")

    evaluacija = 0

    lista_ploca = faza23(ploca)
    brojCrnihPoteza = len(lista_ploca)  # Broj poteza koje je odigrao protivnik, nakon svakog naseg poteza

    if brojCrnih <= 2 or brojCrnih == 0:
        return float('inf')
    elif brojBelih <= 2:
        return float('-inf')
    else:
        return 0


def potencijalniMill(pozicija, ploca, igrac):
    susjedne_pozicije = nearPositionOnBoard(pozicija)

    for pozicija in susjedne_pozicije:
        if (ploca[pozicija] == igrac) and (not haveBoardMill(pozicija, ploca, igrac)):
            return True
    return False

def nizKamencicaKojiFormirajuPotencijalniMill(ploca, igrac):
    brojac = 0

    for kamencic in range(len(ploca)):
        if (ploca[kamencic] == igrac):
            susjedne_pozicije = nearPositionOnBoard(kamencic)
            for pozicija in susjedne_pozicije:
                if (igrac == "1"):
                    if (ploca[pozicija] == "2"):
                        ploca[kamencic] = "2"
                        if player_have_mill(kamencic, ploca):
                            brojac += 1
                        ploca[kamencic] = igrac
                else:
                    if (ploca[pozicija] == "1" and potencijalniMill(pozicija, ploca, "1")):
                        brojac += 1

    return brojac


def isPhase3(board):
    countPlayerFigures = 0
    for field in board:
        if field == "1":
            countPlayerFigures += 1
    if countPlayerFigures == 3:
        return True
    else:
        return False


def possibleMove(position1, position2, board):
    if isPhase3(board):
        return True
    else:
        positions = nearPositionOnBoard(position1)
        print(positions)
        if position2 in positions:
            return True
        else:
            return False
