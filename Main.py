from Game import Game
players = ["p0", "p1"]
game = Game(players)
print("player 0: " + game.get_player(0))
print("round: " + str(game.get_round()))
game.adv_round()
print("round: " + str(game.get_round()))