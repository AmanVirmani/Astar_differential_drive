#!/usr/bin/env python

from AStar import PathPlanning
import sys
from math import degrees


def main():
    rpm = [int(sys.argv[7]), int(sys.argv[8])]
    planner = PathPlanning([int((float(sys.argv[1])+5)*10), int((float(sys.argv[2])+5)*10), int(degrees(float(sys.argv[3])))],
                  [int((float(sys.argv[4])+5)*10), int((float(sys.argv[5])+5)*10)], int(sys.argv[6]), rpm)
    ret,path,_ = planner.Astar()
    if ret == -1 :
        print("no solution found")
        exit(1)
    planner.draw_path(path)

if __name__ == '__main__':
    main()
