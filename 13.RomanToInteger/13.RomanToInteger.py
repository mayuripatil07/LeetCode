class Solution:
    def romanToInt(self, s: str) -> int:
        hmap = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
        z= 0
        for i in range(len(s)-1):
            if hmap[s[i]] < hmap[s[i+1]]:
                z -= hmap[s[i]]
            elif hmap[s[i]] >= hmap[s[i+1]]:
                z += hmap[s[i]]

        z += hmap[s[-1]]
        return z
                
