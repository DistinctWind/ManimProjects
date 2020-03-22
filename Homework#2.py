from manimlib.imports import *
from numpy import *
class BeginScene(Scene) :
    def construct(self) :
        title = Text("Manim Homework Vol.2", font='微软雅黑', stroke_width=0)
        author = Text("Made by @DistinctWind", font='微软雅黑', stroke_width=0).scale(0.5)
        title.move_to(UP*0.5)
        author.move_to(DOWN*0.5)
        self.play(Write(title))
        self.play(Write(author))
        self.wait(2)
        
        title_and_author = VGroup(title, author)
        main = Text("自然数立方和公式几何证明", font='微软雅黑', stroke_width=0)
        self.play(
            FadeOut(title_and_author)
        )
        self.play(
            Write(main),
            run_time=2
        )
        self.wait(2)
        self.play(FadeOutAndShift(main))
        self.wait(2)
