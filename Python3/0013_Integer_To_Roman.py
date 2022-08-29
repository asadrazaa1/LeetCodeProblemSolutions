class Solution:
    def intToRoman(self, num: int) -> str:
        lookup = {
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I',
        }

        roman_number = ""
        for key, val in lookup.items():
            roman_number += val * (num // key)
            num -= key * (num // key)
        return roman_number