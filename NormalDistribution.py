import numpy
from Distribution import Distribution
from math import exp, sqrt, pi, log, sin
from scipy.stats import norm


class NormalDistribution(Distribution):
    def __init__(self, parameters):
        self.mean = parameters['mean']
        self.std = parameters['std']

    def get_probability(self, x, acc):
        if acc:
            return norm.cdf(x, self.mean, self.std)
        else:
            return (1 / (self.std * sqrt(2 * pi))) * exp((-((x - self.mean) ** 2) / ((2 * self.std) ** 2)))

    def get_sample(self, n):
        sample = []
        for i in range(n):
            u1 = numpy.random.uniform(0, 1, 1)[0]
            u2 = numpy.random.uniform(0, 1, 1)[0]
            k = self.mean + self.std * (sin(2 * pi * u1) * sqrt(-2 * log(u2)))
            sample.append(k)
        return sample
