from gym.envs.registration import register

register(
        id='Maze-v0',
        entry_point='envs.gym:ACRandMaze0S40Env',
        max_episode_steps=800,
        kwargs={}
)

register(
        id='Kitchen-v0',
        entry_point='envs.gym:KitchenEnv',
        max_episode_steps=280,
        kwargs={}
)