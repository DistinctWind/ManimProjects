from manimlib import *

import sys
import os

from tqdm.std import tqdm

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
        
        Fib = [1, 1]
        for i in range(2, 2022):
            Fib.append(Fib[i-1]+Fib[i-2])
        Fib_eq = []
        for i in tqdm(range(2021)):
            Fib_eq.append(Text("a["+str(i+1)+"]"))
        VGroup(*Fib_eq).arrange(DOWN).next_to(RecurrenceFormula, DOWN)
        self.play(*[Write(_Fib_eq) for _Fib_eq in Fib_eq], run_time=2)
        self.wait()
        self.play(self.camera.frame.animate.move_to(Fib_eq[-1].get_center()), run_time=10)
        self.wait()

        self.play(*[FadeOut(_mobjects) for _mobjects in self.mobjects])
        self.wait()

        return super().construct()

class RecurrenceFibIntroduction(Scene):
    def construct(self):
        title = Text("斐波那契数列", font='DengXian')
        self.play(Write(title))
        self.wait()
        subtitle = Text("Fibonacci", font='DengXian')
        subtitle.next_to(title, DOWN)
        self.play(Write(subtitle))
        subtitle.target = Text("Fib", font='DengXian').next_to(title, DOWN)
        self.play(MoveToTarget(subtitle))
        self.wait()
        subtitle.target = Text("fib", font='DengXian').next_to(title, DOWN)
        self.play(MoveToTarget(subtitle))
        self.wait()
        self.play(FadeOut(subtitle))
        self.wait()

        self.play(title.animate.to_edge(UP).scale(0.75))

        RecurrenceFormula = Tex(
            r"a_n=\begin{cases}1&{n=1,2,}\\a_{n-1}+a_{n-2}&n\geq3.\end{cases}"
        ).scale(1.25).shift(UP*.5)
        GeneralFormula = Tex(
            r"a_n=\frac{1}{\sqrt{5}}\left[\left(\frac{1+\sqrt{5}}{2}\right)^n-\left(\frac{1-\sqrt{5}}{2}\right)^n\right]"
        ).next_to(RecurrenceFormula, DOWN, buff=LARGE_BUFF)
        self.play(Write(RecurrenceFormula), Write(GeneralFormula))
        self.wait()
        self.play(FadeOut(RecurrenceFormula), FadeOut(GeneralFormula))
        self.wait()

        seq = Sequence([0 for i in range(10)]).move_to(ORIGIN)
        seq.on_show(self)
        seq.write(1, 1, self)
        seq.write(2, 1, self)
        for pos in range(3, 11):
            seq.activate(pos, self)
            seq.write(pos, seq.get_val(pos-1)+seq.get_val(pos-2), self)
        
        self.play(*[FadeOut(_mobject) for _mobject in self.mobjects])
        return super().construct()


class RecursionFibIntroduction(Scene):
    def construct(self):
        title = Text("斐波那契数列", font='DengXian')
        subtitle = Text("(递归解法）", font='DengXian')
        subtitle.scale(0.75).next_to(title, DOWN, buff=MED_SMALL_BUFF)
        self.play(
            Write(title),
            Write(subtitle)
        )
        self.wait()
        self.play(
            FadeOut(title),
            FadeOut(subtitle)
        )

        seq = Sequence([1, 1, 0, 0, 0])
        main_call = seq.cells[rid(5)].copy().next_to(seq, DOWN, buff=MED_LARGE_BUFF)

        self.play(ShowCreation(seq))
        self.wait()
        self.play(ShowCreation(main_call))
        
        return super().construct()
class trying1(Scene):
    def construct(self):
        tex = Tex("a=1")
        self.play(Write(tex))
        return super().construct()

class trying2(Scene):
    def construct(self):
        hello = Tex("1")
        rec = Rectangle()
        f_always(rec.move_to, hello.get_center)
        self.play(Write(hello))
        self.play(ShowCreation(rec))
        self.play(hello.animate.shift(2*RIGHT+UP))

class trying3(Scene):
    def construct(self):
        cell = Cell(1234567890, 7)
        self.play(ShowCreation(cell))
        self.play(*cell.write(1))
        return super().construct()

class trying4(Scene):
    def construct(self):
        seq = Sequence([1, 3, 5, 2, 4, 6])
        self.play(ShowCreation(seq), GrowArrow(seq.arrow))
        seq.activate(4, self)
        seq.activate(6, self)
        seq.write(3, 123456, self)
        seq.write(6, 123456, self)
        seq.write(2, 1345, self)
        seq.write(3, 1, self)
        return super().construct()
    
class trying5(Scene):
    def construct(self):
        depth_bar = DepthBar()
        self.play(ShowCreation(depth_bar))
        self.play(depth_bar.deepen())
        return super().construct()