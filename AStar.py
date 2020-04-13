from math import sqrt
import cv2
from map import Map
from utils import Node, Environment


class PathPlanning:
    # Initiation method
    def __init__(self, start, goal, clearance, stepSize):
        self.start = start
        self.goal = goal
        self.clearance = clearance
        self.stepSize = stepSize
        map = Map()
        self.map = map.map_img
        video_format = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
        self.video_output = cv2.VideoWriter('./video_output.avi', video_format, 10.0,
                                            (1020, 1020))

    # Method to solve a A* object
    def Astar(self):
        search = []
        # Set current node to start and add start node to the node list and node search dictionary
        CurrentNode = Node(self.start, self.start, self.goal, self.stepSize)
        NodeList = [CurrentNode]
        NodeDict = {tuple(CurrentNode.env)}
        search.append(CurrentNode)
        # Check if the current node is the goal node
        while sqrt((CurrentNode.env[0] - self.goal[0]) ** 2 + (CurrentNode.env[1] - self.goal[1]) ** 2) > 1.5:

            # Keep checking if there are nodes in list
            if len(NodeList) > 0:
                # Set current node to the first node in the list and then delete from list
                CurrentNode = NodeList.pop()

                Course = Environment(CurrentNode.env, self.clearance)
                # Check all of the possible nodes
                for node in Course.possibleMoves(self.start, CurrentNode, self.stepSize):

                    # Search dictonary and add node to list and dictionary if it hasn't been explored yet
                    if tuple((int(node.env[0]), int(node.env[1]), node.env[2])) not in NodeDict:
                        NodeList.append(node)
                        search.append(node)
                        NodeDict.add(tuple((int(node.env[0]), int(node.env[1]), node.env[2])))
                        sub_nodes = node.sub_nodes
                        for i in range(len(sub_nodes) - 1):
                            cv2.line(self.map, (int(sub_nodes[i][0] * 10), 1020 - int(sub_nodes[i][1] * 10)),
                                     (int(sub_nodes[i + 1][0] * 10), 1020 - int(sub_nodes[i + 1][1] * 10)), (0, 255, 0))
                        self.video_output.write(self.map)
                # Sort list of nodes based on cost
                NodeList.sort(key=lambda x: x.cost, reverse=True)

            else:
                return -1, CurrentNode.path(), search
        # solve for path
        x = CurrentNode.path()
        path = []
        for node in x:
            path.append(node)
        return 0, path, search

    def draw_path(self, path):
        # Define colors
        red = [0, 0, 255]
        blue = [255, 0, 0]
        green = [0, 255, 0]
        # Iterate through path nodes
        print('Video Dumping...')
        for i in range(1, len(path)):
            # Get intermediate nodes of each node in path-nodes' list
            sub_nodes = path[i].sub_nodes
            # Iterate through intermediate nodes' list to display path to be taken by the robot
            for j in range(len(sub_nodes) - 1):
                cv2.line(self.map, (int(sub_nodes[j][0] * 10), 1020 - int(sub_nodes[j][1] * 10)),
                         (int(sub_nodes[j + 1][0] * 10), 1020 - int(sub_nodes[j + 1][1] * 10)), red, 2)
            self.video_output.write(self.map)
            # Draw start and goal node to the video frame in the form of filled circle
            # cv2.circle(self.map,
            #            (int(path[-1].data[1]), 102 - int(path[-1].data[0])),
            #            int(3), red, -1)
            # cv2.circle(self.map,
            #            (int(path[0].data[1]), 102 - int(path[0].data[0])),
            #            int(3), green, -1)
            # Show path for longer time
            for _ in range(1000):
                self.video_output.write(self.map)
        print('Video Dumped')
        self.video_output.release()
