import random

GOAL_STATE = [1, 2, 3, 8, 0, 4, 7, 6, 5]

def get_neighbors(state):
    zero_index = state.index(0)
    neighbors = []
    if zero_index not in [0, 1, 2]:
        up = state[:]
        up[zero_index], up[zero_index - 3] = up[zero_index - 3], up[zero_index]
        neighbors.append(up)
    if zero_index not in [6, 7, 8]:
        down = state[:]
        down[zero_index], down[zero_index + 3] = down[zero_index + 3], down[zero_index]
        neighbors.append(down)
    if zero_index not in [2, 5, 8]:
        right = state[:]
        right[zero_index], right[zero_index + 1] = right[zero_index + 1], right[zero_index]
        neighbors.append(right)
    if zero_index not in [0, 3, 6]:
        left = state[:]
        left[zero_index], left[zero_index - 1] = left[zero_index - 1], left[zero_index]
        neighbors.append(left)
    return neighbors

def h(state):
    h = 0
    for i, value in enumerate(state):
        if value != 0:
            h += abs(i % 3 - GOAL_STATE.index(value) % 3) + abs(i // 3 - GOAL_STATE.index(value) // 3)
    return h

def hill_climbing(state):
    while True:
        neighbors = get_neighbors(state)
        if not neighbors:
            return state
        neighbor_scores = [(h(neighbor), neighbor) for neighbor in neighbors]
        neighbor_scores.sort()
        if neighbor_scores[0][0] >= h(state):
            return state
        state = neighbor_scores[0][1]

if __name__ == '__main__':
    state = [2, 8, 3, 1, 6, 4, 7, 0, 5]
    print("Initial state:", state)
    print("Final state:", hill_climbing(state))
