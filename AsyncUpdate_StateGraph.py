from Nash import *
import matplotlib.pyplot as plt
import networkx as nx

__author__ = 'Chirag'


def play_game(G, game, i, j):
    if game.nash.__len__() == 0:
        print("game has no nash equilibrium")
        return
    else:
        for n in game.nash:
            print("({},{})".format(n.x,n.y))

    i_0 = i
    j_0 = j
    count = 0

    player_one_turn = True

    while game.is_nash(i_0, j_0) == False and count < 20:
        if player_one_turn:
            i = Player.B_1(j_0, game.payoff)
            player_one_turn = False
        else:
            j = Player.B_2(i_0, game.payoff)
            player_one_turn = True
        G.add_edge((i_0, j_0), (i, j))
        i_0 = i
        j_0 = j

        count += 1

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

game.show_payoff()
game.find_nash()

G = nx.DiGraph()

for i in range(5):
    for j in range(5):
        play_game(G, game, i, j)

nx.draw(G, pos=nx.spring_layout(G), with_labels=True, scale=10, center=(0,0))
plt.show()
