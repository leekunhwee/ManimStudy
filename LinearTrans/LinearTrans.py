# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 17:13:50 2020

@author: alexlee.stu
"""

from manimlib.imports import *

class FirstLinearTransformation(LinearTransformationScene):
    def construct(self):
        mob = Circle(color=PURPLE)
        mob.move_to(RIGHT+UP*2)
        vector_array1 = np.array([[1], [2]])
        vector_array2 = np.array([[2], [1]])
        matrix = [[2, 0], [1, 1]]
        
        self.add_transformable_mobject(mob)
        self.add_vector(vector_array1,color=YELLOW)
        self.add_vector(vector_array2,color=BLUE)
        self.apply_matrix(matrix)
        self.wait(3)
        
class SecondLinearTransformation(LinearTransformationScene):
    CONFIG = {
        "include_background_plane": True,
        "include_foreground_plane": True,
        "foreground_plane_kwargs": {
            "x_max": 2*FRAME_WIDTH / 2,
            "x_min": -2*FRAME_WIDTH / 2,
            "y_max": 2*FRAME_WIDTH / 2,
            "y_min": -2*FRAME_WIDTH / 2,
            "faded_line_ratio": 0
        },
        "background_plane_kwargs": {
            "color": GREY,
            "axis_config": {
                "stroke_color": LIGHT_GREY,
            },
            "axis_config": {
                "color": GREY,
            },
            "background_line_style": {
                "stroke_color": GREY,
                "stroke_width": 1,
            },
        },
        "show_coordinates": True,
        "show_basis_vectors": True,
        "basis_vector_stroke_width": 6,
        "i_hat_color": GREEN,
        "j_hat_color": RED,
        "leave_ghost_vectors": False,
    }
    def construct(self):
        mob = Circle(color=PURPLE)
        mob.move_to(RIGHT+UP*2)
        vector_array1 = np.array([[1], [2]])
        vector_array2 = np.array([[2], [1]])
        matrix = [[2, 0], [1, 1]]
        title1 = TexMobject(r"\left[ {\begin{array}{*{20}{c}}2&0\\1&1\end{array}} \right]\cdot\
                            \left[ {\begin{array}{*{20}{c}}1\\0\end{array}} \right]=\
                            \left[ {\begin{array}{*{20}{c}}2\\1\end{array}} \right]").set_color(GREEN)
        title2 = TexMobject(r"\left[ {\begin{array}{*{20}{c}}2&0\\1&1\end{array}} \right]\cdot\
                            \left[ {\begin{array}{*{20}{c}}0\\1\end{array}} \right]=\
                            \left[ {\begin{array}{*{20}{c}}0\\1\end{array}} \right]").set_color(RED)
        title3 = TexMobject(r"\left[ {\begin{array}{*{20}{c}}2&0\\1&1\end{array}} \right]\cdot\
                            \left[ {\begin{array}{*{20}{c}}1\\2\end{array}} \right]=\
                            \left[ {\begin{array}{*{20}{c}}2\\3\end{array}} \right]").set_color(YELLOW)
        title4 = TexMobject(r"\left[ {\begin{array}{*{20}{c}}2&0\\1&1\end{array}} \right]\cdot\
                            \left[ {\begin{array}{*{20}{c}}2\\1\end{array}} \right]=\
                            \left[ {\begin{array}{*{20}{c}}4\\3\end{array}} \right]").set_color(BLUE)
        TextGroup=VGroup(title1,title2,title3,title4).arrange_submobjects(DOWN,aligned_edge=LEFT,buff=0.5).shift(4*LEFT)
        
        self.add_transformable_mobject(mob)
        self.add_vector(vector_array1,color=YELLOW)
        self.add_vector(vector_array2,color=BLUE)
        self.apply_matrix(matrix)
        self.add_title(TextGroup,animate=True)
        self.wait(3)
        
class ThirdLinearTransformation(LinearTransformationScene):
    CONFIG = {
        "include_background_plane": True,
        "include_foreground_plane": True,
        "foreground_plane_kwargs": {
            "x_max": 2*FRAME_WIDTH / 2,
            "x_min": -2*FRAME_WIDTH / 2,
            "y_max": 2*FRAME_WIDTH / 2,
            "y_min": -2*FRAME_WIDTH / 2,
            "faded_line_ratio": 0
        },
        "background_plane_kwargs": {
            "color": GREY,
            "axis_config": {
                "stroke_color": LIGHT_GREY,
            },
            "axis_config": {
                "color": GREY,
            },
            "background_line_style": {
                "stroke_color": GREY,
                "stroke_width": 1,
            },
        },
        "show_coordinates": True,
        "show_basis_vectors": True,
        "basis_vector_stroke_width": 6,
        "i_hat_color": GREEN,
        "j_hat_color": RED,
        "leave_ghost_vectors": False,
    }
    def construct(self):
        mob = Circle(color=PURPLE)
        mob.move_to(RIGHT+UP*2)
        vector_array1 = np.array([[1], [2]])
        vector_array2 = np.array([[2], [1]])
        matrix = [[0, -1], [1, 0]]
        title11 = TexMobject(r"\left[ {\begin{array}{*{20}{c}}0&-1\\1&0\end{array}} \right]\cdot\
                            \left[ {\begin{array}{*{20}{c}}1\\0\end{array}} \right]=\
                            \left[ {\begin{array}{*{20}{c}}0\\1\end{array}} \right]").set_color(GREEN)
        title21 = TexMobject(r"\left[ {\begin{array}{*{20}{c}}0&-1\\1&0\end{array}} \right]\cdot\
                            \left[ {\begin{array}{*{20}{c}}0\\1\end{array}} \right]=\
                            \left[ {\begin{array}{*{20}{c}}-1\\0\end{array}} \right]").set_color(RED)
        title31 = TexMobject(r"\left[ {\begin{array}{*{20}{c}}0&-1\\1&0\end{array}} \right]\cdot\
                            \left[ {\begin{array}{*{20}{c}}1\\2\end{array}} \right]=\
                            \left[ {\begin{array}{*{20}{c}}-2\\1\end{array}} \right]").set_color(YELLOW)
        title41 = TexMobject(r"\left[ {\begin{array}{*{20}{c}}0&-1\\1&0\end{array}} \right]\cdot\
                            \left[ {\begin{array}{*{20}{c}}2\\1\end{array}} \right]=\
                            \left[ {\begin{array}{*{20}{c}}-1\\2\end{array}} \right]").set_color(BLUE)
        TextGroup1=VGroup(title11,title21,title31,title41).arrange_submobjects(DOWN,aligned_edge=LEFT,buff=0.5).shift(3.5*RIGHT)
        title12 = TexMobject(r"\left[ {\begin{array}{*{20}{c}}0&1\\-1&0\end{array}} \right]\cdot\
                            \left[ {\begin{array}{*{20}{c}}0\\1\end{array}} \right]=\
                            \left[ {\begin{array}{*{20}{c}}1\\0\end{array}} \right]").set_color(GREEN)
        title22 = TexMobject(r"\left[ {\begin{array}{*{20}{c}}0&1\\-1&0\end{array}} \right]\cdot\
                            \left[ {\begin{array}{*{20}{c}}-1\\0\end{array}} \right]=\
                            \left[ {\begin{array}{*{20}{c}}0\\1\end{array}} \right]").set_color(RED)
        title32 = TexMobject(r"\left[ {\begin{array}{*{20}{c}}0&1\\-1&0\end{array}} \right]\cdot\
                            \left[ {\begin{array}{*{20}{c}}-2\\1\end{array}} \right]=\
                            \left[ {\begin{array}{*{20}{c}}1\\2\end{array}} \right]").set_color(YELLOW)
        title42 = TexMobject(r"\left[ {\begin{array}{*{20}{c}}0&1\\-1&0\end{array}} \right]\cdot\
                            \left[ {\begin{array}{*{20}{c}}-1\\2\end{array}} \right]=\
                            \left[ {\begin{array}{*{20}{c}}2\\1\end{array}} \right]").set_color(BLUE)
        TextGroup2=VGroup(title12,title22,title32,title42).arrange_submobjects(DOWN,aligned_edge=LEFT,buff=0.5).shift(3.5*LEFT)
                            
        self.add_transformable_mobject(mob)
        self.add_vector(vector_array1,color=YELLOW)
        self.add_vector(vector_array2,color=BLUE)
        self.apply_matrix(matrix)
        self.add_title(TextGroup1,animate=True)
        self.wait(3)
        self.play(FadeOut(TextGroup1))
        self.apply_inverse(matrix) 
        self.add_title(TextGroup2,animate=True)
        self.wait(3)
        
class FourthLinearTransformation(LinearTransformationScene):
    CONFIG = {
        "include_background_plane": True,
        "include_foreground_plane": True,
        "foreground_plane_kwargs": {
            "x_max": 2*FRAME_WIDTH / 2,
            "x_min": -2*FRAME_WIDTH / 2,
            "y_max": 2*FRAME_WIDTH / 2,
            "y_min": -2*FRAME_WIDTH / 2,
            "faded_line_ratio": 0
        },
        "background_plane_kwargs": {
            "color": GREY,
            "axis_config": {
                "stroke_color": LIGHT_GREY,
            },
            "axis_config": {
                "color": GREY,
            },
            "background_line_style": {
                "stroke_color": GREY,
                "stroke_width": 1,
            },
        },
        "show_coordinates": True,
        "show_basis_vectors": True,
        "basis_vector_stroke_width": 6,
        "i_hat_color": GREEN,
        "j_hat_color": RED,
        "leave_ghost_vectors": False,
    }
    def construct(self):
        mob = Circle(color=PURPLE)
        mob.move_to(RIGHT+UP*2)
        vector_array1 = np.array([[1], [2]])
        vector_array2 = np.array([[2], [1]])
        matrix = [[1, 0], [1, 0]]
        title1 = TexMobject(r"\left[ {\begin{array}{*{20}{c}}1&0\\1&0\end{array}} \right]\cdot\
                            \left[ {\begin{array}{*{20}{c}}1\\0\end{array}} \right]=\
                            \left[ {\begin{array}{*{20}{c}}1\\1\end{array}} \right]").set_color(GREEN)
        title2 = TexMobject(r"\left[ {\begin{array}{*{20}{c}}1&0\\1&0\end{array}} \right]\cdot\
                            \left[ {\begin{array}{*{20}{c}}0\\1\end{array}} \right]=\
                            \left[ {\begin{array}{*{20}{c}}0\\0\end{array}} \right]").set_color(RED)
        title3 = TexMobject(r"\left[ {\begin{array}{*{20}{c}}1&0\\1&0\end{array}} \right]\cdot\
                            \left[ {\begin{array}{*{20}{c}}1\\2\end{array}} \right]=\
                            \left[ {\begin{array}{*{20}{c}}1\\1\end{array}} \right]").set_color(YELLOW)
        title4 = TexMobject(r"\left[ {\begin{array}{*{20}{c}}1&0\\1&0\end{array}} \right]\cdot\
                            \left[ {\begin{array}{*{20}{c}}2\\1\end{array}} \right]=\
                            \left[ {\begin{array}{*{20}{c}}2\\2\end{array}} \right]").set_color(BLUE)
        TextGroup=VGroup(title1,title2,title3,title4).arrange_submobjects(DOWN,aligned_edge=LEFT,buff=0.5).shift(3.5*LEFT)
                            
        self.add_transformable_mobject(mob)
        self.add_vector(vector_array1,color=YELLOW)
        self.add_vector(vector_array2,color=BLUE)
        self.apply_matrix(matrix)
        self.add_title(TextGroup,animate=True)
        self.wait(3)