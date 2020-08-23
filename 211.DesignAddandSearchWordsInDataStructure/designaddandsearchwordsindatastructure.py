class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s = defaultdict(list)

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        self.s[len(word)].append(word)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        if '.' not in word:
            if word in self.s[len(word)]:
                return True
            else:
                return False
        else:
            dot = set()
            for w in range(len(word)):
                if word[w] == '.':
                    dot.add(w)

            for i in self.s[len(word)]:
                searchword = i
                for index in dot:
                    searchword = searchword[:index] + '.' + searchword[index + 1:]
                if searchword == word:
                    return True
        return False




# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
