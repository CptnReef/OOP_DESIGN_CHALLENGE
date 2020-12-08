from Player import Player

def menu_Screen():
    gotIt = input("\nenter to continue\n")
    return gotIt

game = Player(999,100,{},{},1,1,"","","",{})
menu_Screen()

game.fixed_Position()
menu_Screen()

game.player_Move()

