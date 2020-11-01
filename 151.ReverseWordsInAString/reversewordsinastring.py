class Solution:
    def reverseWords(self, s: str) -> str:
        a = s.split(" ")
        if len(a) == 1 :
            return s
        word_list = []
        for word in a:
            if word != '':
                word_list.append(word)

        i = 0
        j = len(word_list) - 1
        while(i <= j):
            word_list[i], word_list[j] = word_list[j], word_list[i]
            i += 1
            j -= 1
        return " ".join(word_list)
