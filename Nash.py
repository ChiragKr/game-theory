from Tuple import *
import Player
import random

__author__ = 'Chirag'


class Nash(object):
    def __init__(self):
        print("computing nash equilibrium")
        self.nash = []
        self.payoff = []
        for i in range(5):
            row = []
            for j in range(5):
                row.append(Tuple(0, 0))
            self.payoff.append(row)

    def fill_payoff(self):
        for i in range(5):
            for j in range(5):
                self.payoff[i][j].x = random.randint(0, 9)
                self.payoff[i][j].y = random.randint(0, 9)

    def show_payoff(self):
        for i in range(5):
            for j in range(5):
                print("({}, {})".format(self.payoff[i][j].x, self.payoff[i][j].y), end="  ")
            print()

    def find_nash(self):
        num = 0
        for i in range(5):
            for j in range(5):
                a = self.payoff[i][j].x
                b = self.payoff[i][j].y
                if self.is_nash(i, j):
                    print("({}, {}) is a Nash equilibrium".format(a, b))
                    self.nash.append(Tuple(a, b))

    def is_nash(self, i,j):
        return Player.B_1(j, self.payoff) == i and Player.B_2(i, self.payoff) == j

# game = Nash()
# game.fill_payoff()
# game.show_payoff()
# game.find_nash()
