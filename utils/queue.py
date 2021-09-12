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
        self.object_list = []
        self.len = 0
        self.num = 1
        super().__init__(*vmobjects, **kwargs)
    def put(self, item):
        tag = Text(str(self.num), font='msyh')
        self.num+=1
        item_and_tag = VGroup(item, tag).arrange(DOWN, buff=MED_SMALL_BUFF)
        self.add(item_and_tag)
        self.object_list.append(item_and_tag)
        self.len+=1
    def pop(self):
        self.remove(self.object_list[0])
        del self.object_list[0]
        self.len-=1

class data_pack:
    def __init__(self, step, lin, col):
        self.step=step
        self.lin=lin
        self.col=col