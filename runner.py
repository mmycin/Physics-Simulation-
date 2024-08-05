"""
Description:
-----------
This module consists of a function named `draw()`
It is the main event loop of the simulation app.

Functions:
---------
1. draw: None
"""

from libraries.calculate import CreateVector
from libraries.config import *

def run(window: Surface, width: int, height: int) -> None:
    """
    Description:
    -----------
    Main event loop of the app that:
    1. Defines a Pymunk space in the window
    2. Starts a clock for 60 FPS refresh rate
    3. Creates the objects on the screen with appropriate forces
    4. Applies impulsive force on a ball with calculated force components

    Parameters:
    ----------
    @type window: pygame.Surface

    @type width: int
    @param windth: Width of the screen (no default value)

    @type height: int
    @param height: Height of the screen (no default value)

    Returns:
    -------
    @rtype None

    Example:
    ------
    ```python
    import pygame
    pygame.init()

    # Define constants
    WIDTH: int = 1000
    HEIGHT: int = 800

    window: pygame.Surface = pygame.display.set_mode((WIDTH, HEIGHT))
    run(window=window, width=WIDTH, height=HEIGHT)
    ```
    """
    # Event loop settings
    run: bool = True
    clock: Clock = pygame.time.Clock()
    fps: int = 60
    dt: float = 1 / fps

    space: Space = pymunk.Space()
    space.gravity = (0, 981)

    # Defining the objects
    ball: Optional[Shape] = None
    pressed_position: Optional[Coordinate] = None
    draw_options: utils.DrawOptions = utils.DrawOptions(window)

    create_boundaries(space=space, width=width, height=height)
    create_structure(space=space, width=width, height=height)
    create_pendulum(space=space)

    while run:
        line: Optional[Line] = None
        if ball and pressed_position:
            line = [pressed_position, pygame.mouse.get_pos()]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            if event.type == pygame.MOUSEBUTTONDOWN:
                if not ball:
                    pressed_position = tuple(float(x) for x in pygame.mouse.get_pos())
                    ball = create_ball(space=space, radius=22.5, mass=20, position=pressed_position)
                elif pressed_position:
                    ball.body.body_type = pymunk.Body.DYNAMIC
                    if line is not None:
                        (magnitute, angle) = CreateVector(point1=line[0], point2=line[1])
                        force: float = magnitute * 50
                        force_x_component: float = - math.cos(angle) * force
                        force_y_component: float = - math.sin(angle) * force
                    else:
                        raise ValueError("expected line: Line, got line: None")
                    ball.body.apply_impulse_at_local_point((force_x_component, force_y_component), (0, 0))
                    pressed_position = None
                else:
                    space.remove(ball, ball.body)
                    ball = None

        draw(window=window, space=space, draw_options=draw_options, line=line)
        space.step(dt=dt)

        clock.tick(fps)
    pygame.quit()
