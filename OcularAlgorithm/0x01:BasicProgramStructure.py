from manimlib.imports import *

class Introduction(Scene) :
    def construct(self) :
        title = Text('基本算法结构', font='WenQuanYi Zen Hei', stroke_width=0).to_edge(UP).scale(0.9)
        text_list = [
            '顺序结构',
            '选择结构',
            '循环结构',
        ]
        text_list = [
            Text(_text, font='WenQuanYi Zen Hei', stroke_width=0).scale(0.5) for _text in text_list
        ]
        text_group = VGroup(*text_list).arrange(direction=RIGHT, buff=2).shift(UP*1.5)
        self.play(Write(title))
        self.wait(2)

        chart_list = [
            VGroup(
                Arrow(np.array([0, 4, 0]), np.array([0, 2, 0]), buff=0.1).set_stroke(width=3),
                VGroup(
                    Text('step 1', font='Arimo', stroke_width=0),
                    Polygon(np.array([2, 1, 0]), np.array([2, -1, 0]), np.array([-2, -1, 0]), np.array([-2, 1, 0])),
                ),
                Arrow(np.array([0, -2, 0]), np.array([0, -4, 0]), buff=0.1).set_stroke(width=3),
                VGroup(
                    Text('step 2', font='Arimo', stroke_width=0),
                    Polygon(np.array([2, 1, 0]), np.array([2, -1, 0]), np.array([-2, -1, 0]), np.array([-2, 1, 0])),
                ),
                Arrow(np.array([0, -6, 0]), np.array([0, -8, 0]), buff=0.1).set_stroke(width=3),
            ).arrange(DOWN, buff=0.1).scale(0.4),
            VGroup(
                Arrow(np.array([0, 2, 0]), np.array([0, 1, 0]), buff=0).set_stroke(width=3),
                VGroup(
                    Text('Judgement', font='Arimo', stroke_width=0).scale(0.5).set_color(YELLOW),
                    Polygon(np.array([0, 1, 0]), np.array([2, 0, 0]), np.array([0, -1, 0]), np.array([-2, 0, 0])),
                ),
                Text('Yes', font='Arimo', stroke_width=0).scale(0.5).move_to(np.array([-2.5, 0.5, 0])).set_color(GREEN),
                Line(np.array([-2, 0, 0]), np.array([-3, 0, 0]), buff=0).set_color(GREEN),
                Arrow(np.array([-3, 0, 0]), np.array([-3, -1, 0]), buff=0).set_stroke(width=3).set_color(GREEN),
                Text('No', font='Arimo', stroke_width=0).scale(0.5).move_to(np.array([2.5, 0.5, 0])).set_color(RED),
                Line(np.array([2, 0, 0]), np.array([3, 0, 0]), buff=0).set_color(RED),
                Arrow(np.array([3, 0, 0]), np.array([3, -1, 0]), buff=0).set_color(RED),
            ).scale(0.5),
            VGroup(
                Arrow(np.array([0, 3, 0]), np.array([0, 1, 0]), buff=0.1).set_stroke(width=3),
                VGroup(
                    Text('Loop Body', font='Arimo', stroke_width=0).scale(0.7),
                    Polygon(np.array([2, 1, 0]), np.array([2, -1, 0]), np.array([-2, -1, 0]), np.array([-2, 1, 0])),
                ),
                Arrow(np.array([0, -1, 0]), np.array([0, -2, 0]), buff=0).set_stroke(width=3),
                VGroup(
                    Text('judgement', font='Arimo', stroke_width=0).scale(0.5).shift(DOWN*3).set_color(YELLOW),
                    Polygon(np.array([0, -2, 0]), np.array([2, -3, 0]), np.array([0, -4, 0]), np.array([-2, -3, 0])),
                ),
                Text('No', font='Arimo', stroke_width=0).move_to(np.array([2.5, -2.5, 0])).scale(0.5).set_color(RED),
                Line(np.array([2, -3, 0]), np.array([3, -3, 0]), buff=0).set_color(RED),
                Line(np.array([3, -3, 0]), np.array([3, 2, 0]), buff=0).set_color(RED),
                Arrow(np.array([3, 2, 0]), np.array([0.1, 2, 0]), buff=0).set_stroke(width=3).set_color(RED),
                Text('Yes', font='Arimo', stroke_width=0).move_to(np.array([0.5, -4.4, 0])).scale(0.5).set_color(GREEN),
                Arrow(np.array([0, -4, 0]), np.array([0, -5, 0]), buff=0).set_stroke(width=3).set_color(GREEN),
            ).scale(0.5)
        ]
        for text, chart in zip(text_list, chart_list) :
            chart.next_to(text, direction=DOWN, buff=0.5)
            self.play(Write(text))
            self.play(ShowCreation(chart), run_time=3, rate_func=lambda x: x)
            self.wait()
        self.wait(2)
        self.play(FadeOut(VGroup(*self.mobjects)))
        self.wait()