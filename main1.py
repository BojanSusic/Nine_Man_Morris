# -*- coding: utf-8 -*-

from alfabetarezanje import *
from igra import *
from heuristika import *
import time

alfa = float('-inf')
beta = float('inf')
dubina = 3


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


def HUMAN_VS_AI(heuristika_faza1, heuristika_faza23):
    ploca = []

    # "Popunjavamo" plocu sa praznim mjestima
    for i in range(24):
        ploca.append("X")

    evaluacija = evaluator()

    for i in range(9):
        trenutnaPloca(ploca)
        zavrseno = False
        while not zavrseno:
            try:
                pozicija = int(input("\nStavite kamenčić '1' na neko od praznih polja: "))

                #Ukoliko je mjesto prazno, onda ga mozemo popuniti
                if ploca[pozicija] == "X":
                    ploca[pozicija] = "1"
                    if imaLiIkoMill(pozicija, ploca):
                        #Ukoliko smo dobili MILL, prije nego sto postavimo kamencic, mozemo da uklonimo bilo koji
                        # protivnicki
                        kamencicPostavljen = False
                        while not kamencicPostavljen:
                            try:
                                pozicija = int(input("\n Ukloni jedan protivnički '2' kamenčić: "))

                                if ploca[pozicija] == "2" and not imaLiIkoMill(pozicija, ploca) or (imaLiIkoMill(pozicija, ploca) and brojKonkretnihPoteza(ploca, "1") == 3):
                                    ploca[pozicija] = "X"
                                    kamencicPostavljen = True
                                else:
                                    print ("Na poziciji koju ste uneli ne postoji protivnički '2' kamenčić. Pokušajte ponovo.")
                            except Exception:
                                print ("Nevalidan unos (van datog opsega/nije cijeli broj")

                    zavrseno = True

                else:
                    print ("Mjesto je već zauzeto.")

            except Exception:
                print("Nevalidan unos.")

        trenutnaPloca(ploca)
        odgovorProtivnika = alfaBetaRezanje(ploca, dubina, False, alfa, beta, True, heuristika_faza1)

        if odgovorProtivnika.evaluator == float('-inf'):
            print("Izgubili ste.\n")
            exit(0)
        else:
            ploca = odgovorProtivnika.ploca
    zavrsneFazeGotove = False
    while not zavrsneFazeGotove:
        trenutnaPloca(ploca)

        #Izvrsavanje sledeceg poteza za igraca
        igracSePomjerio = False
        while not igracSePomjerio:
            try:
                pozicija = int(input("\nPomjerite '1' kamenčić: "))

                while ploca[pozicija] != '1':
                    pozicija = int(input("\nPomjerite '1' kamenčić: "))

                igracZauzeoNovoMesto = False
                while not igracZauzeoNovoMesto:
                    nova_pozicija = int(input("Nova lokacija za '1' kamenčić: "))

                    if ploca[nova_pozicija] == "X":
                        ploca[pozicija] = 'X'
                        ploca[nova_pozicija] = '1'

                        if imaLiIkoMill(nova_pozicija, ploca):
                            uklonjenProtivnik = False
                            while not uklonjenProtivnik:
                                try:
                                    pozicija = int(input("\nUklonite '2' kamenčić: "))

                                    if ploca[pozicija] == "2" and not imaLiIkoMill(pozicija, ploca) or (imaLiIkoMill(pozicija,ploca) and brojKonkretnihPoteza(ploca, "1") == 3):
                                        ploca[pozicija] = "X"
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

        if heruistickaEvaluacijaFaza23(ploca) == float('inf'):
            print("Pobedili ste!")
            exit(0)

        trenutnaPloca(ploca)
        evaluacija = alfaBetaRezanje(ploca, dubina, False, alfa, beta, False, heuristika_faza23)

        if evaluacija.evaluator == float('-inf'):
            print("Izgubili ste.")
            exit(0)
        else:
            ploca = evaluacija.ploca

if __name__ == "__main__":
   while True:
        HUMAN_VS_AI(brojKamencicaNaPlociHeuristika, CovekVS_AI_Heuristika)
