import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt

import matplotlib.animation as animation

import scipy
import numpy as np

class LiveViewer():

    def __init__(self, life, cmap=plt.get_cmap('Blues')):
        self.life = life
        self.fig = plt.figure()
        self.im = plt.imshow(self.life.array, animated=True, cmap=None)


    def update_fig(self, *args):
        self.life.step()
        self.im.set_array(self.life.array)
        return self.im,

    def draw(self):
        self.ani = animation.FuncAnimation(self.fig, self.update_fig, interval=1, blit=True)
        plt.show()