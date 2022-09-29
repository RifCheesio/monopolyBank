

from player import Players

gameActive = True

listOfPlayers = []
totalPlayers = 0


while gameActive:
    
    def end_game():
        gameActive = False

    def create_player(name, userRFID):
        totalPlayers += 1
        gamePlayer = Players(name, userRFID)
        listOfPlayers.append(gamePlayer)

    def add_money(userRFID, moneyToAdd):
        for player in listOfPlayers:
            if player.id == userRFID:
                player.money += moneyToAdd
        else:
            print("Player not found!")

    def sub_money(userRFID, moneyToCut):
        for player in listOfPlayers:
            if player.id == userRFID:
                player.money -= moneyToCut
        else:
            print("Player not found!")

    
