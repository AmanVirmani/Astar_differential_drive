## Overview
A* implementation for Rigid Robot

## Dependencies

The following dependencies must be installed.

1. python3.5 or above
2. numpy
3. opencv 3.4 or above

Enter the given commands in bash terminal to install the dependencies.
```bash
sudo apt-get install python3
pip3 install numpy opencv-python
```

## Build Instructions

Run the following command to do path planning for a rigid robot using A* algorithm

```bash
git clone https://github.com/AmanVirmani/Astar_differential_drive
python main.py <start node with theta> <goal node without theta> <clearance> <RPM1> <RPM2>
```
For demo output
```bash
python main.py -4 -4 0 4 4 5 30 60
```

## Output

The file  video_output.avi shows the animation for the optimal path after the exploration.
