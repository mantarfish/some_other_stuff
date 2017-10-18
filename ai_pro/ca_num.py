import random

import numpy as np
import matplotlib

matplotlib.use('TkAgg')

import matplotlib.animation as animation

import matplotlib.pyplot as plt

from liveviewer import LiveViewer





def make_table(rule):
    '''make_table takes an int from 0 to 255 and produces a rule table dict'''

    # produce the key for rule_table
    # create a list of 0 to 8 and map them to binaries of length 3
    table_keys = [i for i in range(8)]
    table_keys_bin = list(map(lambda x: format(x, '03b'), table_keys))

    # turn a integer rule into fixed length binary of length 8
    # and turn it into a list with length 8
    table_rules = reversed([i for i in str(format(rule, '08b'))])

    return dict(zip(table_keys_bin, table_rules))


class CA():
    '''models a ca process with rule form 0 to 255'''
    '''this ca is modified to go infinitely long'''

    def __init__(self, rule=90, cols=5, ratio=2):
        # ratio is deprecated
        self.rule_table = make_table(rule)
        self.cols = cols
        self.steps = int(cols*ratio + 1)
        self.array = np.zeros((int(self.steps), self.cols), dtype=np.int8)
        self.next = 0
        self.start_single()

    def start_single(self):
        '''starts with one cell in the middle of the top row'''
        if self.next == 0:
            self.array[0, int(self.cols/2)] = 1
            self.next += 1

    def start_rand(self):
        if self.next == 0:
            self.array[0] = np.random.choice((0,1), self.cols)
            self.next +=1

    def start_right(self):
        if self.next == 0:
            self.array[0, self.cols-1] = 1

    def step(self):
        i = self.next
        self.next += 1
 
        a = self.array
        t = self.rule_table
        for j in range(1, self.cols-1):
            a[i, j] = t[''.join(a[i-1, j-1:j+2].astype(str))]

        self.array = np.append(self.array, np.zeros((1, self.cols), dtype=np.int8), axis = 0)

    def plot_ca(self):
        cmap = plt.get_cmap('Blues')
        plt.imshow(self.array, interpolation=None, cmap=cmap)


class CounterViewer():
    def __init__(self, ca):
        self.fig, self.ax = plt.subplots()
        self.ca = ca
        self.t = 1


        self.num_e = []
        self.one_over_e = []

        self.num_e.append(np.count_nonzero(self.ca.array))
        self.one_over_e.append(1 / (1 / self.t))


        self.line, = self.ax.plot(self.num_e, self.one_over_e)

    def update_line(self, *args):
        self.ca.step()
        self.t += 1

        self.num_e.append(np.count_nonzero(self.ca.array))
        self.one_over_e.append(1 / (1 / self.t))

        self.line.set_xdata(self.num_e)
        self.line.set_ydata(self.one_over_e)
        return self.line,


    def draw(self):
        self.ani =  animation.FuncAnimation(self.fig, self.update_line, interval=1, blit=True)
        plt.show()



'''

class CA_plot():
    ''''do not use very slow''''
    def __init__(self, array, cmap=None, w=800, h=600, size=2):

        if cmap == None:
            self.cmap = {0: (25, 25, 25), 1: (200, 200, 200)}

        self.array = array
        self.rows, self.cols = self.array.shape
        self.w = size * self.cols
        self.h = size * self.rows
        self.size = size

    def to_screen_space(self, t):
        s = self.size
        return (t[1]*s, t[0]*s)

    def update(self, array):
        self.array = array


    def draw(self):
        screen = pygame.display.set_mode((self.w, self.h))
        s = self.size

        for index, value in np.ndenumerate(self.array):
            c = self.cmap[value]
            screen_cord = self.to_screen_space(index)
            pygame.draw.rect(screen, c, (*screen_cord, s, s), 0)

        pygame.display.update()
'''