from manimlib import *

class Sequence(VGroup):
    def __init__(self, len, width, height):
        super().__init__()
        self.num_list=[]
        self.rec_list=[]
        rec = Rectangle(width=width, height=height)
        for i in range(len):
            self.rec_list.append(rec.copy())
            self.add(self.rec_list[-1])
        self.arrange(RIGHT, buff=0)