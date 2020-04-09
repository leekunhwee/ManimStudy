# Arrow
`Arrow` inherit the class of `Line`

## Import modules
```python3
from manimlib.imports import *
```

## Default definition
```python3
class Shapes(Scene):
    def construct(self):
        arrow  = Arrow()

        self.play(ShowCreation(arrow))
        self.wait(2)
```

<p align="center"><img src ="Arr1.gif" /></p>

## Change initial parameters
### Start and end points
`DashedLine(start=LEFT, end=RIGHT, **kwargs)`

```python3
class Shapes(Scene):
    def construct(self):
        arrow  = Arrow(start=(-3,2,0))

        self.play(ShowCreation(arrow))
        self.wait(2)
```

<p align="center"><img src ="Arr2.gif" /></p>

### Colors
```python3
class Shapes(Scene):
    def construct(self):
        arrow  = Arrow(start=(-3,2,0),color=RED)

        self.play(ShowCreation(arrow))
        self.wait(2)
```

<p align="center"><img src ="Arr3.gif" /></p>