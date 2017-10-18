import pygame
import functools
import random


class CAProc():

    def __init__(self, init_state=[0 for i in range(100)], rule=43):
        self.state = init_state
        self.state[int((len(init_state)-1)/2)] = 1

        self.rule_key = [self.to_bin_3(i) for i in range(0, 8)]
        self.rule_value = [int(i) for i in self.to_bin(rule)]

        self.to_rule_dict = zip(reversed(self.rule_key), self.rule_value)

        self.rule_dict = dict(self.to_rule_dict)

        self.state_history = [self.state]

    def to_bin(self, nbr):
        # take base10, convert to bin with a length of 8
        return '{:08}'.format(int("{0:b}".format(nbr)))

    def to_bin_3(self, nbr):
        return '{:03}'.format(int("{0:b}".format(nbr)))

    def map_state(self):
        l = self.state[0::1]
        c = self.state[1::1]
        r = self.state[2::1]

        return zip(l, c, r)

    def next_state(self, inter_state):
        ret = []
        for i in inter_state:
            ret.append(self.rule_dict[str(functools.reduce(lambda x, y:str(x)+str(y), i))])

        return ret


    def change_state(self, prev_state):


        inter_state = self.map_state()
        next_state = self.next_state(inter_state)
        next_state.insert(0, 0)
        next_state.append(0)
        self.state = next_state
        self.state_history.append(next_state)

    def run_proc(self):
        for i in range(600):
            self.change_state(self.state)





class Draw():

    def __init__(self, CAProc):

        w = 1280
        h = 700
        self.state_history = CAProc.state_history
        self.size = 1
        self.padding = 0
        self.screen = pygame.display.set_mode((w, h))

    def draw(self):




        self.screen.fill((34, 55, 23))
        size = self.size

        iteration_counter = 0
        for i in self.grid_cord(self.state_history):
            c = self.colorize(i, self.state_history)
            s = self.screen_cord([i])
            pygame.draw.rect(self.screen, c, (*s[0], size - self.padding, size - self.padding), 0)
            iteration_counter += 1
            if iteration_counter % 800 == 0:

                pygame.display.flip()


    def colorize(self, grid_cord, state_history):
        ret = (25, 50, 30)
        if state_history[grid_cord[1]][grid_cord[0]] == 1:
            ret = (225, 255, 230)

        return ret

    def screen_cord(self, grid_cord):
        ret = []
        size = self.size

        for i in grid_cord:
            ret.append((i[0] * size, i[1] * size))

        return ret

    def grid_cord(self, state_history):
        a_list = []
        for y, l in enumerate(state_history):
            for x,__ in enumerate(l):
                a_list.append([x, y])
        return a_list
