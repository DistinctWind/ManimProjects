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
        self.num.target = Tex(str(n)).move_to(self.num)
        self.rec.target = SurroundingRectangle(self.num.target, buff=MED_SMALL_BUFF).move_to(self.num.target)
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
        for i in range(len(self.seq)):
            self.cells.append(Cell(self.seq[i], id(i)))
        self.arrow = Arrow(UP*0.75, DOWN*0.75).set_color(YELLOW)
        self.add(*self.cells)
        self.arrange(RIGHT)
        self.arrow.next_to(self.cells[0], UP)
        self.active=1
        self.cells[0].rec.set_color(YELLOW)
    
    def on_show(self, scene=NonScene()):
        return scene.play(ShowCreation(self), GrowArrow(self.arrow))

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
    
    def align(self):
        return [
            cell_nxt.animate.next_to(cell_lst, RIGHT, buff=MED_SMALL_BUFF)
            for cell_nxt, cell_lst in zip(self.cells[1:], self.cells[:-1])
        ]

    def write(self, pos, num, scene=NonScene()):
        self.set_val(pos, num)
        cell = self.cells[rid(pos)]
        cell.target = Cell(num, tag_num=pos).move_to(cell)
        if (pos>1):
            cell.target.next_to(self.cells[rid(pos)-1], buff=MED_SMALL_BUFF)
        shift_value = cell.target.get_width()-cell.get_width()
        if (pos==len(self.cells)):
            return scene.play(MoveToTarget(cell))
        else:
            return scene.play(
                MoveToTarget(cell),
                *[
                    lst_cell.animate.shift(shift_value*RIGHT)
                    for lst_cell in self.cells[rid(pos)+1:]
                ]
            )
    
    def get_val(self, pos):
        return self.seq[rid(pos)]
    
    def set_val(self, pos, num):
        self.seq[rid(pos)]=num
