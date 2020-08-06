class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last = {}
        result = []
        for i in range(len(S)-1,-1,-1):
            if S[i] not in last:
                last[S[i]] = i

        left = 0
        right = 0
        for idx, letter in enumerate(S):
            right = max(right, last[letter])

            if right == idx:
                result.append(right-left+1)
                left = right + 1
        return result
