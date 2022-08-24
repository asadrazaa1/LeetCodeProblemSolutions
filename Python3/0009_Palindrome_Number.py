class Solution:
    def isPalindrome(self, x: int) -> bool:
        mini = -2147483648
        maxi = 2147483647

        if x <= mini or x >= maxi:
            return False
        return str(x) == str(x)[::-1]
