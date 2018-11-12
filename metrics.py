from state import State
import numpy as np
import operator


def hamming(state, goal):

    def find_position(board, number):
        temp = np.where(board.frame == number)
        return tuple(np.concatenate(temp, axis=0))

    score = 0

    for i in range(len(goal)-1):
        goal_position = find_position(goal, i)
        current_position = find_position(state, i)

        distance = tuple(map(operator.sub, goal_position, current_position))

        score += distance
    return score


def manhattan(state, goal):
    new_arr = goal - state
    return len(np.where(new_arr.frame == 0))
