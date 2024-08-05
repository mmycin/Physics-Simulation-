"""
Description:
-----------
Configuration of the whole app with constants and objects

Constants:
---------
WIDTH, HEIGHT,
RED, GREEN, BROWN
"""

import pygame
from .declare_types import *
from .calculate import CreateVector
from create_objects import *
import math

# Constants
WIDTH: int = 800
HEIGHT: int = 600
RED: Color = (255, 0, 0, 100)
BROWN: Color = (139, 69, 19, 100)
GREEN: Color = (80, 200, 120, 100)

pygame.init()

window: Surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Physics Simulation")
pygame.display.set_icon(pygame.image.load("icon.ico"))
