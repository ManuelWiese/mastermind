import random
import itertools
import statistics


class Mastermind:
    def __init__(self, colors, holes):
        assert isinstance(colors, list)
        assert len(colors) > 0
        assert isinstance(holes, int)

        self.colors = colors
        self.holes = holes
        self.setRandomCode()
        self.attempts = 0
        self.finished = False

    def setRandomCode(self):
        self.code = []
        for i in range(self.holes):
            self.code.append(random.choice(self.colors))

    def getColors(self):
        return self.colors

    def getHoles(self):
        return self.holes

    def scoreAttempt(self, attempt):
        assert isinstance(attempt, list) or isinstance(attempt, tuple)
        assert len(attempt) == self.holes

        self.attempts += 1
        score = self.compareCodes(self.code, attempt)
        if score[0] == self.holes:
            self.finished = True
        return score

    def compareCodes(self, code1, code2):
        assert isinstance(code1, list) or isinstance(code1, tuple)
        assert isinstance(code2, list) or isinstance(code2, tuple)
        assert len(code1) == len(code2)

        colorMatches = 0
        for color in set(code1):
            count1 = code1.count(color)
            count2 = code2.count(color)
            if count1 < count2:
                colorMatches += count1
            else:
                colorMatches += count2

        matches = 0
        for i in range(len(code1)):
            if code1[i] == code2[i]:
                matches += 1

        return matches, colorMatches

    def isFinished(self):
        return self.finished

    def getAttempts(self):
        return self.attempts


class Solver:

    def __init__(self, mastermind, firstAttempt=None):
        assert isinstance(mastermind, Mastermind)
        self.mastermind = mastermind

        self.colors = mastermind.getColors()
        self.holes = mastermind.getHoles()
        self.setPossibleSolutions()

        assert firstAttempt is None or isinstance(firstAttempt, list)
        assert (firstAttempt is None
                or len(firstAttempt) == mastermind.getHoles())

        if firstAttempt is not None:
            score = self.mastermind.scoreAttempt(firstAttempt)
            self.evaluate(firstAttempt, score)

        self.solve()

    def setPossibleSolutions(self):
        self.possibleSolutions = list(itertools.product(self.colors,
                                                        repeat=self.holes))

    def getAttempt(self):
        return random.choice(self.possibleSolutions)

    def evaluate(self, attempt, score):
        assert isinstance(attempt, list) or isinstance(attempt, tuple)
        assert len(attempt) == self.holes

        assert isinstance(score, tuple)

        self.possibleSolutions = [
            solution for solution in self.possibleSolutions
            if score == self.mastermind.compareCodes(attempt, solution)
        ]

    def solve(self):
        while not self.mastermind.isFinished():
            attempt = self.getAttempt()
            score = self.mastermind.scoreAttempt(attempt)
            self.evaluate(attempt, score)


class Statistics:
    def __init__(self, numberOfColors, holes, runs):
        assert isinstance(numberOfColors, int)
        assert numberOfColors > 0

        assert isinstance(holes, int)
        assert holes > 0

        assert isinstance(runs, int)
        assert runs > 0

        self.attempts = []

        for i in range(runs):
            mastermind = Mastermind(list(range(numberOfColors)), holes)
            Solver(mastermind)
            self.attempts.append(mastermind.getAttempts())

    def getMeanAttempts(self):
        return statistics.mean(self.attempts)

    def getStdev(self):
        return statistics.stdev(self.attempts)

    def getMinAttempts(self):
        return min(self.attempts)

    def getMaxAttempts(self):
        return max(self.attempts)


if __name__ == "__main__":
    stats = Statistics(6, 4, 10000)

    print("mean: {}\n".format(stats.getMeanAttempts())
          + "stdev: {}\n".format(stats.getStdev())
          + "min: {}\n".format(stats.getMinAttempts())
          + "max: {}".format(stats.getMaxAttempts()))
