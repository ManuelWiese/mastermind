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
