class Solution:
    def myAtoi(self, s: str) -> int:
        #         if len(s) == 0:
        #             return 0

        #         mini = -2147483648
        #         maxi = 2147483647

        #         string_split = s.split(' ')
        #         for each in string_split:
        #             try:
        #                 if int(each):
        #                     if int(each) <= maxi or int(each) >= mini:
        #                         return each
        #             except ValueError:
        #                 pass

        #         return 0
        if len(s) == 0:
            return 0
        #         removing spaces
        list_of_characters = list(s.strip())
        #         if string was only spaces
        if len(list_of_characters) == 0:
            return 0
        #         if string starts with minus sign
        sign = -1 if list_of_characters[0] == '-' else 1
        #         removing sign
        if list_of_characters[0] in ['-', '+']:
            del list_of_characters[0]

        ret, i = 0, 0
        while i < len(list_of_characters) and list_of_characters[i].isdigit():
            ret = ret * 10 + int(list_of_characters[i])
            i += 1

        return max(-2 ** 31, min(sign * ret, 2 ** 31 - 1))