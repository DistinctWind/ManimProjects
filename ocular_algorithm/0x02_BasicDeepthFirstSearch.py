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
                    self.play(
                        ShowCreation(arrow),
                        ApplyMethod(poi.move_to, hard_maze.get_rec(nlin, ncol).get_center())
                        , run_time=0.25, rate_func=linear
                    )
                    hard_maze.move_poi(nlin, ncol)
                    if search(nlin, ncol) :
                        return True
                    hard_maze.role_back()
                    self.play(
                        Uncreate(arrow, rate_func=lambda t: linear(1-t)), 
                        ApplyMethod(poi.move_to, hard_maze.get_rec(lin, col).get_center(), 
                        rate_func=linear), run_time=0.25
                    )
            return False
        
        print(search(*hard_maze.start))

class Choose_introduction(Scene) :
    def construct(self):
        maze = Maze(3, 5)
        maze.set_start(2, 2)
        maze.set_end(3, 5)
        poi = Dot().move_to(maze.get_rec(*maze.start))
        self.play(ShowCreation(maze))
        self.wait(2)
        self.play(ShowCreation(poi))
        arrows = [
            maze.get_arrow(*maze.loc, direction)
            for direction in [UP, RIGHT, DOWN, LEFT]
        ]
        for arrow in arrows :
            self.play(GrowArrow(arrow))
        self.wait(2)
        poi_and_arrows = VGroup(poi, *arrows)
        self.play(ApplyMethod(poi_and_arrows.move_to, maze.get_rec(2, 3)))
        self.wait(2)
        self.play(
            *[FadeOut(arrow) for arrow in arrows], 
            FadeOut(poi)
        )
        self.wait(2)

        arrows_config = [
            (2, 2, RIGHT),
            (2, 3, RIGHT),
            (2, 4, RIGHT),
            (2, 5, DOWN),
        ]
        arrows = [
            maze.get_arrow(lin, col, direction)
            for lin, col, direction in arrows_config
        ]
        arrow_group = VGroup(*arrows)
        for arrow in arrows :
            self.play(ShowCreation(arrow))
        self.wait(2)

        arrows_config = [
            (2, 2, DOWN),
            (3, 2, RIGHT),
            (3, 3, RIGHT),
            (3, 4, RIGHT),
        ]
        arrows = [
            maze.get_arrow(lin, col, direction)
            for lin, col, direction in arrows_config
        ]
        arrow_group.target = VGroup(*arrows)
        self.play(MoveToTarget(arrow_group))
        self.wait(2)
        self.play(FadeOut(VGroup(*self.mobjects)))
        self.wait(2)

class Show_path(Scene):
    def construct(self):
        maze = Maze(3, 5)
        maze.set_start(1, 1)
        maze.set_end(3, 5)
        dir_set = maze.get_search_order(UP, RIGHT, DOWN, LEFT)
        path_group = []
        path = []
        def search(lin, col):
            nonlocal path, path_group
            if (lin, col)==maze.end:
                path_group.append(VGroup(*[p.deepcopy() for p in path]).set_color_by_gradient(GREEN, RED))
            for mov_x, mov_y, direction in dir_set:
                nlin = lin+mov_x
                ncol = col+mov_y
                if maze.judge(nlin, ncol):
                    maze.move_poi(nlin, ncol)
                    path.append(maze.get_line(lin, col, direction))
                    search(nlin, ncol)
                    maze.role_back()
                    path.pop()
        
        self.play(ShowCreation(maze))
        self.wait(2)
        search(*maze.start)
        cnt = 0
        text = Text('cnt = ',font='Microsoft YaHei', stroke_width=0).scale(0.5).to_corner(UL)
        c = TexMobject('0', stroke_width=0)
        c.next_to(text)
        self.play(Write(text), Write(c))
        for i in range(len(path_group)):
            cnt+=1
            c.target = TexMobject(str(cnt), stroke_width=0).next_to(text)
            if i>=1:
                self.play(Uncreate(path_group[i-1]), run_time=0.25)
            self.play(ShowCreation(path_group[i]), MoveToTarget(c), run_time=0.25)
        

class Limit_introduction(Scene):
    def construct(self):
        maze = Maze(3, 3)
        maze.set_bar(1, 1)
        poi = Dot()
        poi.move_to(maze.get_rec(1, 2).get_center())
        arrow_config = [
            (1, 2, UP),
            (1, 2, RIGHT),
            (1, 2, DOWN),
            (1, 2, LEFT),
        ]
        arrows = []
        for lin, col, direction in arrow_config:
            arrows.append(maze.get_arrow(lin, col, direction))
        out_edge_rectangle = DashedRectangle(1)
        out_edge_rectangle.next_to(maze.get_rec(1, 2), UP, buff=0)
        cross = Cross(out_edge_rectangle)

        self.play(ShowCreation(maze))
        self.play(ShowCreation(poi))
        self.wait()
        self.play(ShowCreation(VGroup(*arrows)))
        self.wait()
        self.play(ShowCreation(out_edge_rectangle))
        self.wait()
        self.play(ShowCreation(cross), ApplyMethod(out_edge_rectangle.set_color, RED))
        self.wait()
        self.play(FadeOut(out_edge_rectangle), FadeOut(cross))
        self.remove(arrows[0])
        self.play(Uncreate(arrows[0].copy()))
        self.wait(2)
        cross = Cross(maze.get_rec(1, 1))
        self.remove(maze.get_rec(1, 1))
        self.add(maze.get_rec(1, 1))
        self.play(
            ApplyMethod(maze.get_rec(1, 1).set_color, RED),
            ShowCreation(cross)
        )
        self.remove(arrows[3])
        self.play(
            Uncreate(arrows[3].copy()),
            ApplyMethod(maze.get_rec(1, 1).set_color, WHITE),
            FadeOut(cross)
        )
        self.wait(2)
        self.play(
            *[Uncreate(arrows[i]) for i in range(1, 3)],
            FadeOut(poi)
        )
        