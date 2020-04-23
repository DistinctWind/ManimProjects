from manimlib.imports import *
from random import randint

class Maze(VGroup) :
    rec_list = []
    bar_list = []
    path_poi_list = []
    mlin = 0
    mcol = 0
    length = 0
    start = (0, 0)
    end = (0, 0)
    scale_factor = 0
    poi = (0, 0)
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
        self.poi = self.start = (lin, col)
        self.path_poi_list.append((lin, col))
        self.add(start_text)
    
    def set_end(self, lin, col) :
        end_text = Text('E', font='courier', stroke_width=0)
        end_text.move_to(self.get_rec(lin, col).get_center())
        end_text.scale(0.8*self.scale_factor)
        end_text.set_color(RED)
        self.end = (lin, col)
        self.add(end_text)
    
    def get_arrow(self, poi, dir, color=YELLOW) :
        """
        这个函数返回一个从点poi指向dir方向的箭头
        """
        location = self.get_rec(*poi).get_center()
        return Arrow(location, location+dir*self.length, buff=0).set_color(color)
    
    def move_poi_to(self, target) :
        assert(isinstance(target, tuple))
        self.path_poi_list.append(target)
        self.poi = target
    
    def role_back(self) :
        if len(self.path_list)==1 :
            raise RuntimeError
        self.path_poi_list.pop()