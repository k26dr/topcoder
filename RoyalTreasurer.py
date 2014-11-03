# TopCoder SRM 433 R1D2L1
__author__ = 'kedar'

class RoyalTreasurer:
    def __init__(self):
        return

    # A and B are int[]
    def minimalArrangement(self, A: list, B: list):
        B.sort()
        A.sort(reverse=True)
        return sum(x*B[i] for i,x in enumerate(A))


