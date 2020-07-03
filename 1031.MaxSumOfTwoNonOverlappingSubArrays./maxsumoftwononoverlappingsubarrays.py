class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        B = sorted(A)
        res = []
        window_start = 0
        s = 0
        for window_end in range(len(A)):
            s += A[window_end]
            if window_end - window_start + 1 == L:
                res.append((s, window_start, window_end))
                s -= A[window_start]
                window_start += 1
        res.sort()

        r = []
        window_start = 0
        s = 0
        for window_end in range(len(A)):
            s += A[window_end]
            if window_end - window_start + 1 == M:
                r.append((s, window_start, window_end))
                s -= A[window_start]
                window_start += 1
        r.sort()

        result = 0
        for t1 in r:
            Lt, Ls, Le = t1
            for t2 in res:
                Mt, Ms, Me = t2
                if self.overlap(Ls, Le, Ms, Me):
                    result = max(result, Lt+Mt)
        return result


    def overlap(self,Lstart,Lend,Mstart,Mend):
        if Mstart < Lstart and Mend < Lstart or Mstart > Lend:
            return True
        return False
        
