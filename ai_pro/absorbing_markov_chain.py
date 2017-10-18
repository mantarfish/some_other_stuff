import random
import collections

prob_matrix = [
    [0, 1, 0, 0, 0, 1],
    [4, 0, 0, 3, 2, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
]


class Agent():
    def __init__(self, prob_matrix):
        self.current_state = 0
        self.prob_matrix = prob_matrix
        self.count = collections.defaultdict(lambda: 0)
        self.called = 0


    def _sum_prob(self, current_state):
        current = self.prob_matrix[current_state]
        sumd = sum(current)
        
        return sumd

    def _prob_dict(self, sumd, prob_matrix):
        prob = list(map(lambda x: x / sumd, prob_matrix[self.current_state]))
        prob_dict = {}
        for k, v in enumerate(prob):
            if v != 0:
                prob_dict[k] = v

        return prob_dict

    def _counter(self, current_state):
        self.count[current_state] += 1
        self.called += 1


    def choose_state(self, prob_dict):

        x = random.uniform(0, 1)
        upto = 0

        for state_name, prob in prob_dict.items():
            if upto + prob >= x:
                return state_name
            upto += prob


    def main_loop(self):
        it = 10000
        for i in range(0, it):
            sumd = self._sum_prob(self.current_state)

            if sumd == 0:
                self._counter(self.current_state)
                self.current_state = 0
                # sumd = self._sum_prob(self.current_state)
                sumd = 2

            prob_dict = self._prob_dict(sumd, self.prob_matrix)
            next_state = self.choose_state(prob_dict)
            self.current_state = next_state


        a_dict = {}
        for k, v in dict(self.count).items():
            a_dict[k] = v / self.called
            
        return a_dict
