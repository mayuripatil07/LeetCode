class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words.sort()
        result = []
        counter = OrderedDict()
        for i in words:
            if i in counter:
                counter[i] += 1
            else:
                counter[i] = 1

        heap = [(-freq, word) for word, freq in counter.items()]
        heapq.heapify(heap)
        while(heap and k > 0):
            freq, word = heapq.heappop(heap)
            result.append(word)
            k -= 1
        return result


        
