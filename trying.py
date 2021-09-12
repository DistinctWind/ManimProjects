import sys
import os
sys.path.append(os.getcwd())

from manimlib import *
from utils.imports import *

class RecallingMaze(Scene) :
    def construct(self):
        maze = Maze(5, 5)
        maze.set_start(3, 3)
        maze.set_end(1, 1)

        self.play(ShowCreation(maze))
        self.wait()

        poi = Dot(color=RED).move_to(maze.get_rec(*maze.start))
        self.play(FadeIn(poi, scale=0.5))
        
        return super().construct()

class try_playing_together(Scene):
    def construct(self):
        text = Text('text')
        self.add(text)
        self.play(
            text.animate.set_color(RED),
            self.camera.frame.animate.scale(0.5)
        )
        return super().construct()