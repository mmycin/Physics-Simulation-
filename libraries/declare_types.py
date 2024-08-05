"""
Description:
-----------
Custom data type used in the projects. The imports are the objects from Pygame
and Pymunk to be used as type. The custom data types are descripted bellow

Types:
-----
@type Coordinate
@type Line
@type Color

Coordinate Type:
---------------
The type Coordinate is used as the Cartesian Coordinates. It can refer to
a Tuple (x, y) or a Sequence and specially a Vector. A vector can be defined
in many ways, one of the ways is to use coordinates. Hence, a Coordinate can be
defined as either a Tuple of floats or sequence or a vector.
In pyhon, Union is used to merge multiple types.
Example:
```python
point1: Coordinate = (2, 4)
print(point1) # Output: (2, 4)
```

Line Type:
---------
A line is just a list of points. A line can be defined as a list of bunch of Coordinates.
Now a line can have a length of zero which leads the line to be non-existent or in this case,
None. So a line can be a list coodinates, list of lengths or None. That's how it is defined.
Example:
```python
line1: Line = [(2, 3), (4, 2)]
check_none = lambda line: "yes" if line1 is not None else "no"
print(check_none(line1)) # Output: yes
line1 = None
print(check_none(line1)) #Output: no
```

Color Type:
----------
In computer graphics, color is defined in many ways such as rgb, cmyk, rgba, hex etc.
Here, we've used the rgba method. It is defined as a Tuple that takes four integers as rgba values: red, green, blue, alpha.
Example:
```python
red: Color = (255, 0, 0, 100)
green: Color = (0, 255, 0, 100)
blue: Color = (0, 0, 255, 100)
white: Color = (255, 255, 255, 100)
black: Color = (0, 0, 0, 0)
# Use them in your process
```
"""

#  Imported for better type hinting
from pygame.time import Clock
from pygame.surface import Surface
from pymunk.body import Body
from pymunk.shapes import Shape
from pymunk.space import Space
from pymunk.shapes import Segment
from typing import Any, List, Optional, Self, Tuple, Union, Sequence
from pygame.math import Vector2
import pymunk.pygame_util as utils
from pymunk import PinJoint as Joint
# -------------------------------------

# Declare Types
Coordinate = Union[Tuple[float, float], Sequence[float], Vector2]
Line = Optional[Union[List[Coordinate], List[Any]]]
Color = Tuple[int, int, int, int]
