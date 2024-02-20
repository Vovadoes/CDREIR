import math

# from Charts import *

# from scipy.stats import t

# CONST
pi = 3.14159265
Yc = 17.3 * (10 ** -6)


class Calculation:
    def __init__(self, i, n):
        self.i = i
        self.n = n
        self.d = None

    def simple(self):
        self.d = self.i / (1 + self.n * (self.i / 100))

    def difficult(self):
        self.d = self.i / (1 + (self.i / 100))


if __name__ == "__main__":
    i = 1
    n = 2
    calculation = Calculation(i, n)
    calculation.simple()
    print(calculation.d)
    calculation.difficult()
    print(calculation.d)
    # ChartLinePLT(calculation.chart_v_y_data)
    # plt.legend()
    # plt.show()
