from math import remainder
from platform import uname
from manimlib import *

class Cell(VGroup):
    def __init__(self, n, tag_num):
        super().__init__()

        self.num = Tex(str(n))
        self.rec = SurroundingRectangle(self.num, buff=MED_SMALL_BUFF).set_color(WHITE)
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

def rid(num):
    """Translate from id to rid"""
    return num-1
    
def id(num):
    """Translate from rid to id"""
    return num+1

class NonScene():
    def play(self, animates):
        return animates
class Sequence(VGroup):
    def __init__(self, seq):
        super().__init__()
        self.seq = seq
        self.cells = []
        for num in self.seq:
            self.cells.append(Cell(num, id(self.seq.index(num))))
        self.arrow = Arrow(UP*0.75, DOWN*0.75).set_color(YELLOW)
        self.add(*self.cells)
        self.arrange(RIGHT)
        self.arrow.next_to(self.cells[0], UP)
        self.active=1
        self.cells[0].rec.set_color(YELLOW)
    
    def move_arrow(self, num, scene=NonScene()):
        return scene.play(self.arrow.animate.next_to(self.cells[rid(num)], UP))
     
    def mark(self, num, scene=NonScene()):
        return scene.play(self.cells[rid(num)].rec.animate.set_color(YELLOW))
    
    def unmark(self, num, scene=NonScene()):
        return scene.play(self.cells[rid(num)].rec.animate.set_color(WHITE))
    
    def activate(self, num, scene=NonScene()):
        animate_list = scene.play(
            self.mark(num),
            self.unmark(self.active),
            self.move_arrow(num)
        )
        self.active=num
        if animate_list!=None:
            return animate_list
    
    def move_and_update_mark(self, num):
        pass

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