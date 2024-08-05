# Physics Simulation in Python

In this repository, applied force and gravitational force on various objects are simulated in python. For the physics, we'll use Pymunk library and for the GUI, we'll use Pygame.

## Initialization
To continue with this project, it is recommended to create a new virtual environment in python.
```bash
$ cd path/to/directory
$ python -m venv pyphysics
```
Now to activate the environment:
**Windows:**
```bash
$ .\venv\Scripts\activate.bat
```
**Mac OS / Linux**
```bash
$ source venv/bin/activate
```
## Installation
For this particular project, we'll use two external libraries pygame and pymunk. And for building the app to release version, we'll use pyinstaller.
```bash
$ pip install pygame pymunk pyinstaller
```
To be noted that the project uses some of the modern features of Python. So it is recommended to use Python version 3.10.* or updated ones.

## Running
To run this app, simply write run the main file
```bash
$ python main.py
```

[![Demo](https://raw.githubusercontent.com/mmycin/Physics-Simulation-/master/thumbnai..jpg)](https://raw.githubusercontent.com/mmycin/Physics-Simulation-/master/20240805-1850-04.3335478.mp4)

## Building
To export it as an executable app, we'll use pyinstaller
```bash
$ pyinstaller --name PhysicsSimulator --onefile --windowed --icon=icon.ico main.py
```
It will make a PhysicsSimulator.exe at the `dist/` folder. Now you can use it and make a Setup file.
