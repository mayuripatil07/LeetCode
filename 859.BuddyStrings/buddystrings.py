class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        for letter in A:
            if letter not in B:
                return False
        count = 0
        hmap1 = {}
        hmap2 = {}
        for i in range(len(A)):
            hmap1[A[i]] = i
        for j in range(len(B)):
            hmap2[B[j]] = j

        for key in hmap1:
            if hmap1[key] != hmap2[key]:
                index1 = hmap1[key]
                index2 = hmap2[key]
                count += 1
        if count == 0:
            for i in A:
                c = A.count(i)
                if c >= 2:
                    return True
            else:
                return False

        elif count > 2:
            return False
        else:
            new_A = list(A)
            new_A[index1], new_A[index2] = new_A[index2], new_A[index1]
            new = ''
            for i in new_A:
                new += i
        return new == B
