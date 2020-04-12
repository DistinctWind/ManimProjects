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

class Start_end_introduction(Scene) :
    def construct(self) :
        motto = Text('物有本末，事有终始，知所先后，则近道矣。', font='WenQuanYi Zen Hei', stroke_width=0)
        motto.scale(0.5)
        left_quote = Text('“', font='WenQuanYi Zen Hei', stroke_width=0)
        left_quote.scale(1.5)
        left_quote.next_to(motto, direction=UP*0.5+LEFT, buff=0.5)
        author = Text('——曾参《礼记·大学》', font='WenQuanYi Zen Hei', stroke_width=0)
        author.scale(0.5)
        author.next_to(motto, direction=DR, buff=0.5).shift(LEFT*4)
        self.play(*[Write(item) for item in [left_quote, motto, author]])
        self.wait(2)
        self.play(*[FadeOut(item) for item in [left_quote, motto, author]])
        self.wait(2)
        
        start_text = Text('Start', font='Arimo', stroke_width=0).scale(0.5)
        start_round_rectangle = RoundedRectangle(height=start_text.get_height()+1, width=start_text.get_width()+1)
        start_round_rectangle.set_color('#16c0ac')
        start = VGroup(start_text, start_round_rectangle)
        start.move_to(UP*2)
        end_text = Text('End', font='Arimo', stroke_width=0).scale(0.5)
        end_round_rectangle = RoundedRectangle(height=end_text.get_height()+1, width=end_text.get_width()+1)
        end_round_rectangle.set_color('#78380d')
        end = VGroup(end_text, end_round_rectangle)
        end.move_to(DOWN*2)
        arrow = Arrow(start.get_bottom(), end.get_top(), buff=0.1)
        no_end_warning = Text('无法结束的程序', font='WenQuanYi Zen Hei', stroke_width=0).scale(0.5)
        no_end_warning.move_to(RIGHT*3)
        endless_loop_text = Text('Endless Loop', font='Arimo', stroke_width=0).scale(0.7)
        endless_loop_text.next_to(no_end_warning.get_bottom(), DOWN, buff=0.5)
        endless_loop_text.set_color(RED)
        cross = Cross(no_end_warning)

        self.play(ShowCreation(start))
        self.wait()
        self.play(GrowArrow(arrow))
        self.wait()
        self.play(ShowCreation(end))
        self.wait()
        self.wait(2)
        self.play(*[ApplyMethod(item.shift, LEFT*4) for item in [start, arrow, end]])
        self.wait(2)

        endless_loop_arrow = CurvedArrow(start.get_bottom(), endless_loop_text.get_edge_center(DOWN))
        self.play(Write(no_end_warning))
        self.wait(2)
        self.play(ShowCreation(cross))
        self.wait(2)
        self.play(FadeInFrom(endless_loop_text, UP))
        self.wait(2)
        self.play(ReplacementTransform(arrow, endless_loop_arrow))
        self.wait(2)
        self.play(*[FadeOut(item) for item in self.mobjects])
        self.wait(2)