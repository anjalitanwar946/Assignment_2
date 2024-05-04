def player_1 (chocklates):
     if chocklates == 0:
        return -1 
     if chocklates == 1:
        return 1
     return player_1

def player_2 (chocklates):
     if chocklates == 0:
        return 1 
     if chocklates %2 == 1:
        return -1
     return player_2

def game():
    n=int(input("number of chocklates in bowl"))
    winner=player_1(n)
    if winner == 1:
        print("Player1 won")
    else:
        print("Player2 won")
game()