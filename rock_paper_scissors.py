#Rodrigo Drumond Valente
#Rock Paper Scissors
#Play against CPU or Player

from random import*

qtt_plays = int(input("Type how many plays:"))

if qtt_plays < 0:
    print("Invalid.")
else:
    for i in range(qtt_plays):
        choice = int(input("Play against computer (1) or player (2):"))
        if choice < 1 or choice > 2:
            print("Invalid!")
        else:
            if choice == 1:
                print("------MENU------\n0 - Rock\n1 - Paper\n2 - Scissors\n----------------\n")
                player1 = int(input("Type an option:"))
                computer = randint(0, 2)
                if player1 < 0 or player1 > 2:
                    print("Invalid!")
                else:
                    if player1 == 0 and computer == 0:
                        bet = "Rock x Rock"
                        result = "Tie!"
                    else:
                        if player1 == 1 and computer == 1:
                            bet = "Paper x Paper"
                            result = "Tie!"
                        else:
                            if player1 == 2 and computer == 2:
                                bet = "Scissors x Scissors"
                                result = "Tie!"
                            else:
                                if player1 == 0 and computer == 1:
                                    bet = "Rock x Paper"
                                    result = "Win! Computer"
                                else:
                                    if player1 == 0 and computer == 2:
                                        bet = "Rock x Scissors"
                                        result = "Win! Player 1"
                                    else:
                                        if player1 == 1 and computer == 0:
                                            bet = "Paper x Rock"
                                            result = "Win! Player 1"
                                        else:
                                            if player1 == 1 and computer == 2:
                                                bet = "Paper x Scissors"
                                                result = "Win! Computer"
                                            else:
                                                if player1 == 2 and computer == 0:
                                                    bet = "Scissors x Stone"
                                                    result = "Win! Computer"
                                                else:
                                                    bet = "Scissors x Paper"
                                                    result = "Win! Player 1"
                    print(f"{bet} - {result}")
            else:
                print("------MENU------\n0 - Pedra\n1 - Papel\n2 - Tesoura\n----------------\n")
                player1 = int(input("Type an option:"))
                player2 = int(input("Type an option:"))
                if player1 < 0 or player1 > 2 or player2 < 0 or player2 > 2:
                    print("Inválido!")
                else:
                    if player1 == 0 and player2 == 0:
                        bet = "Rock x Rock"
                        result = "Tie!"
                    else:
                        if player1 == 1 and player2 == 1:
                            bet = "Paper x Paper"
                            result = "Tie!"
                        else:
                            if player1 == 2 and player2 == 2:
                                bet = "Scissors x Scissors"
                                result = "Tie!"
                            else:
                                if player1 == 0 and player2 == 1:
                                    bet = "Rock x Paper"
                                    result = "Win! Player 2"
                                else:
                                    if player1 == 0 and player2 == 2:
                                        bet = "Rock x Scissors"
                                        result = "Win! Player 1"
                                    else:
                                        if player1 == 1 and player2 == 0:
                                            bet = "Paper x Rock"
                                            result = "Win! Player 1"
                                        else:
                                            if player1 == 1 and player2 == 2:
                                                bet = "Paper x Scissors"
                                                result = "Win! Player 2"
                                            else:
                                                if player1 == 2 and player2 == 0:
                                                    bet = "Scissors x Stone"
                                                    result = "Win! Player 2"
                                                else:
                                                    bet = "Scissors x Paper"
                                                    result = "Win! Player 1"
                    print(f"{bet} - {result}")