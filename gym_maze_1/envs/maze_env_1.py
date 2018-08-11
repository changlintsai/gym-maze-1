import gym
from gym import spaces
from gym.utils import seeding
from graphics import *
import numpy as np


class MazeEnv1(gym.Env):
    def __init__(self):
        self.vertical_0 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.vertical_1 = [0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1]  # from top to bottom
        self.vertical_2 = [0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0]
        self.vertical_3 = [0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0]
        self.vertical_4 = [0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0]
        self.vertical_5 = [0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0]
        self.vertical_6 = [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0]
        self.vertical_7 = [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
        self.vertical_8 = [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
        self.vertical_9 = [0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
        self.vertical_10 = [0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0]
        self.vertical_11 = [0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0]
        self.vertical_12 = [0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
        self.vertical_13 = [0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0]
        self.vertical_14 = [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0]
        self.vertical_15 = [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0]
        self.vertical_16 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.vertical_wall = [self.vertical_0, self.vertical_1, self.vertical_2, self.vertical_3, self.vertical_4,
                              self.vertical_5, self.vertical_6, self.vertical_7, self.vertical_8, self.vertical_9,
                              self.vertical_10, self.vertical_11, self.vertical_12, self.vertical_13, self.vertical_14,
                              self.vertical_15, self.vertical_16]

        self.horizontal_0 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.horizontal_1 = [0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0]  # from left to right
        self.horizontal_2 = [0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0]
        self.horizontal_3 = [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0]
        self.horizontal_4 = [0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0]
        self.horizontal_5 = [0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0]
        self.horizontal_6 = [0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0]
        self.horizontal_7 = [0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0]
        self.horizontal_8 = [0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0]
        self.horizontal_9 = [0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0]
        self.horizontal_10 = [0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0]
        self.horizontal_11 = [0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0]
        self.horizontal_12 = [0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0]
        self.horizontal_13 = [0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0]
        self.horizontal_14 = [0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0]
        self.horizontal_15 = [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0]
        self.horizontal_16 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.horizontal_wall = [self.horizontal_0, self.horizontal_1, self.horizontal_2, self.horizontal_3,
                                self.horizontal_4, self.horizontal_5, self.horizontal_6, self.horizontal_7,
                                self.horizontal_8, self.horizontal_9, self.horizontal_10, self.horizontal_11,
                                self.horizontal_12, self.horizontal_13, self.horizontal_14, self.horizontal_15,
                                self.horizontal_16]

        self.bot = Circle(Point(30, 630), 15)  # create bot
        self.bot.setOutline(color_rgb(255, 255, 255))
        self.bot.setWidth(3)

        self.x_move = 0
        self.y_move = 0
        self.x_coord = 30
        self.y_coord = 630
        self.virtual_x = int((self.x_coord - 30) / 40)
        self.virtual_y = int((self.y_coord - 30) / 40)
        self.above_wall = self.horizontal_wall[self.virtual_y][self.virtual_x]
        self.below_wall = self.horizontal_wall[self.virtual_y + 1][self.virtual_x]
        self.right_wall = self.vertical_wall[self.virtual_x + 1][self.virtual_y]
        self.left_wall = self.vertical_wall[self.virtual_x][self.virtual_y]

        self.action_space = spaces.Discrete(4)  # if action==0, up; 1, down; 2, left; 3, right
        self.observation_space = spaces.Box(low=0, high=15, shape=(2,))  # not sure what to put as observation, yet

        self.step_count = 0
        # self.step_max = 1000
        self.observation = np.array(
            [0, 15])  # not sure if this is right(observe four walls: U, R, B, L))(virtual coords)

        self.seed()
        self.reset()

    def seed(self, seed=None):
        self.nu_random, seed = seeding.np_random(seed)
        return [seed]

    def step(self, action):
        assert self.action_space.contains(action)

        self.x_move = 0
        self.y_move = 0
        done = False
        reward = 0

        if action == 0 and self.above_wall == 0:  # up
            self.y_move = -40
        elif action == 1 and self.below_wall == 0:  # down
            self.y_move = 40
        elif action == 2 and self.left_wall == 0:  # left
            self.x_move = -40
        elif action == 3 and self.right_wall == 0:  # right
            self.x_move = 40

        self.x_coord += self.x_move
        self.y_coord += self.y_move
        self.virtual_x = int((self.x_coord - 30) / 40)
        self.virtual_y = int((self.y_coord - 30) / 40)
        self.above_wall = self.horizontal_wall[self.virtual_y][self.virtual_x]
        self.below_wall = self.horizontal_wall[self.virtual_y + 1][self.virtual_x]
        self.right_wall = self.vertical_wall[self.virtual_x + 1][self.virtual_y]
        self.left_wall = self.vertical_wall[self.virtual_x][self.virtual_y]

        self.bot.move(self.x_move, self.y_move)

        # this part could contain a bug, the boolean statements could be imprecise
        if self.x_coord == 30 or self.x_coord == 630 or self.y_coord == 30 or self.y_coord == 630:
            reward = 0.1
        elif self.x_coord == 70 or self.x_coord == 590 or self.y_coord == 70 or self.y_coord == 590:
            reward = 0.2
        elif self.x_coord == 110 or self.x_coord == 550 or self.y_coord == 110 or self.y_coord == 550:
            reward = 0.3
        elif self.x_coord == 150 or self.x_coord == 510 or self.y_coord == 150 or self.y_coord == 510:
            reward = 0.4
        elif self.x_coord == 190 or self.x_coord == 470 or self.y_coord == 190 or self.y_coord == 470:
            reward = 0.5
        elif self.x_coord == 230 or self.x_coord == 430 or self.y_coord == 230 or self.y_coord == 430:
            reward = 0.6
        elif self.x_coord == 270 or self.x_coord == 390 or self.y_coord == 270 or self.y_coord == 390:
            reward = 0.7
        elif self.x_coord == 310 or self.x_coord == 350 or self.y_coord == 310 or self.y_coord == 350:
            reward = 0.8
            done = True

        self.observation = np.array([self.virtual_x, self.virtual_y])
        self.step_count += 1
        '''if self.step_count > self.step_max:
            done = True'''

        print(self.step_count)

        return self.observation, reward, done

    def draw_map(self):
        """mouseMap = GraphWin("2017 high school maze", 1000, 700)  # create window\canvas
        mouseMap.setBackground(color_rgb(50, 50, 50))
        bot = Circle(Point(30, 630), 15)  # create bot
        bot.setOutline(color_rgb(255, 255, 255))
        bot.setWidth(3)
        bot.draw(mouseMap)"""

        for j in range(17):
            for i in range(16):
                if self.vertical_wall[j][i] == 1:
                    line = Line(Point(10 + j * 40, 10 + i * 40), Point(10 + j * 40, 50 + i * 40))
                    line.setWidth(3)
                    line.setOutline(color_rgb(255, 255, 0))
                    line.draw(self.mouseMap)

        for k in range(17):
            for l in range(16):
                if self.horizontal_wall[k][l] == 1:
                    line = Line(Point(10 + l * 40, 10 + k * 40), Point(50 + l * 40, 10 + k * 40))
                    line.setWidth(3)
                    line.setOutline(color_rgb(255, 255, 0))
                    line.draw(self.mouseMap)

    def close_map(self):
        self.mouseMap.close()

    def reset(self):
        self.x_move = 0
        self.y_move = 0
        self.x_coord = 30
        self.y_coord = 630
        self.step_count = 0
        self.observation = np.array([0, 15])
        self.mouseMap = GraphWin("2017 high school maze", 1000, 700)  # create window\canvas
        self.mouseMap.setBackground(color_rgb(50, 50, 50))

        self.bot = Circle(Point(30, 630), 15)  # create bot
        self.bot.setOutline(color_rgb(255, 255, 255))
        self.bot.setWidth(3)
        self.bot.draw(self.mouseMap)


        return self.observation # don't know why
