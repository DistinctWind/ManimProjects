from manimlib.imports import *

class Alogorithm_introduction(Scene) :
    def construct(self) :
        title = Text('算法的特点', font='Dent', stroke_width=0).to_corner(UL)
        self.play(Write(title))
        self.wait(2)

        effectiveness_text = Text('可行性', font='Dent', stroke_width=0).scale(0.6)
        finiteness_text = Text('有穷性', font='Dent', stroke_width=0).scale(0.6)
        definiteness_text = Text('确切性', font='Dent', stroke_width=0).scale(0.6)
        input_text = Text('输入性', font='Dent', stroke_width=0).scale(0.6)
        output_text = Text('输出性', font='Dent', stroke_width=0).scale(0.6)
        finiteness_text.next_to(effectiveness_text, DL, buff=1)
        definiteness_text.next_to(effectiveness_text, DR, buff=1)
        input_text.next_to(finiteness_text, DL, buff=1)
        output_text.next_to(definiteness_text, DR, buff=1)
        effectiveness_text.shift(UP*2)
        definiteness_text.shift(UP)
        finiteness_text.shift(UP)

        ef_arrow = Arrow(effectiveness_text.get_bottom(), finiteness_text.get_top())
        ed_arrow = Arrow(effectiveness_text.get_bottom(), definiteness_text.get_top())
        fi_arrow = Arrow(finiteness_text.get_bottom(), finiteness_text.get_bottom()+DOWN*2.41)
        do_arrow = Arrow(definiteness_text.get_bottom(), definiteness_text.get_bottom()+DOWN*2.41)
        io_arrow = Arrow(input_text.get_right(), output_text.get_left())

        ef_arrow.set_color(GREEN)
        ed_arrow.set_color(GREEN)
        fi_arrow.set_color(YELLOW)
        do_arrow.set_color(YELLOW)
        io_arrow.set_color(RED)
        self.play(Write(effectiveness_text))
        self.play(GrowArrow(ef_arrow), GrowArrow(ed_arrow))
        self.play(Write(definiteness_text), Write(finiteness_text))
        self.play(Write(input_text), Write(output_text))
        self.play(GrowArrow(io_arrow))
        self.play(GrowArrow(fi_arrow), GrowArrow(do_arrow))
        self.wait(2)
        
        self.play(FadeOut(VGroup(*self.mobjects)))

        title = Text('算法', font='Dent', stroke_width=0).to_edge(UP)
        self.play(Write(title))
        introduction_text = Text('通过一定的步骤来解决一类问题的方法', font='Dent', stroke_width=0).scale(0.7)
        add_introduction_text = Text('通常由计算机代劳', font='Dent', stroke_width=0).scale(0.5)
        add_introduction_text.to_edge(DOWN)
        step_list = []
        step_list.append(Text('先告诉计算机你想要什么', font='Dent', stroke_width=0).scale(0.3))
        step_list.append(Text('告诉计算机要怎么做', font='Dent', stroke_width=0).scale(0.3))
        step_list.append(Text('计算机把得到的答案给你', font='Dent', stroke_width=0).scale(0.3))
        result_list = []
        result_list.append(Text('输入性', font='Dent', stroke_width=0).scale(0.3))
        result_list.append(Text('可行性 | 确切性 | 有效性', font='Dent', stroke_width=0).scale(0.3))
        result_list.append(Text('输出性', font='Dent', stroke_width=0).scale(0.3))
        arrow_list = []
        step_list[0].move_to(introduction_text.get_left()+DOWN+RIGHT)
        step_list[1].next_to(step_list[0], DOWN, buff=0.25)
        step_list[2].next_to(step_list[1], DOWN, buff=0.25)
        result_list[0].move_to(introduction_text.get_right()+DOWN+LEFT)
        result_list[1].next_to(result_list[0], DOWN, buff=0.25)
        result_list[2].next_to(result_list[1], DOWN, buff=0.25)

        for step, result in zip(step_list, result_list) :
            arrow_list.append(Arrow(step.get_right(), result.get_left(), stroke_width=2).set_color(RED))
        VGroup(
            add_introduction_text[3],
            add_introduction_text[4],
            add_introduction_text[5],
        ).set_color(GREEN_SCREEN)
        self.play(Write(introduction_text))
        self.wait()
        self.play(Write(add_introduction_text))
        self.wait()
        self.play(Write(VGroup(*step_list)))
        self.wait()
        self.play(Write(VGroup(*result_list)))
        self.play(*[GrowArrow(arrow) for arrow in arrow_list])
        self.wait()

        self.play(FadeOut(VGroup(*self.mobjects)))

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
        end_round_rectangle = RoundedRectangle(height=start.get_height(), width=start.get_width())
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
        end_round_rectangle = RoundedRectangle(height=start.get_height(), width=start.get_width())
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
        self.play(FadeOut(start), FadeOut(end))
        self.wait(2)
        self.play(FadeOut(VGroup(*[itom for itom in self.mobjects])))
        self.wait()
        
class Case_structure_introduction(Scene) :
    def construct(self):
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
        case_yes_connection_dot = Dot().scale(0.1)
        case_yes = VGroup(case_yes_text, case_yes_line, case_yes_arrow)
        case_no_text = Text('No', font='Arimo', stroke_width=0).scale(0.3)
        case_no_text.set_color(RED)
        case_no_line = Line([0, 0, 0], [1, 0, 0])
        case_no_line.set_color(RED)
        case_no_arrow = Arrow([1, 0, 0], [1, -1, 0], buff=0, stroke_width=4)
        case_no_arrow.set_color(RED)
        case_no_connection_dot = Dot().scale(0.1)
        case_no = VGroup(case_no_text, case_no_line, case_no_arrow)
        step_yes_text = Text('Yes Action', font='Arimo', stroke_width=0)
        step_yes_text.set_color(GREEN)
        step_yes_rectangle = SurroundingRectangle(step_yes_text, buff=0.5)
        step_yes_rectangle.set_color(GREEN)
        step_yes = VGroup(step_yes_rectangle, step_yes_text).scale(0.5)
        step_no_text = Text('No Action', font='Arimo', stroke_width=0)
        step_no_text.set_color(RED)
        step_no_rectangle = SurroundingRectangle(step_no_text, buff=0.5)
        step_no_rectangle.set_color(RED)
        step_no = VGroup(step_no_rectangle, step_no_text).scale(0.5)

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
        step_yes.next_to(case_yes_arrow, DOWN, buff=0)
        step_no.next_to(case_no_arrow, DOWN, buff=0)
        start_arrow = Arrow(case.get_top()+UP, case.get_top(), buff=0, stroke_width=4)
        
        self.play(GrowArrow(start_arrow), ShowCreation(case))
        self.wait(2)
        self.play(ShowCreation(case_yes), ShowCreation(case_no))
        self.play(ShowCreation(step_yes), ShowCreation(step_no))
        self.wait(2)
        self.play(*[ApplyMethod(item.shift, UP*1.5) for item in self.mobjects])
        self.wait(2)
        case_arrow = Arrow(case.get_bottom(), case.get_bottom()+DOWN*1.5, buff=0, stroke_width=4)
        start_to_case_arrow = Arrow(step_yes.get_right(), step_yes.get_right()+RIGHT*1.6, buff=0, stroke_width=4)
        start_to_case_arrow.set_color(GREEN)
        self.play(ReplacementTransform(VGroup(case_no, step_no), case_arrow))
        self.play(GrowArrow(start_to_case_arrow))
        self.wait(2)
        self.play(FadeOut(VGroup(*[item for item in self.mobjects])))
        self.wait(2)

class Loop_structure_introduction(Scene) :
    def construct(self):
        title = Text('直到型循环', font='WenQuanYi Zen Hei', stroke_width=0).scale(0.7)
        title.to_corner(UL)
        start_arrow = Arrow([0, 0, 0], [0, -1, 0], stroke_width=4, buff=0)
        start_arrow.move_to(UP*2)
        loop_body_text = Text('Loop Body', font='Arimo', stroke_width=0).scale(0.7)
        loop_body_rectangle = Polygon([2, 1, 0], [2, -1, 0], [-2, -1, 0], [-2, 1, 0])
        loop_body = VGroup(loop_body_text, loop_body_rectangle).scale(0.5)
        case_text = Text('Judgement', font='Arimo', stroke_width=0).scale(0.5)
        case_text.set_color(YELLOW)
        case_rhombus = Polygon([0, 1, 0], [2, 0, 0], [0, -1, 0], [-2, 0, 0])
        case = VGroup(case_text, case_rhombus).scale(0.7)
        case_yes_arrow = Arrow(case.get_bottom(), case.get_bottom()+DOWN, stroke_width=4, buff=0)
        case_yes_text = Text('Yes', font='Arimo', stroke_width=0).scale(0.3)
        case_yes = VGroup(case_yes_arrow, case_yes_text)
        case_yes.set_color(GREEN)
        case_no_level_line = Line(case.get_right(), case.get_right()+RIGHT)
        case_no_vertical_line = Line(case_no_level_line.get_right(), case_no_level_line.get_right()+UP*3.3)
        case_no_arrow = Arrow(case_no_vertical_line.get_top(), case_no_vertical_line.get_top()+LEFT*2.4, stroke_width=4, buff=0)
        case_no_text = Text('No', font='Arimo', stroke_width=0).scale(0.3)
        case_no = VGroup(case_no_level_line, case_no_vertical_line, case_no_arrow, case_no_text)
        case_no.set_color(RED)

        loop_body.next_to(start_arrow, DOWN, buff=0)
        loop_case_connection_arrow = Arrow(loop_body.get_bottom(), loop_body.get_bottom()+DOWN, stroke_width=4, buff=0)
        loop_case_connection_arrow.next_to(loop_body, DOWN, buff=0)
        case.next_to(loop_case_connection_arrow, DOWN, buff=0)
        case_no_level_line.next_to(case, RIGHT, buff=0)
        case_no_vertical_line.next_to(case_no_level_line.get_right(), UP, buff=0)
        case_no_arrow.next_to(case_no_vertical_line.get_top(), LEFT, buff=0)
        case_no_text.next_to(case_no_level_line, UP, buff=0.1)
        case_yes_arrow.next_to(case, DOWN, buff=0)
        case_yes_text.next_to(case_yes_arrow, RIGHT, buff=0.1)
        
        self.play(Write(title))
        self.wait()
        self.play(GrowArrow(start_arrow))
        self.wait()
        self.play(ShowCreation(loop_body))
        self.wait()
        self.play(GrowArrow(loop_case_connection_arrow))
        self.wait()
        self.play(ShowCreation(case))
        self.wait()
        self.play(ShowCreation(case_no))
        self.wait()
        self.play(ShowCreation(case_yes))
        self.wait(2)
        
        self.play(FadeOut(VGroup(*[item for item in self.mobjects])))
        self.wait()
        
        title = Text('当型循环', font='WenQuanYi Zen Hei', stroke_width=0)
        title.scale(0.7)
        level_line = Line([0, 0, 0], [1, 0, 0])
        vertical_line = Line([0, 0, 0], [0, 3.4, 0])
        arrow = Arrow([0, 0, 0], [-2.5, 0, 0], stroke_width=4)
        case_no_arrow = Arrow([0, 0, 0], [0, -1, 0], stroke_width=4)
        case_no_arrow.set_color(RED)

        title.to_corner(UL)
        case.next_to(start_arrow, DOWN, buff=0)
        case_yes_arrow.next_to(case, DOWN, buff=0)
        loop_body.next_to(case_yes_arrow, DOWN, buff=0)
        level_line.next_to(loop_body, RIGHT, buff=0)
        vertical_line.next_to(level_line.get_right(), UP, buff=0)
        arrow.next_to(vertical_line.get_top(), LEFT, buff=0)
        case_no_level_line.next_to(case, LEFT, buff=0)
        case_no_arrow.next_to(case_no_level_line.get_left(), DOWN, buff=0)
        case_yes_text.next_to(case_yes_arrow, RIGHT, buff=0.1)
        case_no_text.next_to(case_no_level_line, UP, buff=0.1)
        self.play(Write(title))
        self.wait()
        self.play(GrowArrow(start_arrow))
        self.play(ShowCreation(case))
        self.wait()
        self.play(GrowArrow(case_yes_arrow), Write(case_yes_text))
        self.play(ShowCreation(loop_body))
        self.play(ShowCreation(level_line))
        self.play(ShowCreation(vertical_line))
        self.play(GrowArrow(arrow))
        self.play(ShowCreation(case_no_level_line), ShowCreation(case_no_arrow), Write(case_no_text))
        self.wait(2)