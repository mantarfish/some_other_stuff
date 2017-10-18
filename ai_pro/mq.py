import random
import math

# use mm1 queue to model merchant inventory

class MQueue():
    def __init__(self, add_rate=.59, remove_rate=.6):
        # rate of add/remove per unit of time.
        self._add_rate = add_rate
        self._remove_rate = remove_rate

        self._rate_ratio = self._add_rate / self._remove_rate

    def prob(self, n):
        # return prob of a queue haveing a length of n.
        r = self._rate_ratio
        p = (1 - r) * (r ** n)
        return p

    def cdf(self, n):
        r = self._rate_ratio
        return r**n*(-r + 1)/math.log(r) - (-r + 1)/math.log(r)

    def limit(self):
        r = self._rate_ratio
        return (-1 + r) / math.log(r)


    def get_sample(self):
        # get length give prob

        # generate a prob from 0 to 1
        x = random.uniform(0, self.limit())

        # try to find a n so that p(n) < x
        n = 1
        p = self.cdf(n)
        t = 0
        

        while p <= x and t < 5000:
            n += 1
            p = self.cdf(n)
            t += 1
            
        
        return (n, t, p, x)



