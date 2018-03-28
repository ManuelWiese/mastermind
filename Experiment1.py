from Statistics import Statistics
import matplotlib.pyplot as plt

minHoles = 1
maxHoles = 5

minColors = 2
maxColors = 8

fig, ax_lst = plt.subplots(1, 1)

ax_lst.set_xlabel("Number of colors")
ax_lst.set_ylabel("Mean number of tries")

for holes in range(minHoles, maxHoles + 1):
    x = list(range(minColors, maxColors + 1))
    y = []
    error = []
    for colors in x:
        stats = Statistics(colors, holes, 1000)
        y.append(stats.getMeanAttempts())
        error.append(stats.getStdError())

    print(x, y, error)
    ax_lst.errorbar(x, y, yerr=error, label="{} holes".format(holes))

plt.show()
