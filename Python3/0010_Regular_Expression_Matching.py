import re


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        getmatchings = re.findall(p, s)

        if len(getmatchings) > 0:
            if getmatchings[0] == s:
                return True
            else:
                return False
        else:
            return False
