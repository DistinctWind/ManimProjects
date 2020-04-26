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

        poi = Dot().move_to(hard_maze.get_rec(*hard_maze.start))
        self.play(ShowCreation(poi))
        hard_maze.setup_map()
        dir_set = hard_maze.get_search_order(RIGHT, DOWN, LEFT, UP)
        def search(lin, col) :
            if (lin, col)==hard_maze.end :
                return True
            for mov_lin, mov_col, direction in dir_set :
                nlin = lin+mov_lin
                ncol = col+mov_col
                arrow = hard_maze.get_arrow(lin, col, direction)
                if hard_maze.judge(nlin, ncol) :
                    self.play(ShowCreation(arrow), poi.move_to, hard_maze.get_rec(nlin, ncol).get_center(), run_time=0.25, rate_func=linear)
                    hard_maze.move_poi(nlin, ncol)
                    if search(nlin, ncol) :
                        return True
                    hard_maze.role_back()
                    self.play(Uncreate(arrow, rate_func=lambda t: linear(1-t)), ApplyMethod(poi.move_to, hard_maze.get_rec(lin, col).get_center(), rate_func=linear), run_time=0.25)
            return False
        
        print(search(*hard_maze.start))
