class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i=j=0
        m,n=len(name),len(typed)
        while j<n:
            if i < m and name[i]==typed[j]:
                i+=1
                j+=1
            elif i > 0 and typed[j]==name[i-1]:
                j+=1
            else:
                return False

        return i==m
