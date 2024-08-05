from .declare_types import *
import math

# Helper Class
class CreateVector(list):
    """
    Description:
    -----------
    Creates a Vector that takes two Cartesian Coordinates as (x, y)
    and outputs (r, ɵ) as a Polar Coordinate where `r` is the distance between the two points
    or the magnitute of the vector and ɵ is the direction angle.

    CreateVector class inherits the list object for the output to be a list.

    Arguments:
    ---------
    @type point1: Coordinate
    @type point2: Coordinate

    Returns:
    -------
    @rtype Tuple[float, float]


    Methods:
    --------
    @type calculate_magnitute: float
    @type calculate_angle: float

    @returns calculate_magnitute: Distance between two points given as a Cartesian Coordinate using
    Eucledian distance formula
    @returns calculate_angle: Direction angle in Radian unit using tangent formula

    Formulae:
    --------
    @method calculate_magnitute: r = ✓[(x₂-x₁)² + (y₂-y₁)²]
    @method calculate_angle: ɵ = tan¯¹[(y₂-y₁)/(x₂-x₁)]

    Others:
    ------
    The parameters used are Coordinate types which is declared as
    ```python
    Coordinate = Union[Tuple[float, float], Sequence[float], Vector2]
    ```

    Example:
    -------
    ```python
    (r, ɵ) = CreateVector(point1=(2, 3), point2=(5, 6))
    print(r) # Output: 4.242640687119285
    print(ɵ) # Output: 0.7853981633974483
    ```
    """
    def __init__(self: Self, point1: Coordinate, point2: Coordinate) -> None:
        self.point1 = point1
        self.point2 = point2
        self.extend((self.calculate_magnitute(), self.calculate_angle()))
        return

    def calculate_magnitute(self: Self) -> float:
        return math.sqrt(((self.point2[0] - self.point1[0])**2 + (self.point2[1] - self.point1[1])**2))

    def calculate_angle(self: Self) -> float:
        return math.atan2(self.point2[1] - self.point1[1], self.point2[0] - self.point1[0])
