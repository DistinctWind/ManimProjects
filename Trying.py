from manimlib.imports import *
import numpy

class Underline(Scene) :
    def construct(self) :
        greet = TextMobject("HELLO", "WORLD")
        dbrace = Brace(greet[0], DOWN)
        ubrace = Brace(greet[1], UP)
        dtext = dbrace.get_text("down")
        utext = ubrace.get_text("up")

        self.play(Write(greet))
        self.play(GrowFromCenter(dbrace), GrowFromCenter(ubrace))
        self.wait()
        self.play(FadeIn(dtext), FadeIn(utext))
        self.wait()

class FrameBox2(Scene):
    def construct(self):
        text=TexMobject(
            "\\hat g(", "f", ")", "=", "\\int", "_{t_1}", "^{t_{2}}",
            "g(", "t", ")", "e", "^{-2\\pi i", "f", "t}", "dt"
        )
        seleccion=VGroup(text[4],text[5],text[6])
        frameBox = SurroundingRectangle(seleccion, buff = 0.5*SMALL_BUFF)
        frameBox.set_stroke(GREEN,3)
        self.play(Write(text))
        self.wait(.5)
        self.play(ShowCreation(frameBox))
        self.wait(2)

class ChangeSize(Scene):
    def construct(self):
        text = TexMobject("\\sum_{i=0}^n i=\\frac{n(n+1)}{2}")
        self.play(Write(text))
        text.scale_in_place(2)
        self.wait()
        text.scale_in_place(0.5)
        self.wait()
        text.scale(2)
        self.wait()
        text.scale(0.5)
        self.wait()

class ColorByCaracter(Scene):
	def construct(self):
		text = TexMobject("{d","\\over","d","x}","\\int^","x_","a","f(","t",")d","t","=","f(","x",")")
		text.set_color_by_tex("x",RED)
		self.play(Write(text))
		self.wait(2)

class Sizes(Scene) :
    def construct(self) :
        textHuge = TextMobject("{\\Huge Huge Text 012.\\#!?} Text")
        self.add(textHuge)

class FlipObject(Scene) :
    def construct(self) :
        up = TextMobject("UP")
        down = TextMobject("DOWN")
        left = TextMobject("LEFT")
        right = TextMobject("RIGHT")

        up.flip(UP)
        up.move_to(UP)
        down.flip(DOWN)
        down.move_to(DOWN)
        left.flip(LEFT)
        left.move_to(LEFT)
        right.flip(RIGHT)
        right.move_to(RIGHT)

        self.play(Write(up), Write(down), Write(left), Write(right))
        self.wait(3)

class Roating(Scene) :
    def construct(self) :
        text = TextMobject("Hi! How do you do?")
        self.play(ShowCreation(text))
        self.wait()
        self.play(ApplyMethod(text.rotate, PI/4))
        self.wait()
        self.play(ApplyMethod(text.rotate, PI/4))
        self.wait()
        self.play(ApplyMethod(text.rotate, PI/2))
        self.wait()
        self.play(ApplyMethod(text.rotate, PI))
        self.wait()

class Shoot(Scene) :
    def construct(self) :
        c1 = Circle(color=BLUE)
        c2 = Circle(color=RED, fill_color=RED, fill_opacity=1)
        c2.scale(0.1)
        l1 = Line(np.array([-1, 0, 0]), np.array([1, 0, 0]))
        l2 = Line(np.array([0, -1, 0]), np.array([0, 1, 0]))
        scope = VGroup(c1, c2, l1, l2)
        
        t = []
        lr = np.array([-4, -2, 0])
        for i in range(3) :
            for j in range(5) :
                c = Circle(color=YELLOW, fill_color=YELLOW, fill_opacity=0.5)
                c.scale(0.5)
                t.append(c)
                self.play(FadeIn(c), run_time=0.1)
                self.play(ApplyMethod(c.move_to, lr+UP*i*2+RIGHT*j*2), run_time=0.1)
        
        def shoot(x, y) :
            self.play(ApplyMethod(scope.move_to, lr+UP*x*2+RIGHT*y*2))
            t[x*5+y].target = Circle(color=GRAY, fill_color=GRAY, fill_opacity=0.5)
            t[x*5+y].target.move_to(lr+UP*x*2+RIGHT*y*2)
            t[x*5+y].target.scale(0.5)
            scope.target = scope.copy()
            scope.set_color(RED)
            scope.scale(2)
            self.play(MoveToTarget(t[x*5+y]), MoveToTarget(scope), run_time = 0.5)
            self.wait()
            text = TextMobject('$('+str(x)+', '+str(y)+')$')
            text.next_to(t[x*5+y], DOWN*0.1)
            self.play(FadeIn(text))

        shoot(0,1)
        shoot(1,4)
        shoot(2,0)
        shoot(0,3)
        
        

class Function_t(Scene) :
    CONFIG = {
        "axis_config": {
            "include_ticks": True,
            "include_tip": True,
        },
        "x_line_frequency": 2,
    }
    def f(self, x) :
        return 2**x
    def construct(self) :
        tip = TextMobject("$f(x)=a^x$")
        tip.to_corner(UL)
        plane = NumberPlane()
        
        graph = plane.get_graph(self.f)
        
        self.play(ShowCreation(plane))
        self.wait()
        self.play(ShowCreation(graph))
        self.wait(3)

class Basic_shape(GraphScene) :
    def construct(self) :
        line = Line(np.array([0, 3.6, 0]), np.array([0, 2, 0]), color=BLUE)
        ring = Annulus(inner_radius=0.4, outer_radius=1, color=BLUE)
        square = Square(color=ORANGE, fill_color=ORANGE, fill_opacity=0.5)
        rect = Rectangle(height=3.2, width=1.2, color=PINK, fill_color=PINK, fill_opacity=0.3)
        line1 = Line(np.array([-1, 2 ,0]), np.array([-1, -1, 0]), color=RED)
        line2 = Line(np.array([1, 2, 0]), np.array([1, 0, 0]), color=RED)

        ring.shift(UP*2)
        square.shift(LEFT + DOWN*2)
        rect.shift(RIGHT + DOWN*(3.2/2))

        plane = NumberPlane()
        self.play(ShowCreation(plane), run_time=1.41)
        self.wait()

        self.add(line)
        self.play(GrowFromCenter(ring))
        self.wait()
        self.play(FadeInFromDown(line1), FadeInFromDown(line2))
        self.wait()
        self.play(ShowCreation(square), ShowCreation(rect))
        self.wait(3)

        self.play(Uncreate(plane), run_time=1.41)

class Fun(Scene) :
    def construct(self) :
        greet = TextMobject("你好鸭", color = WHITE)
        rec = Rectangle(color = BLUE)
        rec.surround(greet)
        group1 = VGroup(greet, rec)

        self.play(Write(greet))
        self.wait()
        self.play(FadeInFromLarge(rec, scale_factor=1.5))
        self.wait()
        

        greet.target = TextMobject("Hello!", color = GREEN)
        greet.target.scale(2.5)

        self.play(
            ApplyMethod(group1.scale, 2.5)
        )
        self.play(
            ApplyMethod(rec.set_color, RED),
            MoveToTarget(greet)
        )
        self.wait()

class Graph2D(GraphScene) :
    CONFIG = {
        "x_min": -5,
        "x_max": 5,
        "y_min": 0,
        "y_max": 25,
        "graph_origin": DOWN*2.5
    }
    def f(self, x) :
        return x**2
    def construct(self) :
        self.setup_axes(True)
        graph = self.get_graph(self.f, color=RED, x_min=-5, x_max=5)
        self.play(ShowCreation(graph), run_time = 2)
        self.wait(2)

class mgird(Scene) :
    def construct(self) :
        gird = NumberPlane()
        self.add(gird)
        self.wait(3)

class corner(Scene) :
    def construct(self) :
        ul = Dot()
        ur = Dot()
        dr = Dot()
        dl = Dot()
        ul.to_corner(UL)
        ul.set_color(RED)
        ur.to_corner(UR)
        ur.set_color(RED)
        dl.to_corner(DL)
        dl.set_color(RED)
        dr.to_corner(DR)
        dr.set_color(RED)

        ult = TextMobject("UPANDLEFTPOINT")
        urt = TextMobject("UPANDRIGHTPOINT")
        drt = TextMobject("DOWNANDRIGHTPOINT")
        dlt = TextMobject("DOWNANDLEFTPOINT")
        ult.next_to(ul, RIGHT*0.5 + DOWN*0.5)
        urt.next_to(ur, LEFT*0.5 + DOWN*0.5)
        drt.next_to(dr, LEFT*0.5 + UP*0.5)
        dlt.next_to(dl, RIGHT*0.5 + UP*0.5)
        self.play(
            ShowCreation(ul), 
            ShowCreation(ur), 
            ShowCreation(dr),
            ShowCreation(dl),
        )
        self.wait(2)
        self.play(
            Write(ult), 
            Write(urt), 
            Write(drt), 
            Write(dlt),
        )

class PlayMethods(Scene) :
    def construct(self) :
        fade = TextMobject("Fade")
        creation = TextMobject("ShowCreation")
        border = TextMobject("Border")
        write = TextMobject("Write")

        fade.move_to(UP*2)
        creation.move_to(DOWN*2)
        border.move_to(LEFT*2)
        write.move_to(RIGHT*2)

        self.play(
                FadeIn(fade), 
                ShowCreation(creation), 
                DrawBorderThenFill(border), 
                Write(write)
            )
        self.wait(2)
        self.play(FadeOut(fade), Uncreate(creation))
        self.wait(2)
        self.play(FadeInFromDown(fade))
        self.wait(2)
        self.play(FadeOutAndShiftDown(fade))
        self.wait(2)

class WriteText(Scene) :
    def construct(self) :
        t = TextMobject("text")
        self.wait(2)
        self.play(Write(t))
        t.target = TextMobject("HI!")
        t.target.set_color(RED)
        t.target.shift(LEFT)
        self.wait(2)
        self.play(MoveToTarget(t), run_time = 2)

class TextArray(Scene):
    def construct(self) :
        text = TextMobject("text0", "text1", "text2")
        text[0].move_to(UP*2)
        text[2].move_to(DOWN*2)
        self.wait(2)
        self.play(Transform(text[0], text[1]))
        self.wait(2)
        self.play(Transform(text[1], text[2]))
        self.wait(2)

        text[0].move_to(LEFT)
        text[1].move_to(LEFT)
        text[2].move_to(LEFT)
        self.play(Write(text[0]), Write(text[1]), Write(text[2]))
        self.wait(2)