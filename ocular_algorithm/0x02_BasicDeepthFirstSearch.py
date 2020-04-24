from manimlib.imports import *
from project.utils.imports import *

class Begin_introduction(Scene) :
    def construct(self) :
        easy_maze = Maze(3, 5)
        easy_maze.set_start(1, 1)
        easy_maze.set_end(3, 5)
        easy_maze.set_bar_by_str(
            """
            01100
            00010
            11000
            """
        )
        self.play(ShowCreation(easy_maze), rate_func=linear)
        self.wait(2)

        hard_maze = Maze(9, 16)
        hard_maze.set_start(1, 1)
        hard_maze.set_end(9, 16)

        