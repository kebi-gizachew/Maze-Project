# Maze Generator and Solver
## Overview

This project is a Python and Pygame implementation of a maze generator and solver.

The maze is generated using a stack-based Depth First Search (DFS) algorithm where a virtual “mouse” removes walls between cells to create a proper maze. The maze is then solved using a backtracking algorithm.

## Features
Random maze generation
Dynamic wall removal visualization
Automatic maze solving
Backtracking visualization
Red cells show the current path
Blue cells show dead ends
## Technologies Used
Python
Pygame
Maze Representation

## The maze uses two arrays:

- northWall[R][C]
- eastWall[R][C]
### 1 means the wall exists
### 0 means the wall has been removed
## Maze Generation Logic
- Start with all walls intact
- Choose a random starting cell
- Visit unvisited neighbors randomly
- Remove walls between connected cells
- Use a stack to backtrack when trapped

This ensures every cell is connected.

## Maze Solving Logic

### The solver uses DFS backtracking:

- Red cells represent the explored path
- Blue cells represent dead ends
- The algorithm continues until the exit is found
## How to Run

### Install pygame:

- pip install pygame

### Run the project:

- python maze.py
- Loom Demonstration

## The Loom recording demonstrates:

- Dynamic maze generation
- Mouse movement through walls

## Demo link
https://www.loom.com/share/a43ffb57a811462f8be166b256e116f6
- Maze solving using backtracking
- Dead-end detection
## Author
Kebron Gizachew
