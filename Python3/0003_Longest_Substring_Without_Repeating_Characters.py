class Solution:
    def hasRepeatingCharacter(self, word: str):
        for character in word:
            if word.count(character) >= 2:
                return True
        return False

    def lengthOfLongestSubstring(self, s: str) -> int:
        iterating_characters = set()
        left_pivot = 0
        res = 0
        for right_pivot in range(len(s)):
            while s[right_pivot] in iterating_characters:
                iterating_characters.remove(s[left_pivot])
                left_pivot += 1
            iterating_characters.add(s[right_pivot])
            res = max(res, right_pivot - left_pivot + 1)
        return res

#         Memory limit exceeding problem with this algorithm
#         if len(s) == 1:
#             return 1
#         elif len(s) == 0:
#             return 0

#         substrings = [s[i:j] for i in range(len(s))
#                       for j in range(i+1, len(s) + 1)]
#         substrings.sort(key=len)
#         substrings = substrings[::-1]


#         for each in substrings:
#             if not self.hasRepeatingCharacter(each):
#                 return len(each)
#         return 0
