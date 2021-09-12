from re import search
import sys
import os
import random

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
                    easy_maze.role_back()
                    self.play(
                        FadeOut(arrow, scale=0.5),
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
        self.play(FadeOut(title), FadeOut(path_1), FadeOut(path_2))
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
        self.add(maze)
        poi=Dot().move_to(maze.get_rec(*maze.start))
        self.add(poi)

        arrow_group=VGroup()
        path_and_tag_group=VGroup().to_corner(UL)
        search_order = maze.get_search_order(UP, RIGHT, DOWN, LEFT)
        cnt=0
        def dfs_for_the_shortest_way(lin, col, step):
            if ((lin, col)==maze.end):
                nonlocal cnt
                cnt = cnt+1
                tag=Text(
                    '#'+str(cnt)+" step="+str(step), color=BLUE_A,
                    t2c={
                        "step=": YELLOW
                    }
                ).next_to(arrow_group, UP)
                path_and_tag=VGroup(
                    arrow_group.deepcopy(),
                    tag
                )
                self.add(path_and_tag)
                self.play(Write(tag))
                path_and_tag.target=path_and_tag.copy().scale(0.25).to_corner(DL)
                self.play(MoveToTarget(path_and_tag))
                path_and_tag_group.add(path_and_tag)
                self.play(
                    # path_and_tag.animate.scale(0.25),
                    path_and_tag_group.animate.arrange(DOWN).to_corner(UL)
                )
                self.wait()
            for mov_lin, mov_col, direction in search_order:
                nlin=lin+mov_lin
                ncol=col+mov_col
                arrow=maze.get_arrow(lin, col, direction)
                if (maze.judge(nlin, ncol)) :
                    arrow_group.add(arrow)
                    self.play(
                        GrowArrow(arrow),
                        poi.animate.move_to(maze.get_rec(nlin, ncol)),
                        run_time=0.25
                    )
                    maze.move_poi(nlin, ncol)
                    dfs_for_the_shortest_way(nlin, ncol, step+1)
                    maze.role_back()
                    self.play(
                        FadeOut(arrow, scale=0.5),
                        poi.animate.move_to(maze.get_rec(lin, col)),
                        run_time=0.25
                    )
                    arrow_group.remove(arrow)
        dfs_for_the_shortest_way(*maze.start, 0)
        self.play(FadeOut(maze), FadeOut(poi))
        # path_and_tag_group.target=path_and_tag_group.copy().arrange(RIGHT).scale(4).move_to([0, 0, 0])
        self.play(
            path_and_tag_group.animate.arrange(RIGHT).scale(3.5).move_to(ORIGIN)
        )
        self.wait()

        bingo=Text("✓", font='msyh')
        bingo.next_to(path_and_tag_group[2], DOWN, buff=MED_SMALL_BUFF)
        bingo.scale(1.5)
        bingo.set_color(RED)
        self.play(Write(bingo))
        return super().construct()

class Breadth_first_search(Scene):
    def construct(self):
        title = Text("广度优先搜索", font='msyh')
        self.play(Write(title))
        self.wait()
        subtitle = Text("广搜", font='msyh').scale(0.75).set_color(GREY).next_to(title, DOWN)
        self.play(Write(subtitle))

        self.play(
            title.animate.to_edge(UP),
            FadeOut(subtitle, DOWN, scale=0.5)
        )
        
        maze = Maze(3, 5)
        maze.set_start(1, 1)
        maze.set_end(3, 5)
        poi = Dot().move_to(maze.get_rec(*maze.start))
        self.play(ShowCreation(maze), FadeIn(poi, scale=0.5))
        q = Queue()
        q.put(data_pack(0, *maze.start))
        search_order = maze.get_search_order(UP, RIGHT, DOWN, LEFT)
        opa=0.1
        def bfs():
            maze.add_path_poi_list(*maze.start)
            self.play(maze.get_rec(*maze.start).animate.set_fill(BLUE, opacity=opa), run_time=0.25)
            while not q.empty():
                now = q.pop()
                arrow_group = VGroup()
                self.play(poi.animate.move_to(maze.get_rec(now.lin, now.col)))
                print(str(now.lin)+' '+str(now.col)+':')
                if ((now.lin, now.col)==maze.end):
                    break
                for mov_lin, mov_col, direction in search_order:
                    nlin, ncol = now.lin+mov_lin, now.col+mov_col
                    arrow = maze.get_arrow(now.lin, now.col, direction)
                    if (maze.judge(nlin, ncol)):
                        arrow_group.add(arrow)
                        maze.add_path_poi_list(nlin, ncol)
                        self.play(
                            poi.animate.move_to(maze.get_rec(nlin, ncol)),
                            maze.get_rec(nlin, ncol).animate.set_fill(BLUE, opacity=opa+(now.step+1)*0.1),
                            GrowArrow(arrow),
                            run_time=0.25
                        )
                        q.put(data_pack(now.step+1, nlin, ncol))
                        self.play(poi.animate.move_to(maze.get_rec(now.lin, now.col)), run_time=0.25)
                self.play(FadeOut(arrow_group, scale=0.5), run_time=0.25)

        bfs()
        for rec in maze.rec_list:
            rec.target=rec.copy().set_fill(BLUE, opacity=0)
        self.play(
            FadeOut(poi, scale=0.5),
            *[MoveToTarget(__rec) for __rec in maze.rec_list]
        )

        subtitle = Text("（理想状况）", font='msyh').scale(0.75).set_color(GREY)
        subtitle.next_to(title, DOWN, buff=SMALL_BUFF)
        self.play(Write(subtitle))

        change_lists = [
            [
                maze.get_rec(1, 1),
            ],
            [
                maze.get_rec(1, 2),
                maze.get_rec(2, 1),
            ],
            [
                maze.get_rec(1, 3),
                maze.get_rec(2, 2),
                maze.get_rec(3, 1),
            ],
            [
                maze.get_rec(1, 4),
                maze.get_rec(2, 3),
                maze.get_rec(3, 2),
            ],
            [
                maze.get_rec(1, 5),
                maze.get_rec(2, 4),
                maze.get_rec(3, 3),
            ],
            [
                maze.get_rec(2, 5),
                maze.get_rec(3, 4),
            ],
            [
                maze.get_rec(3, 5),
            ]
        ]
        opa=0.3
        for change_list in change_lists:
            self.play(*[__rec.animate.set_fill(BLUE, opacity=opa) for __rec in change_list])
            opa+=0.1
        return super().construct()

class Queue_introduction(Scene):
    def construct(self):
        title = Text("队列", font='msyh')
        self.play(Write(title))
        self.wait()
        self.play(title.animate.to_edge(UP))
        self.wait()
        
        circle_list = [
            Circle()\
                .set_color(get_random_color())\
                .set_fill(get_random_color(), opacity=random.random())\
                .to_edge(RIGHT)\
                for i in range(5)
        ]
        circle_queue = VirtualizedQueue()
        
        for circle in circle_list:
            self.play(
                FadeIn(circle_queue.put(circle).to_edge(RIGHT), scale=0.75),
                circle_queue.animate.arrange(RIGHT)
            )
        
        new_circle = Circle()\
            .set_color(get_random_color())\
            .set_fill(get_random_color(), opacity=random.random())\
            .to_edge(RIGHT)

        def pop_and_reset():
            self.play(
                FadeOut(circle_queue[0], shift=LEFT)
            )
            circle_queue.pop()
            self.play(
                circle_queue.animate.move_to(ORIGIN)
            )
            self.wait()
            
        pop_and_reset()
        pop_and_reset()
        self.play(
            FadeIn(circle_queue.put(new_circle).to_edge(RIGHT), scale=0.75),
            circle_queue.animate.arrange(RIGHT)
        )
        pop_and_reset()
        pop_and_reset()
        pop_and_reset()
        pop_and_reset()
        return super().construct()

class Depth_first_search(Scene):
    def construct(self):
        title = Text("深度优先搜索", font='msyh')
        title.to_edge(UP)
        self.play(Write(title))
        
        maze = Maze(3, 5)
        maze.set_start(1, 1)
        maze.set_end(3, 5)
        self.play(ShowCreation(maze))
        
        poi = Dot().move_to(maze.get_rec(*maze.start))
        self.play(FadeIn(poi, scale = 0.5))
        search_order = maze.get_search_order(RIGHT, DOWN, LEFT, UP)

        cnt=0
        def dfs(lin, col):
            if ((lin, col)==maze.end):
                nonlocal cnt
                cnt=cnt+1
                print(cnt)
                return
            for mov_lin, mov_col, direction in search_order:
                nlin, ncol = lin+mov_lin, col+mov_col
                arrow = maze.get_arrow(lin, col, direction)
                if (maze.judge(nlin, ncol)):
                    self.play(
                        poi.animate.move_to(maze.get_rec(nlin, ncol)),
                        GrowArrow(arrow), run_time=0.25
                    )
                    maze.move_poi(nlin, ncol)
                    dfs(nlin, ncol)
                    maze.role_back()
                    self.play(
                        poi.animate.move_to(maze.get_rec(lin, col)),
                        FadeOut(arrow), run_time=0.25
                    )
        dfs(*maze.start)
        
        return super().construct()

class trying5(Scene):
    def construct(self):
        # circle = Circle()
        # self.add(circle)
        for i in range(5):
            circle = Circle()\
            .set_color(get_random_color())\
            .set_fill(get_random_color(), opacity=random.random())
            self.play(FadeIn(circle, scale=random.random()*2))
        return super().construct()

class trying4(Scene):
    def construct(self):
        virtualized_queue=VirtualizedQueue()
        # data_pack = VirtualizedDataPack(1, 2, 3)
        data_packs = VGroup(*[
            VirtualizedDataPack(__step, 2, 5) for __step in range(1, 6)
        ]).arrange(RIGHT)
        # self.play(FadeIn(data_pack, scale=0.75))
        # self.play(ShowCreation(data_packs))

        for data_pack in data_packs:
            data_pack.move_to(ORIGIN)
            self.play(FadeIn(virtualized_queue.put(data_pack), scale=0.75))
            self.play(virtualized_queue.animate.arrange(RIGHT))
        return super().construct()

class trying3(Scene) :
    def construct(self):
        square = Square()
        square.set_fill(BLUE, opacity=1)
        self.play(ShowCreation(square))
        
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