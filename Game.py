class Game:
    def __init__(self, players, era = 1, round = 0):
        self.players = players #array of player objects
        self.era = era
        self.round = round

    def get_round(self):
        return self.round

    def adv_round(self):
        self.round += 1

    def get_player(self, idx):
        return self.players[idx]

    def get_era(self):
        return self.era

    def adv_era(self):
        self.era+=1


    
