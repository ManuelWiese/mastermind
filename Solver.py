from Mastermind import Mastermind

import random
import itertools


class Solver:

    def __init__(self, mastermind, firstAttempt=None):
        assert isinstance(mastermind, Mastermind)

        self.mastermind = mastermind

        self.colors = mastermind.getColors()
        self.holes = mastermind.getHoles()
        self.setPossibleSolutions()

        assert firstAttempt is None or isinstance(firstAttempt, list)

        assert (
            firstAttempt is None
            or len(firstAttempt) == mastermind.getHoles()
        )

        if firstAttempt is not None:
            score = self.mastermind.scoreAttempt(firstAttempt)
            self.evaluate(firstAttempt, score)

        self.solve()

    def setPossibleSolutions(self):
        self.possibleSolutions = list(
            itertools.product(self.colors, repeat=self.holes)
        )

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
