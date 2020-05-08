class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        st = re.findall("\w+", paragraph)
        counter = {}
        for i in st:
            if i.lower() in counter:
                counter[i.lower()] += 1
            else:
                counter[i.lower()] = 1

        heap = [(-freq, word) for word, freq in counter.items()]
        heapq.heapify(heap)

        while(heap):
            freq, word = heapq.heappop(heap)
            if word in banned:
                continue
            else:
                return word

        return ''
