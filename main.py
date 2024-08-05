from libraries.config import *
from runner import run

"""
Description:
-----------
This App is a Physics Simulation using Pygame and Pymunk library

Installation:
------------
In order to run this code, you'll need to install a few libraries
```bash
$ pip install pygame pymunk
```
"""

if __name__ == "__main__":
    run(window=window, width=WIDTH, height=HEIGHT)
