from gym.envs.registration import register

register(
        id='Maze-v0',
        entry_point='envs.gym:MazeEnv',
        max_episode_steps=50,
        reward_threshold=-3.75,
        kwargs={}
)

register(
        id='ACRandMaze-v0',
        entry_point='envs.gym:ACRandMaze0S40Env',
        max_episode_steps=50,
        reward_threshold=-3.75,
        kwargs={}
)

register(
        id='Kitchen-v0',
        entry_point='envs.gym:KitchenEnv',
        max_episode_steps=50,
        reward_threshold=-3.75,
        kwargs={}
)