class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        s = list(s)
        i = 0
        j = len(s) - 1
        while(i < j):
            while(s[i] not in vowels and i < j):
                i += 1
            while(s[j] not in vowels and i < j):
                j -= 1
            s[i],s[j] = s[j],s[i]
            i ,j = i + 1, j-1

        return "".join(s)
