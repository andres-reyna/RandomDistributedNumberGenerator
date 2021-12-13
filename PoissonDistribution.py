from Distribution import Distribution
import math
import random


class PoissonDistribution(Distribution):
    def __init__(self, parameters):
        self.l = parameters['l']

    def get_probability(self, x, acc):
        if acc:
            p_acc = 0
            for i in range(x+1):
                probability = (self.l**i)/math.factorial(i)
                p_acc += probability

            p_acc *= math.exp(-1 * self.l)
            return p_acc
        else:
            return self.l ** x * math.exp(-1 * self.l) / math.factorial(x)

    def get_sample(self, n):
        sample = []
        for i in range(n):
            u = random.random()
            k = 0
            p_aux = self.get_probability(k, True)
            while True:
                if (p_aux > u):
                    break
                p_aux += self.get_probability(k, True)

            k += 1
            sample.append(k)
        return sample