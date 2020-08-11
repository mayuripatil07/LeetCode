class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        queue = deque([s])
        seen = set()
        while(queue):
            curr_string = queue.pop()
            for word in wordDict:
                if curr_string.startswith(word):
                    new_string = curr_string[len(word):]
                    if new_string == "":
                        return True

                    if new_string not in seen:
                        queue.append(new_string)
                        seen.add(new_string)
        return False
