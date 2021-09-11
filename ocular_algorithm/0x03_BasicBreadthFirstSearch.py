import sys
import os

sys.path.append(os.getcwd())

from manimlib import *
from utils.imports import *

class IntroductionScene(Scene) :
    def construct(self):
        easy_maze = Maze(5, 5)
        easy_maze.set_start(3, 3)
        easy_maze.set_end(5, 1)
        easy_maze.set_bar_by_str(
            """
            00000
            00110
            00010
            01000
            00000
            """
        )
        self.play(ShowCreation(easy_maze))
        return super().construct()

class trying(Scene) :
    def construct(self):
        maze=Maze(5, 5)
        maze.set_start(3, 3)
        maze.set_end(1, 1)
        self.play(ShowCreation(maze))
        self.wait()

        poi = Dot(color=RED).move_to(maze.get_rec(*maze.start))
        self.play(FadeIn(poi, scale=0.5))

        arrow = maze.get_arrow(1, 2, DOWN)
        self.play(DrawBorderThenFill(arrow))
        return super().construct()