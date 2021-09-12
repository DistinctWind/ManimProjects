from manimlib import *
from random import random, seed

class DashedRectangle(VGroup):
    def __init__(self, length=1, **kwargs):
        super().__init__(**kwargs)
        self.line_list = [
            DashedLine(ORIGIN, ORIGIN+RIGHT*length),
            DashedLine(ORIGIN+RIGHT*length, ORIGIN+(RIGHT+UP)*length),
            DashedLine(ORIGIN+(RIGHT+UP)*length, ORIGIN+UP*length),
            DashedLine(ORIGIN+UP*length, ORIGIN),
        ]
        self.add(*self.line_list)
        
class Maze(VGroup) :
    def __init__(self, lin, col, length=1, scale_factor=1, **kwargs) :
        super().__init__(**kwargs)
        self.rec_list = []
        self.bar_list = []
        self.bar_poi_list = []
        self.path_poi_list = []
        self.mlin = lin
        self.mcol = col
        self.length = length
        self.start = (0, 0)
        self.end = (0, 0)
        self.scale_factor = scale_factor
        self.loc = (0, 0)
        for i in range(lin) :
            for j in range(col) :
                self.rec_list.append(Rectangle(width=length, height=length, stroke_width=DEFAULT_STROKE_WIDTH*scale_factor))
                self.rec_list[-1].shift(length*j*RIGHT+length*i*DOWN)
                self.add(self.rec_list[-1])
        self.scale(scale_factor)
        self.move_to(ORIGIN)

    def setup_map(self) :
        self.vis = [ [ False for _col in range(self.mcol) ] for _lin in range(self.mlin) ]
    
    def get_search_order(self, *dirs) :
        res = []
        for i in dirs :
            if all(i==UP) :
                res.append((-1, 0, UP))
            if all(i==RIGHT) :
                res.append((0, 1, RIGHT))
            if all(i==DOWN) :
                res.append((1, 0, DOWN))
            if all(i==LEFT) :
                res.append((0, -1, LEFT))
        return res

    def get_rec(self, lin, col) :
        """
        这个函数会返回给定坐标的矩形，
        其中lin表示行，col表示列。
        """
        return self.rec_list[(lin-1)*self.mcol+(col-1)]
    
    def add_rec_num(self) :
        i = 0
        num_list = []
        for rec in self.rec_list :
            num_list.append(Tex(str(i)))
            num_list[-1].scale(0.8*self.scale_factor)
            num_list[-1].move_to(rec.get_center())
            i += 1
        self.add(*num_list)

    def set_start(self, lin, col) :
        start_text = Text('S', font='cour', stroke_width=0)
        start_text.move_to(self.get_rec(lin, col).get_center())
        start_text.scale(0.8*self.scale_factor)
        start_text.set_color(GREEN)
        self.start = (lin, col)
        self.loc = (lin, col)
        self.path_poi_list.append((lin, col))
        self.add(start_text)
    
    def set_end(self, lin, col) :
        end_text = Text('E', font='cour', stroke_width=0)
        end_text.move_to(self.get_rec(lin, col).get_center())
        end_text.scale(0.8*self.scale_factor)
        end_text.set_color(RED)
        self.end = (lin, col)
        self.add(end_text)

    def set_bar(self, lin, col) :
        self.bar_poi_list.append((lin, col))
        bar = Text('#', font='cour', stroke_width=0)
        bar.move_to(self.get_rec(lin, col))
        bar.scale(1.2*self.scale_factor)
        bar.set_color(YELLOW)
        bar.set_stroke(width=2)
        self.bar_list.append(bar)
        self.add(bar)
    
    def set_bar_randomly(self, rate=0.25) :
        seed(a=None, version=2)
        for i in range(1, self.mlin+1) :
            for j in range(1, self.mcol+1) :
                if (i, j) == self.start or (i, j) == self.end :
                    continue
                if random()<rate :
                    self.set_bar(i, j)
    
    def set_bar_by_str(self, s) :
        assert(isinstance(s, str))
        lines = s.strip().split('\n')
        bar_map = [ list(_l.strip()) for _l in lines]
        for lin in range(1, self.mlin+1) :
            for col in range(1, self.mcol+1) :
                if bar_map[lin-1][col-1]=='1' :
                    self.set_bar(lin, col)    
        
    def get_arrow(self, lin, col, dir, color=BLUE) :
        """
        这个函数返回一个从点poi指向dir方向的箭头
        """
        location = self.get_rec(lin, col).get_center()
        return Arrow(location, location+dir*self.length*self.scale_factor, buff=0).set_color(color)
    
    def get_line(self, lin, col, dir, color=BLUE):
        location = self.get_rec(lin, col).get_center()
        return Line(location, location+dir*self.length*self.scale_factor, buff=0).set_color(color)
    
    def add_path_poi_list(self, lin, col):
        self.path_poi_list.append((lin, col))

    def move_poi(self, lin, col) :
        self.loc = (lin, col)
        self.path_poi_list.append((lin, col))
    
    def role_back(self) :
        if len(self.path_poi_list)==1 :
            raise RuntimeError
        self.loc = self.path_poi_list.pop()
    
    def judge(self, lin, col, ignore_path=False) :
        if (lin, col) in self.bar_poi_list :
            return False
        if not 1<=lin<=self.mlin :
            return False
        if not 1<=col<=self.mcol :
            return False
        if ignore_path:
            return True
        if (lin, col) in self.path_poi_list :
            return False
        return True