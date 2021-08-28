# %%
from sys import intern
from kaggle_environments import evaluate, make, utils
import random
import numpy as np
import pandas as pd

# %%
env = make("connectx", debug=True)
env.render()

# %%
print(list(env.agents))

# %%
env.run(["random", "random"])

# %%
env.render(mode="ipython")

# %%
# Selects random valid column
def agent_random(obs, config):
    valid_moves = [col for col in range(config.columns) if obs.board[col] == 0]
    return random.choice(valid_moves)

# Selects middle column
def agent_middle(obs, config):
    return config.columns//2

# Selects leftmost valid column
def agent_leftmost(obs, config):
    valid_moves = [col for col in range(config.columns) if obs.board[col] == 0]
    print(random.choice(valid_moves))
    return valid_moves[0]


# %%
# Agents play one game round
env.run([agent_random, agent_middle])
# Show the game
env.render(mode="ipython")

# %%
# Agents play one game round
env.run([agent_random, agent_leftmost])
# Show the game
env.render(mode="ipython")

# %%
# Selects fill cols
def fill_cols(obs, config):
    valid_moves = [col for col in range(config.columns) if obs.board[col] == 0]
    grid = np.array(obs.board).reshape(config.rows, config.columns)
    a = np.array(np.where((grid[5, :] == 1) & (grid[4, :] == 0)))

    if a.size == 0:
        b = random.choice(valid_moves)
    else:
        b = valid_moves[a[0][0]]
    return b
   
    # return random.choice(valid_moves)

# %%
# Agents play one game round
env.run([agent_random, fill_cols])
# Show the game
env.render(mode="ipython")













# %%
# Agents play one game round
env.run([agent_leftmost, agent_random])
# Show the game
env.render(mode="ipython")

# %%
# Agents play one game round
env.run([agent_middle, agent_random])
# Show the game
env.render(mode="ipython")





