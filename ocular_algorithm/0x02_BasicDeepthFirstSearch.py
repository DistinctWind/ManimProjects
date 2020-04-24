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
        self.add(easy_maze)
        self.wait(2)

        