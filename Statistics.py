from Solver import Solver
from Mastermind import Mastermind

import statistics
from math import sqrt


class Statistics:
    def __init__(self, numberOfColors, holes, runs):
        assert isinstance(numberOfColors, int)
        assert numberOfColors > 0

        assert isinstance(holes, int)
        assert holes > 0

        assert isinstance(runs, int)
        assert runs > 0

        self.runs = runs
        self.attempts = []

        for i in range(runs):
            mastermind = Mastermind(list(range(numberOfColors)), holes)
            Solver(mastermind)
            self.attempts.append(mastermind.getAttempts())

    def getMeanAttempts(self):
        return statistics.mean(self.attempts)

    def getStdev(self):
        return statistics.stdev(self.attempts)

    def getStdError(self):
        return self.getStdev() / sqrt(self.runs)

    def getMinAttempts(self):
        return min(self.attempts)

    def getMaxAttempts(self):
        return max(self.attempts)


if __name__ == "__main__":
    stats = Statistics(6, 4, 1000)

    print("mean: {}\n".format(stats.getMeanAttempts())
          + "stdev: {}\n".format(stats.getStdev())
          + "min: {}\n".format(stats.getMinAttempts())
          + "max: {}".format(stats.getMaxAttempts()))
