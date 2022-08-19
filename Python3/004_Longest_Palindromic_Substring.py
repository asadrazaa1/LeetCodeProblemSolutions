class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        elif s == s[::-1]:
            return s

        palindrome_long = ""
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                temp = s[i:j]
                if temp == temp[::-1]:
                    if len(temp) > len(palindrome_long):
                        palindrome_long = temp

        return palindrome_long
