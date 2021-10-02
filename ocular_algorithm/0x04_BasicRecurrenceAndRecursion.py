from manimlib import *

import sys
import os

sys.path.append(os.getcwd())

from utils.imports import *

class Opening(Scene):
    def construct(self):
        title = Text("基础递推递归", font='msyh')
        self.play(Write(title), run_time=2)
        self.wait()
        self.play(FadeOut(title))
        self.wait()
        return super().construct()

class BeginningIntroduction(Scene):
    def construct(self):
        RecurrenceFormula = Tex(
            r"a_1=1 ,\quad a_n=a_{n-1}+1"
        )
        GeneralFormula = Tex(
            r"a_n=n"
        )
        VGroup(RecurrenceFormula, GeneralFormula).arrange(DOWN, buff=LARGE_BUFF)
        self.play(Write(RecurrenceFormula))
        self.wait()
        self.play(Write(GeneralFormula))
        self.wait()

        RecurrenceFormula.target = Tex(
            r"a_n=\begin{cases}1&{n=1,2,}\\a_{n-1}+a_{n-2}&n\geq3.\end{cases}"
        ).replace(RecurrenceFormula).scale(1.25).shift(UP*.5)
        GeneralFormula.target = Tex(
            r"a_n=\frac{1}{\sqrt{5}}\left[\left(\frac{1+\sqrt{5}}{2}\right)^n-\left(\frac{1-\sqrt{5}}{2}\right)^n\right]"
        ).next_to(RecurrenceFormula.target, DOWN, buff=LARGE_BUFF)
        self.play(MoveToTarget(RecurrenceFormula), MoveToTarget(GeneralFormula))
        self.wait()

        self.play(
            FadeOut(GeneralFormula),
            RecurrenceFormula.animate.move_to(ORIGIN)
        )
        self.wait()
        self.play(*[FadeOut(_mobjects) for _mobjects in self.mobjects])
        self.wait()

        return super().construct()

class RecurrenceFibIntroduction(Scene):
    def construct(self):
        seq=Sequence(10, 1, 1)
        self.play(ShowCreation(seq))
        return super().construct()

class trying1(Scene):
    def construct(self):
        tex = Tex("a=1")
        self.play(Write(tex))
        return super().construct()