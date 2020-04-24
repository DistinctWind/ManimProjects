from manimlib.imports import *
from random import random, seed

class Maze(VGroup) :
    rec_list = []
    bar_list = []
    bar_poi_list = []
    path_poi_list = []
    mlin = 0
    mcol = 0
    length = 0
    start = (0, 0)
    end = (0, 0)
    scale_factor = 0
    loc = (0, 0)
    def __init__(self, lin, col, length=1, scale_factor=1, **kwargs) :
        super().__init__(**kwargs)
        self.mlin = lin
        self.mcol = col
        self.scale_factor = scale_factor
        self.length = length
        for i in range(lin) :
            for j in range(col) :
                self.rec_list.append(Rectangle(width=length, height=length, stroke_width=DEFAULT_STROKE_WIDTH*scale_factor))
                self.rec_list[-1].shift(length*j*RIGHT+length*i*DOWN)
                self.add(self.rec_list[-1])
        self.scale(scale_factor)
        self.move_to(ORIGIN)

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
            num_list.append(TexMobject(str(i)))
            num_list[-1].scale(0.8*self.scale_factor)
            num_list[-1].move_to(rec.get_center())
            i += 1
        self.add(*num_list)

    def set_start(self, lin, col) :
        start_text = Text('S', font='courier', stroke_width=0)
        start_text.move_to(self.get_rec(lin, col).get_center())
        start_text.scale(0.8*self.scale_factor)
        start_text.set_color(GREEN)
        self.start = (lin, col)
        self.loc = (lin, col)
        self.path_poi_list.append((lin, col))
        self.add(start_text)
    
    def set_end(self, lin, col) :
        end_text = Text('E', font='courier', stroke_width=0)
        end_text.move_to(self.get_rec(lin, col).get_center())
        end_text.scale(0.8*self.scale_factor)
        end_text.set_color(RED)
        self.end = (lin, col)
        self.add(end_text)

    def set_bar(self, lin, col) :
        self.bar_poi_list.append((lin, col))
        bar = TextMobject('\#')
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
        
    def get_arrow(self, lin, col, dir, color=YELLOW) :
        """
        这个函数返回一个从点poi指向dir方向的箭头
        """
        location = self.get_rec(lin, col).get_center()
        return Arrow(location, location+dir*self.length*self.scale_factor, buff=0).set_color(color)
    
    def move_poi(self, lin, col) :
        self.loc = (lin, col)
        self.path_poi_list.append((lin, col))
    
    def role_back(self) :
        if len(self.path_list)==1 :
            raise RuntimeError
        self.loc = self.path_poi_list.pop()