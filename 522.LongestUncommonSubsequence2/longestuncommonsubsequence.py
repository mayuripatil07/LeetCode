class Solution:
    def submatch(self, s: str, sub: str) -> bool:
        i = -1
        for ch in sub:
            i = s.find(ch, i+1)
            if i < 0:
                return False
        return True

    def findLUSlength(self, strs: List[str]) -> int:

        count = collections.Counter(strs)

        strs.sort(key = len, reverse = True)

        for i in range(0,len(strs)):
            if count[strs[i]] == 1:
                for j in range(i):
                    if self.submatch(strs[j], strs[i]):
                        break
                else:
                    return len(strs[i])
        return -1
       
