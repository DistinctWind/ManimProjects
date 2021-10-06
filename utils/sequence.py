from manimlib import *

class Cell(VGroup):
    def __init__(self, n, tag_num):
        super().__init__()

        self.num = Tex(str(n))
        self.rec = SurroundingRectangle(self.num, buff=MED_SMALL_BUFF)
        self.tag = Text(str(tag_num), font='Microsoft YaHei').scale(0.5)\
            .next_to(self.rec, DOWN, buff=MED_SMALL_BUFF)
        self.add(self.num, self.rec, self.tag)
    
    def write(self, n):
        self.num.target = Tex(str(n))
        self.rec.target = SurroundingRectangle(self.num.target, buff=MED_SMALL_BUFF)
        return [
            MoveToTarget(self.num), 
            MoveToTarget(self.rec), 
            self.tag.animate.next_to(self.rec, DOWN, buff=MED_SMALL_BUFF)
        ]

class oldSequence(VGroup):
    """This class is forbidden for its fool"""
    def __init__(self, len, width, height):
        super().__init__()
        self.num_list=[]
        self.rec_list=[]
        self.rec_num = []
        rec = Rectangle(width=width, height=height)
        for i in range(len):
            self.rec_list.append(rec.copy())
            self.rec_num.append(Text(str(i+1)).scale(0.5))
            self.add(self.rec_list[-1], self.rec_num[-1])
        self.arrange(RIGHT, buff=0)
        self.arrow = Arrow(UP*0.75, DOWN*0.75).next_to(self.rec_list[0], UP).set_color(YELLOW)
        self.add(self.arrow)
        self.active_rec = 1
        self.rec_list[0].set_color(YELLOW)
        for i in range(len):
            self.rec_num[i].next_to(self.rec_list[i], DOWN)
    
    def activate(self, num):
        """This methon return a list of animation"""
        animate_list = [
            self.rec_list[self.active_rec-1].animate.set_color(WHITE),
            self.rec_list[num-1].animate.set_color(YELLOW),
            self.arrow.animate.next_to(self.rec_list[num-1], UP)
        ]
        self.active_rec = num
        return animate_list
    
    def mark(self, *num, color=YELLOW):
        animate_list = [
            self.rec_list[i-1].animate.set_color(color) for i in num
        ]
        return animate_list
    
    def remark(self, *num):
        animate_list = [
            self.rec_list[i-1].animate.set_color(WHITE) for i in num
        ]
        return animate_list