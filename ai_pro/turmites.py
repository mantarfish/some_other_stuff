import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt

import matplotlib.animation as animation

import scipy
import numpy as np

from liveviewer import LiveViewer


class Turmite():
    '''Simulate a turmite on a torus'''
    def __init__(self, n=10, heads = []):
        self.n = n
        self.array = np.random.randint(2, size=(self.n, self.n))
        self.heads = heads
        

    def step(self):
        for head in self.heads:
            s = self.array[head.head_pos[0], head.head_pos[1]]
            if s == 1:
                self.array[head.head_pos[0], head.head_pos[1]] = 0
                head.turn('Left')
                

            if s == 0:
                self.array[head.head_pos[0], head.head_pos[1]] = 1
                head.turn('Right')

            head.move(str(head.head_orientation), self.n)



class Head():
    def __init__(self):
        self.head_orientation = 0
        self.head_pos = (0, 0)

    def turn(self, direction):
        if direction == "Left":
            self.head_orientation = (self.head_orientation - 1) % 4

        if direction == "Right":
            self.head_orientation = (self.head_orientation + 1) % 4

    def move(self, direction, n):
        if direction == '3':
            self.head_pos = ((self.head_pos[0] - 1) % n, self.head_pos[1])

        if direction == '1':
            self.head_pos = ((self.head_pos[0] + 1) % n, self.head_pos[1])

        if direction == '0':
            self.head_pos = (self.head_pos[0], (self.head_pos[1] + 1) % n)

        if direction == '2':
            self.head_pos = (self.head_pos[0], (self.head_pos[1] - 1) % n)

