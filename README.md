# Project 2 - ENPM661 - Planning for Autonomous Robots
## Implementation of the Dijkstra Algorithm for a Point Robot

Vinay Lanka
Email - vlanka@umd.edu (120417665)

Github link to repository - https://github.com/vinay-lanka/Dijkstra-Planner-Visualised

This Python script (`djikstra.py`) demonstrates the Dijkstra algorithm for pathfinding in a 2D grid environment using OpenCV for visualization. The script generates a map with obstacles and walls, allows the user to input a start and goal position, and then visualizes the process of finding the shortest path from the start to the goal using Dijkstra's algorithm.

## Dependencies

Before running the script, ensure you have the following dependencies installed:

- Python 3.x
- NumPy
- OpenCV (cv2)

You can install NumPy and OpenCV using pip:

```bash
$ pip3 install numpy opencv-python
```

## Running the Script

To run the script, use the following command:

```bash
$ python3 djikstra.py
```

1. Follow the on-screen instructions to input the start and goal coordinates.

2. Once the visualization is complete, press 'q' to close the visualization window.

## Script Overview

- The script initializes a 2D grid environment with obstacles and walls.
- It prompts the user to input a start and goal position within the grid.
- Dijkstra's algorithm is applied to find the shortest path from the start to the goal.
- The process of pathfinding is visualized using OpenCV.
- After finding the shortest path, the script visualizes the path from the start to the goal.

## Files Included

- `djikstra.py`: The Python script implementing the Dijkstra algorithm visualization.
- `dijkstra.mp4`: The output video file containing the visualization of the Dijkstra algorithm.