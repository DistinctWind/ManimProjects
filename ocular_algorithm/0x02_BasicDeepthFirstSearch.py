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

        hard_maze = Maze(9, 16, scale_factor=0.75)
        hard_maze.set_start(1, 1)
        hard_maze.set_end(9, 16)
        hard_maze.set_bar_by_str(
            """
            0001101101001010
            0100000001101000
            0101110100001011
            0100010010100000
            0111101010101111
            0010001110001000
            1000100010111010
            0010101011100010
            1110101000001010
            """
        )
        self.play(ReplacementTransform(easy_maze, hard_maze))
        self.wait(2)