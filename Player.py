__author__ = 'Chirag'


def B_1(j, payoff):
    max_index = 0
    for i in range(5):
        if payoff[i][j].x > payoff[max_index][j].x:
            max_index = i
    print("best-response of 1 when 2 plays j="+str(j)+" is " + str(max_index))
    return max_index


def B_2(i, payoff):
    max_index = 0
    for j in range(5):
        if payoff[i][j].y > payoff[i][max_index].y:
            max_index = j
    print("best-response of 2 when 1 plays i="+str(i)+" is " + str(max_index))
    return max_index
