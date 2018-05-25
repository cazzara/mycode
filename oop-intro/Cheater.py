from Player import Player


class Cheater_Loaded(Player):
    def cheat(self):
        i = 0
        while i < len(self.dice):
            if self.dice[i] < 6:
                self.dice[i] += 1
            i += 1

class Cheater_Swapper(Player):
    def cheat(self):
        self.dice[-1] = 6
