from libraries import config
from libraries.config import *
from libraries.declare_types import *
import pygame, pymunk

# Event functions
def create_ball(space: Space, radius: float, mass: int, position: Coordinate) -> Shape:
    body: Body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = position
    shape: Shape = pymunk.Circle(body, radius=radius)
    shape.mass = mass
    shape.elasticity = 0.9
    shape.friction = 0.4
    shape.color = config.RED
    space.add(body, shape)
    return shape

def create_boundaries(space: Space, width: int, height: int) -> None:
    rects: list = [
        [(width / 2, height - 10), (width, 20)],
        [(width / 2, 10), (width, 20)],
        [(10, height / 2), (20, height)],
        [(width - 10, height / 2 ), (20, height)],
    ]

    for pos, size in rects:
        body: Body = pymunk.Body(body_type=pymunk.Body.STATIC)
        body.position = pos
        shape: Shape = pymunk.Poly.create_box(body, size)
        shape.elasticity = 0.7
        shape.friction = 0.5
        space.add(body, shape)
    return

def create_structure(space: Space, width: int, height: int) -> None:
    rects = [
        [(480, height - 90), (32, 150), config.BROWN, 100],
        [(720, height - 90), (32, 150), config.BROWN, 100],
        [(600, height - 180), (272, 30), config.BROWN, 150],
    ]

    for position,size, color, mass in rects:
        body: Body = pymunk.Body()
        body.position = position
        shape: Shape = pymunk.Poly.create_box(body, size, radius=1)
        shape.color = color
        shape.mass = mass
        shape.elasticity = 0.4
        shape.friction = 0.4
        space.add(body, shape)
    return

def create_pendulum(space: Space) -> None:
    rotation_axis: Body = pymunk.Body(body_type=pymunk.Body.STATIC)
    rotation_axis.position = (240, 180)

    body: Body = pymunk.Body()
    body.position = (240, 200)
    line: Segment = pymunk.Segment(body=body, a=(0, 0), b=(204, 0), radius=5)
    line.friction = 1
    line.mass = 8

    circle: Shape = pymunk.Circle(body=body, radius=40, offset=(240, 0))
    circle.color = config.GREEN
    circle.friction = 1
    circle.mass = 30
    circle.elasticity = 0.95

    joint: Joint = pymunk.PinJoint(body, rotation_axis, (0, 0), (0, 0))
    space.add(circle, body, line, joint)
    return

def draw(window: Surface, space: Space, draw_options: utils.DrawOptions, line: Line) -> None:
    window.fill("white")
    space.debug_draw(draw_options)
    if line:
        pygame.draw.line(surface=window, color="black", start_pos=line[0], end_pos=line[1], width=3)
        # print(line)
    pygame.display.update()
    return
