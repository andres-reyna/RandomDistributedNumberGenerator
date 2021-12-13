from DistributionFactory import DistributionFactory

class DistributionController(object):
    def __init__(self, type, args):
        self.distribution = DistributionFactory.get_distribution(type, args)


    def get_sample(self, n):
        return self.distribution.get_sample(n)