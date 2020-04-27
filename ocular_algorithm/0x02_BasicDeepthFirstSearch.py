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

#This one is from trying.py,
#which is done when I haven't write Maze()
class Show_path(Scene) :
    def construct(self) :
        g = VGroup(
            *[Square().scale(0.3) for x in range(5)]
        ).arrange(RIGHT, buff=0)
        f = VGroup(
            *[VGroup(
                *[Square().scale(0.5) for x in range(5)]
            ).arrange(RIGHT, buff=0) for y in range(3)]
        ).arrange(DOWN, buff=0)
        self.add(f)
        s = TextMobject('S').scale(1.25).set_color(GREEN).set_opacity(0.5)
        s.move_to(f[0][0].get_center())
        t = TextMobject('T').scale(1.25).set_color(RED).set_opacity(0.5)
        t.move_to(f[2][4].get_center())
        self.play(Write(s), Write(t))
        self.wait()

        path = []
        vis = []
        mov_x = (-1, 0, 1, 0)
        mov_y = (0, 1, 0, -1)
        cnt = 0
        sp = []
        text = TextMobject("cnt="+str(cnt)).set_color(GREEN).to_corner(UL)
        self.play(Write(text))
        def show_path(self) :
            nonlocal cnt, sp
            cnt += 1
            p = VGroup(
                *[Line(f[begin[0]][begin[1]].get_center(), f[end[0]][end[1]].get_center()).set_color(GREEN)
                    for begin, end in path
                ]
            )
            if cnt == 1 :
                self.play(ShowCreation(p))
                sp.append(p)
                text.target=TextMobject("cnt="+str(cnt)).set_color(GREEN).to_corner(UL)
                self.play(MoveToTarget(text))
                self.wait(3)
            else :
                self.remove(sp[0])
                self.add(p)
                text.target=TextMobject("cnt="+str(cnt)).set_color(GREEN).to_corner(UL)
                self.play(MoveToTarget(text), run_time=0.1)
                sp[0]=p
        def dfs(x, y) :
            nonlocal path, vis, cnt
            vis.append((x,y))
            for i in range(4) :
                #if cnt > 10 :
                    #return
                now_x = x + mov_x[i]
                now_y = y + mov_y[i]
                if (now_x, now_y) in vis :
                    continue
                if 0<=now_x<=2 and 0<=now_y<=4 :
                    path.append(((x, y), (now_x, now_y)))
                    if now_x==2 and now_y==4 :
                        show_path(self)
                        #cnt += 1
                    else :
                        dfs(now_x, now_y)
                    path.pop()
            vis.pop()
        dfs(0,0)
        self.wait()

class Limit_introduction(Scene) :
    def construct(self) :
        pass