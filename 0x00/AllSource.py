# 视频标题：直观的算法[0x00]：一切的起源
from manimlib.imports import *
from numpy import *

class BeginScene(Scene) :
    def construct(self) :
        title = Text('直观的算法', font='微软雅黑', stroke_width=0.5)
        author = Text('万木长风', font='微软雅黑', stroke_width=0).scale(0.65)
        title.move_to(UP*0.5)
        author.move_to(DOWN*0.5)

        self.add(title, author)