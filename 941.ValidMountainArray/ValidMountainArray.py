class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3:
            return False
        for i in range(1,len(A)):
            if A[i-1] < A[i]:
                continue
            elif A[i-1] == A[i]:
                return False
            else:
                break
        index = i - 1
        if index == 0:
            return False
        for j in range(index, len(A)-1):
            if A[j] > A[j+1]:
                continue
            else:
                return False

        return True
