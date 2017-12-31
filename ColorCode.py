class ColorCode:
    def __init__(self, code, colors):
        self.code = code
        self.len = len(code)
        self.range = range(self.len)
        self.set = set(code)
        self.count = {color: self.code.count(color) for color in colors}

    def __repr__(self):
        return str(self.code)

    def __str__(self):
        return "{} {} {}".format(self.code, self.set, self.count)

    def __len__(self):
        return self.len

    def __getitem__(self, index):
        return self.code[index]

    @staticmethod
    def compare(code1, code2):
        assert isinstance(code1, ColorCode)
        assert isinstance(code2, ColorCode)
        assert code1.len == code2.len

        colorMatches = 0
        for color in code1.set:
            count1 = code1.count[color]
            count2 = code2.count[color]

            if count1 < count2:
                colorMatches += count1
            else:
                colorMatches += count2

        matches = 0
        for i in code1.range:
            if code1.code[i] == code2.code[i]:
                matches += 1

        return matches, colorMatches


if __name__ == "__main__":
    code1 = ColorCode((0, 1, 2, 3, 0), [0, 1, 2, 3, 4, 5, 6, 7])
    code2 = ColorCode((0, 0, 2, 3, 1), [0, 1, 2, 3, 4, 5, 6, 7])

    print(code1)

    for i in range(100000):
        ColorCode.compare(code1, code2)
