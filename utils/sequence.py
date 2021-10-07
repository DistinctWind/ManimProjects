from manimlib import *

from utils.pos import x_shift

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
    
    def get_cell(self, num):
        return self.cells[rid(num)]

class DepthBar(VGroup):
    def __init__(self):
        super().__init__()
        title = Text("Depth", font='Microsoft YaHei').scale(0.5)
        self.add(title)
        self.depth=1
        
        self.deep_tag = [Text("1", font='Microsoft YaHei').scale(0.75)]
        self.add(*self.deep_tag)
        self.arrange(DOWN, buff=LARGE_BUFF)
    
    def deepen(self):
        self.deep_tag.append(Text(str(self.depth+1), font='Microsoft YaHei').scale(0.75).next_to(self.deep_tag[-1], DOWN, buff=LARGE_BUFF*2))
        self.add(self.deep_tag[-1])
        self.depth+=1
        return FadeIn(self.deep_tag[-1], scale=1.5)

class CallTree(VGroup):
    def __init__(self, main_caller):
        super().__init__(main_caller)
        self.depth_bar = DepthBar().to_edge(LEFT)
        self.main_caller = main_caller
        self.depth_list = [VGroup(main_caller).move_to(ORIGIN).align_to(self.depth_bar.deep_tag[rid(1)], UP)]
        self.arrow_group = VGroup()
        self.add(self.arrow_group)
        
    
    def get_depth_group(self, depth):
        return self.depth_list[rid(depth)]
    
    def get_cell(self, depth, num):
        return self.depth_list[rid(depth)][rid(num)]

    def extent(self, caller, to_call, to_caller_depth):
        animate_list = [FadeIn(to_call, scale=1.5)]
        if to_caller_depth>self.depth_bar.depth:
            animate_list.append(self.depth_bar.deepen())
            self.depth_list.append(VGroup(to_call).align_to(self.depth_bar.deep_tag[rid(to_caller_depth)], UP).shift(x_shift(to_call)))
        else:
            self.depth_list[rid(to_caller_depth)].add(to_call)
        to_call.next_to(self.depth_list[rid(to_caller_depth)], RIGHT)
        to_call.align_to(self.depth_bar.deep_tag[rid(to_caller_depth)], UP)
        arrow = always_redraw(lambda:Arrow(caller.get_bottom(), to_call.get_top()))
        self.arrow_group.add(arrow)
        animate_list.append(GrowArrow(arrow))

        return animate_list
    
    def compose(self):
        return [
            vgroup.animate.arrange(RIGHT, buff=LARGE_BUFF).move_to(vgroup.get_center()).shift(x_shift(vgroup))
            for vgroup in self.depth_list
        ]

        
        

