import sys
import os

sys.path.append(os.getcwd())

from manimlib import *
from utils.imports import *

class IntroductionScene(Scene) :
    def construct(self):
        title = Text("深度优先搜索", font="msyh")
        title.to_edge(UP)
        self.play(Write(title))
        easy_maze = Maze(5, 5)
        easy_maze.set_start(3, 3)
        easy_maze.set_end(5, 1)
        easy_maze.set_bar_by_str(
            """
            00000
            00110
            00010
            01000
            00100
            """
        )
        self.play(ShowCreation(easy_maze))
        
        poi = Dot().move_to(easy_maze.get_start(*easy_maze.start))
        self.play(ShowCreation(poi))

        search_order = easy_maze.get_search_order(UP, RIGHT, DOWN, LEFT)
        def dfs(lin, col) :
            if ((lin, col)==easy_maze.end):
                return True
            for mov_lin, mov_col, direction in search_order :
                nlin = lin+mov_lin
                ncol = col+mov_col
                arrow = easy_maze.get_arrow(lin, col, direction)
                if (easy_maze.judge(nlin, ncol)) :
                    self.play(
                        GrowArrow(arrow),
                        poi.animate.move_to(easy_maze.get_rec(nlin, ncol)),
                        run_time=0.25, rate_func=linear
                    )
                    easy_maze.move_poi(nlin, ncol)
                    if dfs(nlin, ncol) :
                        return True
                    
        return super().construct()

class trying2(Scene) :
    def construct(self):
        arrow = Arrow()
        self.play(GrowArrow(arrow))
        self.wait()
        self.play(GrowArrow(arrow, rate_func=eat_it_back))

        square = Square()
        self.play(ShowCreation(square))
        self.wait()
        self.play(ShowCreation(square, rate_func=eat_it_back))
        return super().construct()

class trying1(Scene) :
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