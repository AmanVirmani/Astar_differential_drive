# Import necessary standard libraries
import cv2
import numpy as np
# Import necessary constants
# from utils import constants


class Map:
    def __init__(self):
        """
        Initialize map class with radius of the robot and clearance
        """
        # Various class parameters
        self.height = 1020
        self.width = 1020
        # self.thresh = int(constants.robot_radius) + clearance
        self.scaling = 100
        self.black = (255, 0, 0)
        # Define length of edge of squares
        # Same for all squares
        self.square_length = 150
        # Define the coordinates of the top-left corner of the square obstacles
        self.square_coords = np.array([(235, 135),
                                       (35, self.height - 510 - 75),
                                       (self.width - 110 - 75, self.height - 510 - 75)],
                                      dtype=np.int32)
        # Define radius of circular obstacles
        # Radius is same for all circles
        self.circle_radius = self.scaling * 1
        # Define centers of all circles
        self.circle_centers = np.array([(self.width - 310, 210),
                                        (510, 510),
                                        (310, self.height - 210),
                                        (self.width - 310, self.height - 210)],
                                       dtype=np.int32)
        # Define empty world and add obstacles to it
        self.map_img = self.draw_obstacles()

    def draw_circle(self, img, thresh=0):
        """
        Draw the 4 circular obstacles on the map-image
        :return: nothing
        """
        for center in self.circle_centers:
            # Draw the circle
            cv2.circle(img, (center[0], center[1]), self.circle_radius + thresh, self.black, -1)

    def draw_squares(self, img, thresh=0):
        """
        # Draw the 3 square obstacles on the map
        # :return: nothing
        """
        for corner in self.square_coords:
            top_corner = (corner[0] - thresh), (corner[1] - thresh)
            bottom_corner = (corner[0] + self.square_length + thresh), (corner[1] + self.square_length + thresh)
            # Draw the square on the map
            cv2.rectangle(img, top_corner, bottom_corner, self.black, -1)

    def draw_obstacles(self):
        """
        Draw map using half-plane equations
        :return: map-image with all obstacles
        """
        self.map_img = cv2.imread('../images/map.png')
        if self.map_img is None:
            self.map_img = np.zeros((self.height, self.width, 3), dtype=np.uint8)
            # Fill map-image with white color
            self.map_img.fill(255)
            # Draw various obstacles on the map
            self.draw_circle(self.map_img)
            self.draw_squares(self.map_img)
            cv2.imwrite('../images/map.png', self.map_img)

        return self.map_img
