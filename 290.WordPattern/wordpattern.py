class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        pat = []
        for i in pattern:
            pat.append(i)
        str = str.split(' ')
        if len(pat) != len(str):
            return False
        hmap = {}
        s = set()
        i = 0
        j = 0
        while(i < len(pat) and j < len(str)):
            if str[j] not in hmap:
                hmap[str[j]] = pat[i]
            elif str[j] in hmap:
                if pat[i] != hmap[str[j]]:
                    return False

            i += 1
            j += 1
        for key,value in hmap.items():
            if value not in s:
                s.add(value)
            else:
                return False
        return True
