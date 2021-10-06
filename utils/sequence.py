from manimlib import *

class Sequence(VGroup):
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