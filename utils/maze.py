from manimlib.imports import *

class Maze(VGroup) :
    rec_list = []
    mlin = 0
    mcol = 0
    scale_factor = 0
    def __init__(self, lin, col, width=1, height=1, scale_factor=1, **kwargs) :
        super().__init__(**kwargs)
        self.mlin = lin
        self.mcol = col
        self.scale_factor = scale_factor
        for i in range(lin) :
            for j in range(col) :
                self.rec_list.append(Rectangle(width=width, height=height, stroke_width=DEFAULT_STROKE_WIDTH*scale_factor))
                self.rec_list[-1].shift(width*j*RIGHT+height*i*DOWN)
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
        self.add(start_text)
    
    def set_end(self, lin, col) :
        end_text = Text('E', font='courier', stroke_width=0)
        end_text.move_to(self.get_rec(lin, col).get_center())
        end_text.scale(0.8*self.scale_factor)
        end_text.set_color(RED)
        self.add(end_text)