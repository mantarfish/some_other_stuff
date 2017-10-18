import numpy as np
import random

import matplotlib
matplotlib.use('TkAgg')



import matplotlib.pyplot as plt
import matplotlib.animation as animation
import scipy
import scipy.ndimage

from liveviewer import LiveViewer

class GOL():
    '''simulating game of life'''
    def __init__(self, n=10, mode='wrap'):
        self.n = n
        self.mode = mode
        self.array = np.random.randint(2, size=(n, n))
        self.weights = np.array([[1, 1, 1],
                                 [1, 10, 1],
                                 [1, 1, 1]])

    def step(self):
        con = scipy.ndimage.filters.convolve(self.array,
                                             self.weights,
                                             mode=self.mode)

        boolean = (con == 3) | (con == 12) | (con ==13)
        self.array = np.int8(boolean)


class ForestFire():
    def __init__(self, n=10, mode='wrap'):
        self.n = n
        self.mode='wrap'
        self.f = 0.05


        # tree on fire prob
        self.p = 0
        self.array = np.random.randint(2, size=(n, n), dtype=np.int8)

        self.array[1, 1] = 10
        self.array[1, 3] = 10

        self.array[1, 2] = 1
        self.weights = np.array([[1, 1, 1],
                                [1, 100, 1],
                                [1, 1, 1]])
        


    def step(self):
        con = scipy.ndimage.filters.convolve(self.array,
                                             self.weights,
                                             mode=self.mode)
        self.con = con
       
        vfunc = np.vectorize(pyfunc=lambda x: self.cat_func(x))
        self.array = vfunc(np.array(con))

    def cat_func(self, x):

        ret = 0
        if x <= 80:
            sample = random.uniform(0,1)
            if self.f > sample:
                ret = 1
            else:
                ret = 0

        if x >= 100 and x <= 108:
            sample = random.uniform(0,1)
            if self.p > sample:
                ret = 10
            else:
                ret = 1

        if x >= 110 and x <= 180:
            ret = 10


        if x < 0:
            ret = 0

        return ret


            