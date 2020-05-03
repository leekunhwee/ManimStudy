# Line
`Line` inherit the class of `TipableVMobject`

## Import modules
```python3
from manimlib.imports import *
```

## Default definition
```python3
class Shapes(Scene):
    def construct(self):
        line  = Line()

        self.play(ShowCreation(line))
        self.wait(2)
```

<p align="center"><img src ="Shapes1.gif" /></p>

## Change initial parameters
### Start and end points
`Line(start=LEFT, end=RIGHT, **kwargs)`

```python3
class Shapes(Scene):
    def construct(self):
        line  = Line(start=(-3,2,0))

        self.play(ShowCreation(line))
        self.wait(2)
```

<p align="center"><img src ="Shapes2.gif" /></p>

### Colors
```python3
class Shapes(Scene):
    def construct(self):
        line  = Line(start=(-3,2,0),color=RED)

        self.play(ShowCreation(line))
        self.wait(2)
```

<p align="center"><img src ="Shapes3.gif" /></p>