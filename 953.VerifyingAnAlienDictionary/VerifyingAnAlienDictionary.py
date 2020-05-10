class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        idx = {}
        new_words = []
        for i, ch in enumerate(order):
            idx[ch] = i

        for i in range(1,len(words)):
            curr_word = words[i-1]
            next_word = words[i]

            first = 0
            last = 0

            while(first < len(curr_word) and last < len(next_word)):
                if idx[curr_word[first]] > idx[next_word[last]]:
                    return False
                elif idx[curr_word[first]] < idx[next_word[last]]:
                    break
                last += 1
                first += 1

            if first >= len(next_word):
                return False

        return True
