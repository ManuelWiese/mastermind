from Statistics import Statistics
import time


def timer(function):
    def timedFunction():
        t1 = time.time()
        function()
        print("took {:.2f}s".format(time.time() - t1))

    return timedFunction

@timer
def benchmark():
    Statistics(2, 2, 100)
    Statistics(4, 3, 100)
    Statistics(6, 4, 100)
    Statistics(8, 5, 100)

if __name__ == "__main__":
    benchmark()
