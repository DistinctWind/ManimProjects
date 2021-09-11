import sys
import os

from numpy import left_shift

sys.path.append(os.getcwd())

from manimlib import *
from utils.imports import *

class Introduction_scene(Scene) :
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
            01110
            00010
            01000
            00100
            """
        )
        self.play(ShowCreation(easy_maze))
        
        poi = Dot().move_to(easy_maze.get_rec(*easy_maze.start))
        self.play(ShowCreation(poi))

        search_order = easy_maze.get_search_order(UP, RIGHT, DOWN, LEFT)
        arrow_group = VGroup()
        def dfs(lin, col) :
            if ((lin, col)==easy_maze.end):
                return True
            for mov_lin, mov_col, direction in search_order :
                nlin = lin+mov_lin
                ncol = col+mov_col
                arrow = easy_maze.get_arrow(lin, col, direction)
                if (easy_maze.judge(nlin, ncol)) :
                    arrow_group.add(arrow)
                    self.play(
                        GrowArrow(arrow),
                        poi.animate.move_to(easy_maze.get_rec(nlin, ncol)),
                        run_time=0.25, rate_func=linear
                    )
                    easy_maze.move_poi(nlin, ncol)
                    if dfs(nlin, ncol) :
                        return True
                    self.play(
                        Uncreate(arrow),
                        poi.animate.move_to(easy_maze.get_rec(lin, col)),
                        run_time=0.25, rate_func=linear
                    )
                    arrow_group.remove(arrow)
            return False
        
        dfs(*easy_maze.start)
        self.wait()
        self.play(FadeOut(arrow_group))
        self.wait()

        title.target=Text("深度优先搜索+最短路径问题", font="msyh").replace(title).scale(1.75)
        
        self.play(MoveToTarget(title))
        self.wait()
        self.play(poi.animate.move_to(easy_maze.get_rec(*easy_maze.start)))
        self.wait()

        path_1 = VGroup(
            easy_maze.get_line(3, 3, LEFT),
            easy_maze.get_line(3, 2, LEFT).shift(0.05*RIGHT),
            easy_maze.get_line(3, 1, DOWN).shift(0.05*RIGHT),
            easy_maze.get_line(4, 1, DOWN).shift(0.05*RIGHT),
        )
        self.play(ShowCreation(path_1))
        self.wait()

        path_2 = VGroup(
            easy_maze.get_line(3, 3, DOWN),
            easy_maze.get_line(4, 3, RIGHT),
            easy_maze.get_line(4, 4, RIGHT),
            easy_maze.get_line(4, 5, UP),
            easy_maze.get_line(3, 5, UP),
            easy_maze.get_line(2, 5, UP),
            easy_maze.get_line(1, 5, LEFT),
            easy_maze.get_line(1, 4, LEFT),
            easy_maze.get_line(1, 3, LEFT),
            easy_maze.get_line(1, 2, LEFT),
            easy_maze.get_line(1, 1, DOWN),
            easy_maze.get_line(2, 1, DOWN),
            easy_maze.get_line(3, 1, DOWN),
            easy_maze.get_line(4, 1, DOWN)
        ).set_color(RED)
        self.play(ShowCreation(path_2))
        self.wait()
        return super().construct()

class Depth_first_search_for_the_shortest_way(Scene):
    def construct(self):
        maze = Maze(5, 5)
        maze.set_start(3, 3)
        maze.set_end(5, 1)
        maze.set_bar_by_str(
            """
            00000
            01110
            00010
            01000
            00100
            """
        )
        return super().construct()

class trying2(Scene) :
    def construct(self):
        arrow = Arrow()
        self.play(GrowArrow(arrow))
        self.wait()
        self.play(GrowArrow(arrow), rate_func=eat_it_back)

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