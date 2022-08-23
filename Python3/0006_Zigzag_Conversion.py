class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = [[] for _ in range(numRows)]

        if numRows == 1: return s

        for i, char in enumerate(s):
            tmp = i % (2 * (numRows - 1))
            res[tmp if tmp < numRows else 2 * (numRows - 1) - tmp].append(char)

        return ''.join([''.join(res[i]) for i in range(numRows)])
