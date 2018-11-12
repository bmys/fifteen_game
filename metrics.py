from state import State
import numpy as np
import operator


def hamming(state, goal):

    def find_position(board, number):
        temp = np.where(board == number)
        return tuple(np.concatenate(temp, axis=0))

    score = 0

    for i in range(len(goal)-1):
        goal_position = find_position(goal, i)
        current_position = find_position(state, i)

        distance = sum(map(operator.sub, goal_position, current_position))

        score += distance
    return score, state


def manhattan(state, goal):
    new_arr = goal - state.frame
    score = len(np.where(new_arr == 0))
    return score, state
