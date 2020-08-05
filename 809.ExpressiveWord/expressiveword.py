def expressiveWords(self, S: str, words: List[str]) -> int:
    def compress(s):
        res = []
        count = 1
        c = s[0]
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                res.append(c)
                res.append(count)
                c = s[i]
                count = 1
            else:
                count += 1

        res.append(c)
        res.append(count)

        return res

    a = compress(S)
    count = 0

    for word in words:
        l = compress(word)
        if len(l) != len(a):
            continue

        flag = True
        for i in range(0, len(l), 2):
            if l[i] != a[i] or int(a[i + 1]) < int(l[i + 1]) or (int(a[i + 1]) == 2 and int(l[i + 1]) == 1):
                flag = False
                break

        if flag:
            count += 1

    return count
