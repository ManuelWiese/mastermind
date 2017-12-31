from ColorCode import ColorCode
import random


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
        code = []
        for i in range(self.holes):
            code.append(random.choice(self.colors))

        self.code = ColorCode(code, self.colors)

    def getColors(self):
        return self.colors

    def getHoles(self):
        return self.holes

    def scoreAttempt(self, attempt):
        assert isinstance(attempt, ColorCode)
        assert len(attempt) == self.holes

        self.attempts += 1
        score = ColorCode.compare(self.code, attempt)
        if score[0] == self.holes:
            self.finished = True
        return score

    def isFinished(self):
        return self.finished

    def getAttempts(self):
        return self.attempts
