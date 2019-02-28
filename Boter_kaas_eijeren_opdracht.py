# Het spel is geschreven als functie. Dit heeft als voordeel dat het makkelijk elders kan worden ingevoegd.
def boter_kaas_eijeren():

    # Introductie en regels
    print("Welkom bij boter, kaas en eijeren (voor twee spelers).\n")
    print("Typ iedere beurt het nummer van het vak dat je in wil vullen.\n")
    print("Het spel begint. Succes!\n")

    # definitie van bord en welke combinaties winst betekenen
    board = [None] + list(range(1, 10)) # door None te gebruiken (in plaats van "_" o.i.d.) is de gebruikte definitie van wincondities mogelijk
    win_combinaties = [
        (1,2,3),
        (4,5,6),
        (7,8,9),
        (1,4,7),
        (2,5,8),
        (3,6,9),
        (3,5,7),
        (1,5,9)]

    # het bord
    def bord_stand():
        print(board[7], board[8], board[9])
        print(board[4], board[5], board[6])
        print(board[1], board[2], board[3])
        print()

    def kruisje_aan_zet():
        while True:
            try:
                x = input('Het spel is bezig. Kruisje is aan zet: ')
                x = int(x)
                break
            except:
                print("\nDat is geen getal tussen 1 en 9. Probeer het opnieuw.")
        #zorgt ervoor dat het antwoord enkel een nummer kan zijn
        if x in range(1,10):
            print()
        else:
            print("\nDat is geen getal tussen 1 en 9. Probeer het opnieuw.")
            kruisje_aan_zet()
         # Zorgt ervoor dat een bezet veld niet gekozen kan worden
        if board[x] == "X" or board[x] == "O":
            print("\nDat veld is al bezet. Probeer een ander veld.")
            kruisje_aan_zet()
        board[x] = "X"

    def rondje_aan_zet():
        while True:
            try:
                x = input('Het spel is bezig. Rondje is aan zet: ')
                x = int(x)
                break
            except:
                print("\nDat is geen getal tussen 1 en 9. Probeer het opnieuw.")
        if x in range(1,10):
            print()
        else:
            print("\nDat is geen getal tussen 1 en 9. Probeer het opnieuw.")
            rondje_aan_zet()
        if board[x] == "X" or board[x] == "O":
            print("\nDat veld is al bezet. Probeer een ander veld.")
            rondje_aan_zet()
        board[x] = "O"

    def check_winst():
         # checkt of er gewonnen is
         for a, b, c in win_combinaties:
            if board[a] == board[b] == board[c]:
                print("Je hebt gewonnen!".format(board[a]))
                print("Gefeliciteerd!\n")
                return True
         # checkt of er een gelijkspel is
         if 9 == sum((pos == 'X' or pos == 'O') for pos in board):
            print("Het spel eindigt zonder winnaar.\n")
            return True

    # het spelverloop
    bord_stand()
    while True:
        if check_winst():
            break
        else:
            kruisje_aan_zet()
            bord_stand()
        if check_winst():
            break
        else:
            rondje_aan_zet()
            bord_stand()

# Doordat het spel als functie is geschreven, kun je het makkelijk elders invoegen, zoals hieronder.
# Zo kan er ook makkelijk voor gekozen worden het spel één keer te spelen, of een beperkt aantal keren (3, 5, etc.).
while True:
    boter_kaas_eijeren()
    if input("Nog een keer spelen? (j/n)\n") != "j":
        break
