class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            x = -(int(str(abs(x))[::-1]))
        else:
            x = int(str(abs(x))[::-1])
        mini = -2147483648
        maxi = 2147483647
        if x >= maxi or x <= mini:
            return 0
        return x