# Dashed Line
`DashedLine` inherit the class of `Line`

## Import modules
```python3
from manimlib.imports import *
```

## Default definition
```python3
class Shapes(Scene):
    def construct(self):
        dashedline  = DashedLine()

        self.play(ShowCreation(dashedline))
        self.wait(2)
```

<p align="center"><img src ="Dashed1.gif" /></p>

## Change initial parameters
### Start and end points
`DashedLine(start=LEFT, end=RIGHT, **kwargs)`

```python3
class Shapes(Scene):
    def construct(self):
        dashedline  = DashedLine(start=(-3,2,0))

        self.play(ShowCreation(dashedline))
        self.wait(2)
```

<p align="center"><img src ="Dashed2.gif" /></p>

### Colors
```python3
class Shapes(Scene):
    def construct(self):
        dashedline  = DashedLine(start=(-3,2,0),color=RED)

        self.play(ShowCreation(dashedline))
        self.wait(2)
```

<p align="center"><img src ="Dashed3.gif" /></p>