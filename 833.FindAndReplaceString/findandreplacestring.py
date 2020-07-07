st = ""
        for i in S:
            st += i
        for i,s,t in sorted(zip(indexes, sources, targets), reverse = True):
            if s == S[i:i+len(s)]:
                    st = st[:i] + t + st[i + len(s):]

        return st
