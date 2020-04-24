from manimlib.imports import *
from project.utils.imports import *

class Begin_introduction(Scene) :
    def construct(self) :
        easy_maze = Maze(3, 5)
        easy_maze.set_start(1, 1)
        easy_maze.set_end(3, 5)
        easy_maze_bar_list = [
            (1, 2), (1, 3), (2, 4), (3, 2),
        ]
        for lin, col in easy_maze_bar_list :
            easy_maze.set_bar(lin, col)
        self.play(ShowCreation(easy_maze), rate_func=linear)
        self.wait(2)

        hard_maze = Maze(9, 16)