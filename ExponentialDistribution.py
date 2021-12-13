import numpy
from Distribution import Distribution
import math


class ExponentialDistribution(Distribution):
    def __init__(self, parameters):
        self.a = parameters['a']

    def get_probability(self, x, acc):
        if acc:
            return 1 - math.exp(-1 * x/self.a)
        else:
            return 1/self.a * math.exp(-1*x/self.a)


    def get_sample(self, n):
        sample = []
        for i in range(n):
            u = numpy.random.uniform(0, 1, 1)[0]
            k = 0
            p_aux = self.get_probability(k, True)
            while True:
                k += 1
                p_aux += self.get_probability(k, True)
                if(p_aux > u):
                    break
            sample.append(k)
        return sample