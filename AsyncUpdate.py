from Nash import *
import matplotlib.pyplot as plt

__author__ = 'Chirag'


def play_game(game, i, j):
    if game.nash.__len__() == 0:
        print("game has no nash equilibrium")
        return
    else:
        for n in game.nash:
            print("({},{})".format(n.x,n.y))

    player1 = []
    player2 = []
    i_0 = i
    j_0 = j
    player1.append(game.payoff[i_0][j_0].x)
    player2.append(game.payoff[i_0][j_0].y)
    count = 0

    player_one_turn = True

    while game.is_nash(i_0, j_0) == False and count < 20:
        if player_one_turn:
            i = Player.B_1(j_0, game.payoff)
            player_one_turn = False
        else:
            j = Player.B_2(i_0, game.payoff)
            player_one_turn = True
        i_0 = i
        j_0 = j
        player1.append(game.payoff[i_0][j_0].x)
        player2.append(game.payoff[i_0][j_0].y)
        count += 1

    player1.append(game.payoff[i_0][j_0].x)
    player2.append(game.payoff[i_0][j_0].y)
    count += 1
    x = range(count+1)
    return player1, player2, x


game = Nash()
# payoff matrix of "oscillating game"
game.payoff = [
    [Tuple(6, 7), Tuple(5, 2), Tuple(5, 8), Tuple(0, 2), Tuple(0, 1)],
    [Tuple(1, 1), Tuple(3, 2), Tuple(5, 2), Tuple(1, 3), Tuple(5, 1)],
    [Tuple(1, 7), Tuple(2, 7), Tuple(1, 7), Tuple(4, 8), Tuple(8, 1)],
    [Tuple(0, 1), Tuple(4, 7), Tuple(8, 2), Tuple(3, 0), Tuple(0, 3)],
    [Tuple(8, 4), Tuple(3, 2), Tuple(1, 4), Tuple(9, 6), Tuple(1, 0)]
]

# payoff matrix of "normal game"
# game.payoff = [
#     [Tuple(9, 8), Tuple(3, 0), Tuple(4, 2), Tuple(1, 1), Tuple(0, 2)],
#     [Tuple(3, 6), Tuple(9, 3), Tuple(8, 5), Tuple(3, 8), Tuple(9, 6)],
#     [Tuple(8, 9), Tuple(4, 7), Tuple(5, 3), Tuple(4, 4), Tuple(6, 5)],
#     [Tuple(1, 7), Tuple(5, 8), Tuple(9, 4), Tuple(1, 2), Tuple(3, 3)],
#     [Tuple(1, 7), Tuple(8, 8), Tuple(0, 9), Tuple(0, 5), Tuple(9, 3)]
# ]

# payoff matrix of "oscillating game" with multiple nash
# game.payoff = [
#     [Tuple(4, 4), Tuple(5, 1), Tuple(9, 6), Tuple(5, 3), Tuple(2, 7)],
#     [Tuple(0, 2), Tuple(1, 7), Tuple(8, 0), Tuple(9, 6), Tuple(0, 5)],
#     [Tuple(5, 0), Tuple(7, 6), Tuple(2, 4), Tuple(2, 2), Tuple(1, 4)],
#     [Tuple(6, 2), Tuple(7, 6), Tuple(8, 1), Tuple(7, 3), Tuple(1, 8)],
#     [Tuple(9, 7), Tuple(7, 1), Tuple(7, 5), Tuple(0, 1), Tuple(9, 1)]
# ]
game.show_payoff()
game.find_nash()

plt.figure(1)
k = 1
for i in range(5):
    for j in range(5):
        plt.subplot(5, 5, k)
        player1, player2, x = play_game(game, i, j)
        player1_curve, = plt.plot(x, player1, label="player 1")
        player2_curve, = plt.plot(x, player2, label="player 2")
        plt.grid()
        k += 1
plt.show()