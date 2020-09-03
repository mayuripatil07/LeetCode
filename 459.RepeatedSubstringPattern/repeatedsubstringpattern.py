class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        string = ''
        for i in s:
            string += i
            if len(s) == len(string):
                return False
            if len(s) % len(string) == 0:
                mult = len(s) // len(string)
                new_string = ""
                new_string = string * mult
                if new_string == s:
                    return True
