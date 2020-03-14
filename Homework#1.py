from manimlib.imports import *
import numpy
import math

class BeginScene(Scene) :
    def construct(self) :
        title = Text("Manim Homework Vol.1", font='calibri')
        author = Text("Made by @DistinctWind", font='calibri').scale(0.5)
        title.move_to(UP*0.5)
        author.move_to(DOWN*0.5)
        self.play(Write(title))
        self.play(Write(author))
        self.wait(2)
