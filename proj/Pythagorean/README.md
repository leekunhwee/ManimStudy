# Pythagorean Theorem



Create scene inherit the class of `Scene`
```python3
from manimlib.imports import *
from numpy import sqrt

class Pythagoras(Scene):
    CONFIG={'scale_all': 0.75,}
    def construct(self):
        cube_kwargs={'color':WHITE,'stroke_width':1,'fill_opacity':0.6,}

        triangle_abc = Polygon(np.array([-2,0,0]),np.array([2,0,0])\
                            ,np.array([-1,sqrt(3),0]),color = WHITE\
                            ,stroke_width=2
                            )
        cube = Cube(fill_opacity = 0, stroke_width = 1).scale(0.2)\
                .shift(0.2*RIGHT+0.2*DOWN).rotate_about_origin(-PI/6)\
                .shift([-1,sqrt(3),0])
        # cube is used to denote the right angle of the triangle_abc
        triangle = VGroup(triangle_abc,cube)

        O_a, O_b, O_c = (1+sqrt(3))*(LEFT*sqrt(3)/2+UP*0.5)\
                    ,(1+sqrt(3))*(RIGHT*0.5+UP*sqrt(3)/2)\
                    ,DOWN*2
        cube_a = Cube(fill_color=BLUE, **cube_kwargs).scale(1).move_to(O_a).rotate(PI/3)
        cube_b = Cube(fill_color=RED, **cube_kwargs).scale(sqrt(3)).move_to(O_b).rotate(-PI/6)
        cube_c = Cube(fill_color=GREEN, **cube_kwargs).scale(2).move_to(O_c)

        poly_kwargs = {"color": WHITE, "strock_width":2, "fill_opacity":0.9,}
        poly_01 = Polygon(O_b, O_b + DOWN * 2, RIGHT * 2, O_b + RIGHT * 2, fill_color = PINK, **poly_kwargs)

        poly_02 = Polygon(O_b, O_b + RIGHT * 2, (2+sqrt(3)) * RIGHT +3 * UP, O_b + UP * 2, fill_color = ORANGE, **poly_kwargs)

        poly_03 = Polygon(O_b, O_b + DOWN * 2, RIGHT * 2, O_b + RIGHT * 2, fill_color = PINK, **poly_kwargs)\
                .scale_about_point(-1, O_b)
        poly_04 = Polygon(O_b, O_b + RIGHT * 2, (2+sqrt(3)) * RIGHT +3 * UP, O_b + UP * 2, fill_color = ORANGE, **poly_kwargs)\
                .scale_about_point(-1, O_b)
        poly_group = VGroup(poly_01, poly_02, poly_03, poly_04)

        group_all = VGroup(triangle, cube_a, cube_b, cube_c, poly_group).scale_about_point(self.scale_all, ORIGIN)

        self.play(FadeIn(triangle_abc),FadeIn(cube)), self.wait(0)
        self.play(FadeIn(cube_a)), self.play(FadeIn(cube_b)), self.play(FadeIn(cube_c)), self.wait()
        self.play(FadeIn(poly_group)), self.wait(0)

        self.play(ApplyMethod(poly_01.copy().shift, (LEFT * 2 - O_b) * self.scale_all)), self.wait(0.5)
        self.play(ApplyMethod(poly_02.copy().shift, (LEFT * 2 + DOWN * 4 - O_b) * self.scale_all)), self.wait(0.5)
        self.play(ApplyMethod(poly_03.copy().shift, (RIGHT * 2 + DOWN * 4 - O_b) * self.scale_all)), self.wait(0.5)
        self.play(ApplyMethod(poly_04.copy().shift, (RIGHT * 2 - O_b) * self.scale_all)), self.wait(0.5)
        self.play(ApplyMethod(cube_a.copy().shift, (O_c - O_a) * self.scale_all)), self.wait(2)
```

<p align="center"><img src ="Pythagoras.gif" /></p>
