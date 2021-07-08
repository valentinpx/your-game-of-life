# your-game-of-life
Project created for the {Digital Art.} exhibition at Epitech (Lille).

## Description
With an SSH key (which was generated at the event entrance from the visitor's face), the program generates a cell grid.
This cell grid is then processed by a cellular automaton: the [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life).
A GIF based on the successive created states of the grid is finally rendered.

### Usage
> python3 src/main.py [key path]
- `[key path]` Path to the ssh key

The program will create a "ygol.gif" file which contains the animation.
