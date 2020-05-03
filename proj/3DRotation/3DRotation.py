from manimlib.imports import *

class Rotation_Sphere(SpecialThreeDScene):
    CONFIG={'scale_all': 0.75,}
    def construct(self):
        sphere1 = self.get_sphere()
        
        vectors = VGroup(*[Vector(u * v, color=color).next_to(sphere1, u * v, buff=0)
                            for v, color in zip(
                                    [RIGHT,  UP,  OUT],
                                    [GREEN, RED, BLUE],
                                    )
                            for u in [-1, 1]]
                          )
        
        vectors.set_shade_in_3d(True)
        sphere1.add(vectors)
        sphere2 = sphere1.copy()
        
        label1 = TextMobject(
            "先绕 $F_b$ 的 $x$轴\\\\",
            "再绕 $F_b$ 的 $y$轴"
        )
        label2 = TextMobject(
            "先绕 $F_b$ 的 $y$轴\\\\",
            "再绕 $F_b$ 的 $x$轴"
        )
        for label in [label1, label2]:
            for part in label:
                part.add_background_rectangle()
            label.rotate(90 * DEGREES, RIGHT)
            label.move_to(3 * OUT + 0.5 * IN)
            
        group_all = VGroup(sphere1, sphere2, label1, label2).scale_about_point(self.scale_all, ORIGIN)
        
        self.set_camera_orientation(phi=75 * DEGREES,theta=-65*DEGREES)
        self.add(self.get_axes())
        self.add(sphere1)
        angle_axis_pairs = [
            (90 * DEGREES, RIGHT),
            (90 * DEGREES, OUT),
        ]
        angle_axis_pairs1 = [
            (90 * DEGREES, UP),
            (90 * DEGREES, IN),
        ]
        for angle, axis in angle_axis_pairs:
            self.play(Rotate(
                sphere1, angle,
                axis=axis,
                run_time=2,
            ))
            self.wait()
        self.play(FadeInFrom(label1, IN))
        self.wait(2)
        
        self.play(
            sphere1.shift, 5 * RIGHT,
            label1.shift, 5 * RIGHT,
            Write(sphere2, run_time=1)
        )
        for angle, axis in angle_axis_pairs1:
            self.play(Rotate(
                sphere2, angle,
                axis=axis,
                run_time=2,
            ))
            self.wait()
        self.play(FadeInFrom(label2, IN))
        self.wait(5)
        
      
class RubiksCube(VGroup):
    CONFIG = {
        "colors": [
            "#FFD500",  # Yellow
            "#C41E3A",  # Orange
            "#009E60",  # Green
            "#FF5800",  # Red
            "#0051BA",  # Blue
            "#FFFFFF"   # White
        ],
    }

    def __init__(self, **kwargs):
        digest_config(self, kwargs)
        vectors = [OUT, RIGHT, UP, LEFT, DOWN, IN]
        faces = [
            self.create_face(color, vector)
            for color, vector in zip(self.colors, vectors)
        ]
        VGroup.__init__(self, *it.chain(*faces), **kwargs)
        self.set_shade_in_3d(True)

    def create_face(self, color, vector):
        squares = VGroup(*[
            self.create_square(color)
            for x in range(9)
        ])
        squares.arrange_in_grid(
            3, 3,
            buff=0
        )
        squares.set_width(2)
        squares.move_to(OUT, OUT)
        squares.apply_matrix(z_to_vector(vector))
        return squares

    def create_square(self, color):
        square = Square(
            stroke_width=3,
            stroke_color=BLACK,
            fill_color=color,
            fill_opacity=1,
            side_length=1,
        )
        square.flip()
        return square

    def get_face(self, vect):
        self.sort(lambda p: np.dot(p, vect))
        return self[-(12 + 9):]
        
class RotationsOfCube(SpecialThreeDScene):
    CONFIG={'scale_all': 0.75,}
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES,theta=-65*DEGREES)
        # self.begin_ambient_camera_rotation(0.0001)
        cube = RubiksCube()
        cube2 = cube.copy()
        axes = self.get_axes()
        axes.scale(0.75)

        label1 = TextMobject(
            "先绕 $F_s$ 的 $x$轴\\\\",
            "先绕 $F_s$ 的 $y$轴"
        )
        label2 = TextMobject(
            "先绕 $F_s$ 的 $y$轴\\\\",
            "先绕 $F_s$ 的 $x$轴"
        )
        for label in [label1, label2]:
            for part in label:
                part.add_background_rectangle()
            label.rotate(90 * DEGREES, RIGHT)
            label.move_to(3 * OUT + 0.5 * IN)
            
        group_all = VGroup(cube, cube2, label1, label2).scale_about_point(self.scale_all, ORIGIN)
        
        self.add(axes, cube)
        self.play(
            Rotate(cube, 90 * DEGREES, RIGHT, run_time=2),
            FadeInFrom(label1[0], IN),
        )
        self.play(
            Rotate(cube, 90 * DEGREES, UP, run_time=2),
            FadeInFrom(label1[1], IN),
        )
        
        self.wait()
        self.play(
            cube.shift, 5 * RIGHT,
            label1.shift, 5 * RIGHT,
            Write(cube2, run_time=1)
        )
        self.play(
            Rotate(cube2, 90 * DEGREES, UP, run_time=2),
            FadeInFrom(label2[0], IN),
        )
        self.play(
            Rotate(cube2, 90 * DEGREES, RIGHT, run_time=2),
            FadeInFrom(label2[1], IN),
        )
        self.wait(5)
        