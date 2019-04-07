import sys

import numpy as np
from gym import utils
from gym.envs.toy_text import discrete
from six import StringIO

LEFT = 0
DOWN = 1
RIGHT = 2
UP = 3

MAPS = {
    "4x4": [
        "S   ",
        " W W",
        "   W",
        "W  G"
    ],
    "8x8": [
        "S       ",
        "        ",
        "   W    ",
        "     W  ",
        "   W    ",
        " WW   W ",
        " W  W W ",
        "   W   G"
    ],
    "20x20": [
        "S      WWW          ",
        "                WW  ",
        "   W       WW       ",
        "     W          WW  ",
        "     W          WW  ",
        "     W          WW  ",
        "        W       WW  ",
        "     W    WW    WW  ",
        "     W          WW  ",
        "     W          WW  ",
        "           WWWWWWW  ",
        "WWWW W          WW  ",
        "     W    WWW   WW  ",
        "                WW  ",
        "     W      W   WW  ",
        "     W          WW  ",
        "           W        ",
        " WW   W    W     W  ",
        " WW W W             ",
        "   W     W    WW W G"
    ]
}


# Updated from: 
# https://github.com/openai/gym/blob/master/gym/envs/toy_text/frozen_lake.py
def generate_random_map(size=8, p=0.8):
    """Generates a random valid map (one that has a path from start to goal)
    :param size: size of each side of the grid
    :param p: probability that a tile is wall
    """
    valid = False

    # BFS to check that it's a valid path.
    def is_valid(arr, r=0, c=0):
        if arr[r][c] == 'G':
            return True

        tmp = arr[r][c]
        arr[r][c] = "#"

        # Recursively check in all four directions.
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for x, y in directions:
            r_new = r + x
            c_new = c + y
            if r_new < 0 or r_new >= size or c_new < 0 or c_new >= size:
                continue

            if arr[r_new][c_new] not in '#W':
                if is_valid(arr, r_new, c_new):
                    arr[r][c] = tmp
                    return True

        arr[r][c] = tmp
        return False

    while not valid:
        p = min(1, p)
        res = np.random.choice([' ', 'W'], (size, size), p=[p, 1-p])
        res[0][0] = 'S'
        res[-1][-1] = 'G'
        valid = is_valid(res)
    return ["".join(x) for x in res]


# Adapted from https://github.com/openai/gym/blob/master/gym/envs/toy_text/frozen_lake.py
# This is a modified environment where rewards are given for every step in addition to on finding a goal.
# This reward shaping makes the problem easier for the learner to solve.
class GridworldEnv(discrete.DiscreteEnv):
    """
    The grid world is described using a matrix like the following

        S
         W W
           W
        W  G

    S   : starting point, safe
    ' ' : frozen surface, safe (space)
    W   : wall
    G   : goal, safe

    The episode ends when you reach the goal.
    You receive a reward of 1 if you reach the goal, -0.25 for hitting a wall, and a small negative reward otherwise.
    
    The wall and step rewards are configurable when creating an instance of the problem.

    """

    metadata = {'render.modes': ['human', 'ansi']}

    def __init__(self, desc=None, map_name="4x4", rewarding=True, step_reward=-0.1, wall_reward=-0.2):
        if desc is None and map_name is None:
            raise ValueError('Must provide either desc or map_name')
            #desc = generate_random_map()
        elif desc is None:
            desc = MAPS[map_name]

        self.desc = desc = np.asarray(desc, dtype='c')
        self.nrow, self.ncol = nrow, ncol = desc.shape
        self.reward_range = (0, 1)
        self.step_reward = step_reward
        self.wall_reward = wall_reward
        self.rewarding = rewarding

        nA = 4
        nS = nrow * ncol

        isd = np.array(desc == b'S').astype('float64').ravel()
        isd /= isd.sum()

        P = {s: {a: [] for a in range(nA)} for s in range(nS)}

        def to_s(row, col):
            return row * ncol + col

        def inc(row, col, a):
            if a == 0:  # left
                col = max(col - 1, 0)
            elif a == 1:  # down
                row = min(row + 1, nrow - 1)
            elif a == 2:  # right
                col = min(col + 1, ncol - 1)
            elif a == 3:  # up
                row = max(row - 1, 0)
            return (row, col)

        for row in range(nrow):
            for col in range(ncol):
                s = to_s(row, col)
                for a in range(4):
                    li = P[s][a]
                    letter = desc[row, col]
                    if letter in b'GW':
                        li.append((1.0, s, 0, True))
                    else:
                        newrow, newcol = inc(row, col, a)
                        newstate = to_s(newrow, newcol)
                        newletter = desc[newrow, newcol]
                        done = bytes(newletter) in b'GW'
                        rew = float(newletter == b'G')
                        if self.rewarding:
                            if newletter == b' ':
                                rew = self.step_reward
                            elif newletter == b'W':
                                rew = self.wall_reward
                        li.append((1.0, newstate, rew, done))

        super(GridworldEnv, self).__init__(nS, nA, P, isd)

    def render(self, mode='human'):
        outfile = StringIO() if mode == 'ansi' else sys.stdout

        row, col = self.s // self.ncol, self.s % self.ncol
        desc = self.desc.tolist()
        desc = [[c.decode('utf-8') for c in line] for line in desc]
        desc[row][col] = utils.colorize(desc[row][col], "red", highlight=True)
        if self.lastaction is not None:
            outfile.write("  ({})\n".format(["Left", "Down", "Right", "Up"][self.lastaction]))
        else:
            outfile.write("\n")
        outfile.write("\n".join(''.join(line) for line in desc) + "\n")

        if mode != 'human':
            return outfile

    def colors(self):
        return {
            b'S': 'green',
            b' ': 'skyblue',
            b'W': 'black',
            b'G': 'gold',
        }

    def directions(self):
        return {
            3: '⬆',
            2: '➡',
            1: '⬇',
            0: '⬅'
        }

    def new_instance(self):
        return GridworldEnv(desc=self.desc, rewarding=self.rewarding, step_reward=self.step_reward,
                            wall_reward=self.wall_reward)
