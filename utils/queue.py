from manimlib import *


class Queue():
    def __init__(self):
        self.data = list()
        self.len = 0
    def put(self, x):
        self.data.append(x)
        self.len+=1
        return x
    def pop(self):
        res = self.data[0]
        del self.data[0]
        self.len-=1
        return res
    def empty(self):
        return self.len==0

class VirtualizedQueue(VGroup):
    def __init__(self, *vmobjects, **kwargs):
        super().__init__(*vmobjects, **kwargs)
        self.object_list = []
        self.len = 0
        self.num = 1
    def put(self, item):
        tag = Text(str(self.num), font='msyh').scale(0.5)
        self.num+=1
        item_and_tag = VGroup(item, tag).arrange(UL, buff=0.1)
        self.add(item_and_tag)
        self.object_list.append(item_and_tag)
        self.len+=1
        return item_and_tag
    def pop(self):
        self.remove(self.object_list[0])
        del self.object_list[0]
        self.len-=1
        return self

class data_pack:
    def __init__(self, step, lin, col, dis=-1, paths=None):
        self.step=step
        self.lin=lin
        self.col=col
        self.dis=dis
        self.path_list = paths

class VirtualizedDataPack(VGroup):
    def __init__(self, step, lin, col, **kwargs):
        super().__init__(**kwargs)
        self.circle = Circle().set_color(BLUE).set_fill(BLUE, opacity=0.3).scale(1.5)
        self.step_tag = Text('step='+str(step), font='msyh', color=YELLOW)
        self.pos_tag = Text(
            '(%(lin)s, %(col)s)' % {"lin": str(lin), "col": str(col)},
            font='msyh'
        )
        VGroup(
            self.step_tag, self.pos_tag
        ).arrange(DOWN).move_to(self.circle.get_center())
        self.add(
            VGroup(self.circle, self.step_tag, self.pos_tag).scale(0.75)
        )
        