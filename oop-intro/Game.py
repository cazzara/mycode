from Player import Player
from time import sleep
from Cheater import Cheater_Loaded, Cheater_Swapper
from random import random

class Game:
    def __init__(self):
        self.main()

    def make_player(self):
        p = None
        name = input("Enter your name: ")
        cheat = input("Are you a cheater? (y/n)")
        if cheat[0].lower() == 'y':
            cheat_type = int(random()*10)
            if cheat_type <= 5:
                p = Cheater_Loaded(name)
            else:
                p = Cheater_Swapper(name)
        else:
           p = Player(name)
        return p
    
    def play_hand(self, player):
        print("1...")
        sleep(1)
        print("2...")
        sleep(1)
        print("3...")
        sleep(1)
        player.roll()
    
    def is_cheater(self, player):
        return isinstance(player, Cheater_Swapper) or isinstance(player, Cheater_Loaded)

    def main(self):
        print("Welcome to the super fun dice game!")
        print("-----Player 1-----")
        player1 = self.make_player()
        print("-----Player 2-----")
        player2 = self.make_player()
        print("Alright, {} vs {}!!".format(player1.get_name(), player2.get_name()))
        print("*****Begin!*****")
        print("Player 1 Rolling:")
        self.play_hand(player1)
        print("Player 2 Rolling:")
        self.play_hand(player2)
        p1_total = sum(player1.get_dice())
        p2_total = sum(player2.get_dice())
        
        print("{} rolled {}...Total: {}".format(player1.get_name(), player1.get_dice(), p1_total))

        print("{} rolled {}...Total: {}".format(player2.get_name(), player2.get_dice(), p2_total))
        if p1_total == p2_total:
            print("A Draw! :O")
        elif p1_total > p2_total:
            if self.is_cheater(player1):
                print("{} Wins! (But you cheated!)".format(player1.get_name()))
            else:
                print("{} Wins!".format(player1.get_name()))
        else:
            if self.is_cheater(player2):
                print("{} Wins! (But you cheated!)".format(player2.get_name()))
            else:
                print("{} Wins!".format(player2.get_name()))
             

if __name__ == "__main__":
    g = Game()          
