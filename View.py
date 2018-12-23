import matplotlib.pyplot as plt
from Nash import *

__author__ = 'Chirag'


def demo():
    game = Nash()
    game.fill_payoff()
    game.show_payoff()
    game.find_nash()

    if game.nash.__len__() == 0:
        print("game has no nash equilibrium")
        return
    else:
        for n in game.nash:
            print("({},{})".format(n.x,n.y))

    player1 = []
    player2 = []
    i_0 = random.randint(0, 4)
    j_0 = random.randint(0, 4)
    player1.append(game.payoff[i_0][j_0].x)
    player2.append(game.payoff[i_0][j_0].y)
    count = 0
    while game.is_nash(i_0, j_0) == False and count < 20:
        i = Player.B_1(j_0, game.payoff)
        j = Player.B_2(i_0, game.payoff)
        i_0 = i
        j_0 = j
        player1.append(game.payoff[i_0][j_0].x)
        player2.append(game.payoff[i_0][j_0].y)
        count += 1

    player1.append(game.payoff[i_0][j_0].x)
    player2.append(game.payoff[i_0][j_0].y)
    count += 1
    x = range(count+1)
    player1_curve, = plt.plot(x, player1, label="player 1")
    player2_curve, = plt.plot(x, player2, label="player 2")
    plt.legend([player1_curve, player2_curve], ['player 1', 'player 2'])
    plt.xlabel('attempt of game')
    plt.ylabel('payoff')
    plt.grid()
    plt.show()

demo()
