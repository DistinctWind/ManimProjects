# 视频标题：直观的算法[0x00]：一切的起源
from manimlib.imports import *
from numpy import *

class BeginScene(Scene) :
    def construct(self) :
        title = Text('直观的算法[0x00]：一切的起源', font='simkai')
        self.add(title)