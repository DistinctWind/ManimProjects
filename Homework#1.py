from manimlib.imports import *
from numpy import *
import math

class BeginScene(Scene) :
    def construct(self) :
        title = Text("Manim Homework Vol.1", font='msyh', stroke_width=0)
        author = Text("Made by @DistinctWind", font='msyh', stroke_width=0).scale(0.5)
        title.move_to(UP*0.5)
        author.move_to(DOWN*0.5)
        self.play(Write(title))
        self.play(Write(author))
        self.wait(2)

class Main(Scene) :
    def construct(self) :
        plane = NumberPlane().set_color(WHITE)
        self.add(plane)

        tri = Polygon(array([-1,0,0]), array([2,0,0]), array([0,math.sqrt(3),0]))
        tri.set_fill(BLUE)
        tri.set_opacity(0.5)
        a_text = TextMobject("a")
        a_text.move_to(array([-0.75,1,0]))
        b_text = TextMobject("b")
        b_text.move_to(array([1.1,1.2,0]))
        c_text = TextMobject("c")
        c_text.move_to(array([0.5,-0.3,0]))
        Tri = VGroup(tri, a_text, b_text, c_text)
        self.play(ShowCreation(tri), *[Write(text) for text in [a_text, b_text, c_text]])
        self.wait()

        rec1 = Polygon(array([-1,0,0]), array([-1,-3,0]), array([2,-3,0]), array([2,0,0]))
        rec1.set_color(GREEN)
        rec1.set_fill(GREEN)
        rec1.set_opacity(0.5)
        rec2 = Polygon(array([-1,0,0]), array([0,math.sqrt(3),0]), array([-1.73,2.73,0]), array([-2.73,1,0]))
        rec2.set_color(GREEN)
        rec2.set_fill(GREEN)
        rec2.set_opacity(0.5)
        rec3 = Polygon(array([0,1.73,0]),array([2,0,0]),array([3.73,2,0]),array([1.73,3.73,0]))
        rec3.set_color(GREEN)
        rec3.set_fill(GREEN)
        rec3.set_opacity(0.5)
        Recs = VGroup(rec1, rec2, rec3)
        self.play(ShowCreation(Recs))
        self.wait()

        tri1 = Polygon(array([-1.73,2.73,0]), array([1.73,3.73,0]), array([0,1.73,0]))
        tri1.set_fill(BLUE_A)
        tri1.set_opacity(0.5)
        s1 = TexMobject("S_1").move_to(tri1.get_center()).scale(1.25)

        tri2 = Polygon(array([3.73,2,0]), array([2,-3,0]), array([2,0,0]))
        tri2.set_fill(BLUE_B)
        tri2.set_opacity(0.5)
        s2 = TexMobject("S_2").move_to(tri2.get_center()).scale(1.25)

        tri3 = Polygon(array([-1,-3,0]), array([-2.73,1,0]), array([-1,0,0]))
        tri3.set_fill(BLUE_E)
        tri3.set_opacity(0.5)
        s3 = TexMobject("S_3").move_to(tri3.get_center()).scale(1.25)

        self.play(*[ShowCreation(t) for t in [tri1, tri2, tri3]])
        self.play(*[Write(t) for t in [s1, s2, s3]])
        self.wait()
        self.play(*[FadeOut(r) for r in [rec1, rec2, rec3]])
        self.wait()

        self.play(
            ApplyMethod(tri1.rotate, PI/2, {"about_point": array([0,math.sqrt(3),0])}),
            ApplyMethod(tri2.rotate, PI/2, {"about_point": array([2,0,0])}),
            ApplyMethod(tri3.rotate, PI/2, {"about_point": array([-1,0,0])}),
        )
        #tri1.rotate(PI/2, about_point=array([0,math.sqrt(3),0]))
        #tri2.rotate(PI/2, about_point=array([2,0,0]))
        #tri3.rotate(PI/2, about_point=array([-1,0,0]))
        self.play(
            *[ApplyMethod(mtext.move_to, mtri.get_center()) for mtext,mtri in [(a_text,tri1), (b_text,tri2), (c_text,tri3)]]
        )
        self.wait()

        s = TexMobject("S").move_to(tri.get_center()).scale(1.5)
        self.play(Write(s))

        self.wait(2)