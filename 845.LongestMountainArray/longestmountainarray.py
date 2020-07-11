class Solution:
    def longestMountain(self, A: List[int]) -> int:
        i = 1
        max_length = 0
        while(i < len(A)):
            if A[i-1] < A[i]:
                starting_point = i - 1

                while(i< len(A) and A[i-1] < A[i]):
                    i += 1

                while( i < len(A) and A[i-1] > A[i]):
                    max_length = max(max_length, i - starting_point + 1)
                    i += 1
            else:
                 i += 1

        return max_length
