from state import State
import numpy as np
import operator


def hamming(state, goal):
    new_arr = state.frame - goal
    new_arr[-1][-1] = 0
    zero_pos = np.where(new_arr != 0)
    score = len(zero_pos[0])
    return score + state.rec, state


def manhattan(state, goal):
    def find_position(board, number):
        temp = np.where(board == number)
        return tuple(np.concatenate(temp, axis=0))

    score = 0

    for i in range(1, goal.size):
        goal_position = find_position(goal, i)
        current_position = find_position(state.frame, i)

        distance = sum(map(abs, map(operator.sub, goal_position, current_position)))

        score += distance
    return score + state.rec, state

