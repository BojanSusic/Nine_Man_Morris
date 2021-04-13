import copy
from turtle import goto

import pygame, math, sys

from alfabetarezanje import *
from igra import *
from heuristika import *
import time

alfa = float('-inf')
beta = float('inf')
dubina = 4


def trenutnaPloca(ploca):
    print(ploca[0] + "(00)----------------------" + ploca[1] + "(01)----------------------" + ploca[2] + "(02)");
    print("|                           |                           |");
    print("|       " + ploca[8] + "(08)--------------" + ploca[9] + "(09)--------------" + ploca[10] + "(10)     |");
    print("|       |                   |                    |      |");
    print("|       |                   |                    |      |");
    print("|       |        " + ploca[16] + "(16)-----" + ploca[17] + "(17)-----" + ploca[18] + "(18)       |      |");
    print("|       |         |                   |          |      |");
    print("|       |         |                   |          |      |");
    print(ploca[3] + "(03)---" + ploca[11] + "(11)----" + ploca[19] + "(19)               " + ploca[20] + "(20)----" +
          ploca[12] + "(12)---" + ploca[4] + "(04)");
    print("|       |         |                   |          |      |");
    print("|       |         |                   |          |      |");
    print("|       |        " + ploca[21] + "(21)-----" + ploca[22] + "(22)-----" + ploca[23] + "(23)       |      |");
    print("|       |                   |                    |      |");
    print("|       |                   |                    |      |");
    print("|       " + ploca[13] + "(13)--------------" + ploca[14] + "(14)--------------" + ploca[15] + "(15)     |");
    print("|                           |                           |");
    print("|                           |                           |");
    print(ploca[5] + "(05)----------------------" + ploca[6] + "(06)----------------------" + ploca[7] + "(07)");


board = ["X", "X", "X", "A", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X",
         "X", "X"]
boardCirclesProp = [[(370, 60), (0, 0, 0), 1], [(670, 60), (0, 0, 0), 1], [(970, 60), (0, 0, 0), 1],
                    [(370, 360), (0, 0, 0), 1], [(970, 360), (0, 0, 0), 1], [(370, 660), (0, 0, 0), 1],
                    [(670, 660), (0, 0, 0), 1], [(970, 660), (0, 0, 0), 1], [(470, 160), (0, 0, 0), 1],
                    [(670, 160), (0, 0, 0), 1], [(870, 160), (0, 0, 0), 1], [(470, 360), (0, 0, 0), 1],
                    [(870, 360), (0, 0, 0), 1], [(470, 560), (0, 0, 0), 1], [(670, 560), (0, 0, 0), 1],
                    [(870, 560), (0, 0, 0), 1], [(570, 260), (0, 0, 0), 1], [(670, 260), (0, 0, 0), 1],
                    [(770, 260), (0, 0, 0), 1], [(570, 360), (0, 0, 0), 1],
                    [(770, 360), (0, 0, 0), 1], [(570, 460), (0, 0, 0), 1], [(670, 460), (0, 0, 0), 1],
                    [(770, 460), (0, 0, 0), 1]]
circles = []


def drawboard():
    circles.clear()
    screen.fill((255, 255, 255))
    for boardCircle in boardCirclesProp:
        circles.append(pygame.draw.circle(screen, boardCircle[1], boardCircle[0], 20, boardCircle[2]))

    pygame.display.flip()


def boardChanged():
    for i in range(24):
        if board[i] == "X":
            boardCirclesProp[i][1] = (0, 0, 0)
            boardCirclesProp[i][2] = 1
        elif board[i] == "1":
            boardCirclesProp[i][2] = 0
        elif board[i] == "2":
            boardCirclesProp[i][2] = 0
            boardCirclesProp[i][1] = (255, 0, 0)
    print(board)
    print(boardCirclesProp)
    drawboard()


background_color = (255, 255, 255)
(width, height) = (1280, 720)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('9 Man Morris')
screen.fill(background_color)
pygame.display.flip()
running = True

drawboard()

prom = "X"
while running:
    pos = pygame.mouse.get_pos()
    ev = pygame.event.get()

    heuristika_faza1 = brojKamencicaNaPlociHeuristika
    heuristika_faza23 = CovekVS_AI_Heuristika

    evaluacija = evaluator()

    for i in range(9):
        trenutnaPloca(board)
        zavrseno = False
        while not zavrseno:
            try:
                pozicija = -1
                print("stavite kamencic na jedno mjesto")
                while pozicija == -1 and running != False:

                    ev = pygame.event.get()
                    pos = pygame.mouse.get_pos()
                    for event in ev:
                        if event.type == pygame.MOUSEBUTTONUP:
                            for i in range(len(circles)):
                                if circles[i].collidepoint(pos):
                                    pozicija = i

                        if event.type == pygame.QUIT:
                            running = False
                # Ukoliko je mjesto prazno, onda ga mozemo popuniti
                if board[pozicija] == "X":
                    board[pozicija] = "1"
                    boardChanged()
                    if imaLiIkoMill(pozicija, board):
                        # Ukoliko smo dobili MILL, prije nego sto postavimo kamencic, mozemo da uklonimo bilo koji
                        # protivnicki
                        kamencicPostavljen = False
                        while not kamencicPostavljen:
                            try:
                                pozicija = -1
                                print("ukloni protivnicki kamencic")
                                while pozicija == -1 and running != False:

                                    ev = pygame.event.get()
                                    pos = pygame.mouse.get_pos()
                                    for event in ev:
                                        if event.type == pygame.MOUSEBUTTONUP:
                                            for i in range(len(circles)):
                                                if circles[i].collidepoint(pos):
                                                    pozicija = i
                                                    boardCirclesProp[i][2] = 0
                                                    drawboard()
                                        if event.type == pygame.QUIT:
                                            running = False
                                # pozicija = int(input("\n Ukloni jedan protivnički '2' kamenčić: "))

                                if board[pozicija] == "2" and not imaLiIkoMill(pozicija, board) or (
                                        imaLiIkoMill(pozicija, board) and brojKonkretnihPoteza(board, "1") == 3):
                                    board[pozicija] = "X"
                                    boardChanged()
                                    kamencicPostavljen = True
                                else:
                                    print(
                                        "Na poziciji koju ste uneli ne postoji protivnički '2' kamenčić. Pokušajte ponovo.")
                            except Exception:
                                print("Nevalidan unos (van datog opsega/nije cijeli broj")

                    zavrseno = True

                else:
                    print("Mjesto je već zauzeto.")

            except Exception:
                print("Nevalidan unos.")

        trenutnaPloca(board)
        odgovorProtivnika = alfaBetaRezanje(board, dubina, False, alfa, beta, True, heuristika_faza1)

        if odgovorProtivnika.evaluator == float('-inf'):
            print("Izgubili ste.\n")
            exit(0)
        else:
            board = odgovorProtivnika.ploca
            boardChanged()
    zavrsneFazeGotove = False
    while not zavrsneFazeGotove:
        trenutnaPloca(board)

        # Izvrsavanje sledeceg poteza za igraca
        igracSePomjerio = False
        while not igracSePomjerio:
            try:
                pozicija = -1
                print("stavite kamencic na jedno mjesto")
                while pozicija == -1 and running != False:

                    ev = pygame.event.get()
                    pos = pygame.mouse.get_pos()
                    for event in ev:
                        if event.type == pygame.MOUSEBUTTONUP:
                            for i in range(len(circles)):
                                if circles[i].collidepoint(pos):
                                    pozicija = i

                        if event.type == pygame.QUIT:
                            running = False

                while board[pozicija] != '1':
                    pozicija = -1
                    print("stavite kamencic na jedno mjesto")
                    while pozicija == -1 and running != False:

                        ev = pygame.event.get()
                        pos = pygame.mouse.get_pos()
                        for event in ev:
                            if event.type == pygame.MOUSEBUTTONUP:
                                for i in range(len(circles)):
                                    if circles[i].collidepoint(pos):
                                        pozicija = i

                            if event.type == pygame.QUIT:
                                running = False

                igracZauzeoNovoMesto = False
                while not igracZauzeoNovoMesto:
                    nova_pozicija = -1
                    print("stavite kamencic na novo mjesto")
                    while nova_pozicija == -1 and running != False:

                        ev = pygame.event.get()
                        pos = pygame.mouse.get_pos()
                        for event in ev:
                            if event.type == pygame.MOUSEBUTTONUP:
                                for i in range(len(circles)):
                                    if circles[i].collidepoint(pos):
                                        nova_pozicija = i

                            if event.type == pygame.QUIT:
                                running = False
                    if board[nova_pozicija] == "X":
                        board[pozicija] = 'X'
                        board[nova_pozicija] = '1'
                        boardChanged()

                        if imaLiIkoMill(nova_pozicija, board):
                            uklonjenProtivnik = False
                            while not uklonjenProtivnik:
                                try:
                                    pozicija = -1
                                    print("pojedi protivnika")
                                    while pozicija == -1 and running != False:

                                        ev = pygame.event.get()
                                        pos = pygame.mouse.get_pos()
                                        for event in ev:
                                            if event.type == pygame.MOUSEBUTTONUP:
                                                for i in range(len(circles)):
                                                    if circles[i].collidepoint(pos):
                                                        pozicija = i

                                            if event.type == pygame.QUIT:
                                                running = False

                                    if board[pozicija] == "2" and not imaLiIkoMill(pozicija, board) or (
                                            imaLiIkoMill(pozicija, board) and brojKonkretnihPoteza(board, "1") == 3):
                                        board[pozicija] = "X"
                                        boardChanged()
                                        uklonjenProtivnik = True
                                    else:
                                        print("Nepostojeća pozicija.")
                                except Exception:
                                    print("Nevalidan unos.")

                        igracZauzeoNovoMesto = True
                        igracSePomjerio = True

                    else:
                        print("Ne možete se pomeriti na datu poziciju.")

            except Exception:
                print("Ne mozete se pomeriti na datu poziciju.")

        if heruistickaEvaluacijaFaza23(board) == float('inf'):
            print("Pobedili ste!")
            exit(0)

        trenutnaPloca(board)
        evaluacija = alfaBetaRezanje(board, dubina, False, alfa, beta, False, heuristika_faza23)

        if evaluacija.evaluator == float('-inf'):
            print("Izgubili ste.")
            exit(0)
        else:
            board = evaluacija.ploca
            boardChanged()