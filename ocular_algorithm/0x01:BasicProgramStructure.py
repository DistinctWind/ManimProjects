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
        start_round_rectangle = RoundedRectangle(height=start_text.get_height()+1, width=start_text.get_width()+1.5)
        start_round_rectangle.set_color('#16c0ac')
        start = VGroup(start_text, start_round_rectangle)
        start.move_to(UP*2)
        end_text = Text('End', font='Arimo', stroke_width=0).scale(0.5)
        end_round_rectangle = RoundedRectangle(height=end_text.get_height()+1, width=end_text.get_width()+2)
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

class Sequential_structure_introduction(Scene) :
    def construct(self) :
        start_text = Text('Start', font='Arimo', stroke_width=0).scale(0.5)
        start_round_rectangle = RoundedRectangle(height=start_text.get_height()+1, width=start_text.get_width()+1.5)
        start_round_rectangle.set_color('#16c0ac')
        start = VGroup(start_text, start_round_rectangle)
        end_text = Text('End', font='Arimo', stroke_width=0).scale(0.5)
        end_round_rectangle = RoundedRectangle(height=end_text.get_height()+1, width=end_text.get_width()+2)
        end_round_rectangle.set_color('#78380d')
        end = VGroup(end_text, end_round_rectangle)

        step_text_list = []
        step_rectangle_list = []
        step_list = []
        step_arrow_list = []
        for i in range(1, 33) :
            text = Text('Step '+str(i), font='Arimo', stroke_width=0)
            rectangle = SurroundingRectangle(text, buff=0.5)
            rectangle.set_color(BLUE)
            step = VGroup(text, rectangle).scale(0.5)

            step_text_list.append(text)
            step_rectangle_list.append(rectangle)
            step_list.append(step)
        
        start.move_to(UP*3)
        end.move_to(DOWN*1)
        start_end_arrow = Arrow(start.get_bottom(), end.get_top(), buff=0)
        self.play(*[ShowCreation(item) for item in [start, start_end_arrow, end]])
        self.wait(2)

        step_list[0].move_to(UP*1)
        start_arrow = Arrow(start.get_bottom(), step_list[0].get_top(), buff=0)
        step_arrow_list.append(Arrow(step_list[0].get_bottom(), end.get_top(), buff=0))
        self.play(Uncreate(start_end_arrow))
        self.play(ShowCreation(step_list[0]))
        self.play(GrowArrow(start_arrow), GrowArrow(step_arrow_list[0]))
        self.wait(2)

        step_list[1].next_to(step_arrow_list[0], DOWN, buff=0)
        end.target = end.copy().next_to(step_list[1], DOWN, buff=1)
        step_arrow_list.append(Arrow(step_list[1].get_bottom(), end.target.get_top(), buff=0))
        self.play(
            ShowCreation(step_list[1]),
            MoveToTarget(end),
            GrowArrow(step_arrow_list[1])
        )
        self.wait(2)

        #Finally I give up to do the animation that shows 32 steps
        #at the same time on the screen. It's much more harder than
        #I thoutht.
        self.play(FadeOut(VGroup(*[itom for itom in self.mobjects])))
        self.wait()
        
class Case_structure_introduction(Scene) :
    def construct(self):
        start_text = Text('Start', font='Arimo', stroke_width=0).scale(0.5)
        start_round_rectangle = RoundedRectangle(height=start_text.get_height()+1, width=start_text.get_width()+1.5)
        start_round_rectangle.set_color('#16c0ac')
        start = VGroup(start_text, start_round_rectangle)
        end_text = Text('End', font='Arimo', stroke_width=0).scale(0.5)
        end_round_rectangle = RoundedRectangle(height=end_text.get_height()+1, width=end_text.get_width()+2)
        end_round_rectangle.set_color('#78380d')
        end = VGroup(end_text, end_round_rectangle)
        case_text = Text('Judgement', font='Arimo', stroke_width=0).scale(0.5)
        case_text.set_color(YELLOW)
        case_rhombus = Polygon([0, 1, 0], [2, 0, 0], [0, -1, 0], [-2, 0, 0])
        case = VGroup(case_text, case_rhombus)
        case_yes_text = Text('Yes', font='Arimo', stroke_width=0).scale(0.3)
        case_yes_text.set_color(GREEN)
        case_yes_line = Line([0, 0, 0], [-1, 0, 0])
        case_yes_line.set_color(GREEN)
        case_yes_arrow = Arrow([-1, 0, 0], [-1, -1, -1], buff=0, stroke_width=4)
        case_yes_arrow.set_color(GREEN)
        case_yes_connection_dot = Dot()
        case_yes = VGroup(case_yes_text, case_yes_line, case_yes_arrow, case_yes_connection_dot)
        case_no_text = Text('No', font='Arimo', stroke_width=0).scale(0.3)
        case_no_text.set_color(RED)
        case_no_line = Line([0, 0, 0], [1, 0, 0])
        case_no_line.set_color(RED)
        case_no_arrow = Arrow([1, 0, 0], [1, -1, 0], buff=0, stroke_width=4)
        case_no_arrow.set_color(RED)
        case_no_connection_dot = Dot()
        case_no = VGroup(case_no_text, case_no_line, case_no_arrow, case_no_connection_dot)
        def calibrite_case_yes() :
            case_yes_line.next_to(case_yes_connection_dot, LEFT, buff=0)
            case_yes_text.next_to(case_yes_line, UP, buff=0.1)
            case_yes_arrow.next_to(case_yes_line.get_left(), DOWN, buff=0)
        def calibrite_case_no() :
            case_no_line.next_to(case_no_connection_dot, RIGHT, buff=0)
            case_no_text.next_to(case_no_line, UP, buff=0.1)
            case_no_arrow.next_to(case_no_line.get_right(), DOWN, buff=0)
        #case_yes_text.next_to(case_yes_arrow, UP, buff=0.1)
        #self.add(case_yes_arrow, case_yes_text)
        #case_no_text.next_to(case_no_arrow, UP, buff=0.1)
        #self.add(case_no_arrow, case_no_text)
        case_yes_connection_dot.move_to(case.get_left())
        case_no_connection_dot.move_to(case.get_right())
        calibrite_case_yes()
        calibrite_case_no()
        self.add(case, case_yes, case_no)