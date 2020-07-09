if not needle:
            return 0
        i = 0
        j = 0

        while(j < len(haystack)):
            if needle[0] in haystack[j]:
                if needle == haystack[j:j+len(needle)]:
                    return j
            j += 1
        return -1
