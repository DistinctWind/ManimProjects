from manimlib.imports import *
class Main(Scene) :
    def construct(self):
        title = Text('万木长风', font='msyh', stroke_width=0)
        sub_title = Text('Directed by DistinctWind', font='mayh', stroke_width=0)
        sub_title.scale(0.5)
        sub_title.next_to(title, DOWN*1.5)
        self.play(Write(title))
        self.play(Write(sub_title))
        self.wait()
        self.play(Uncreate(title), Uncreate(sub_title))
        self.wait()