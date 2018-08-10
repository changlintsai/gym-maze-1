from gym.envs.registration import register

register(
    id='maze-v1',
    entry_point='gym_maze_1.envs:MazeEnv1',
)
