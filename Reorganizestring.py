class Solution:
    def reorganizeString(self, S: str) -> str:
        if len(S) == 1:
            return S

        st = ""
        counter = collections.defaultdict(int)
        for i in S:
            if i in S:
                counter[i] += 1
            else:
                counter[i] = 1

        heap = [(-freq, letter) for letter, freq in counter.items()]
        heapq.heapify(heap)

        while(len(heap) > 1):
            freq1, curr = heapq.heappop(heap)
            freq2, curr_nxt = heapq.heappop(heap)

            st += curr
            st += curr_nxt

            new_freq1 = freq1 + 1
            if new_freq1 < 0:
                heapq.heappush(heap, (new_freq1, curr))

            new_freq2 = freq2 + 1
            if new_freq2 < 0:
                heapq.heappush(heap, (new_freq2, curr_nxt))


        if len(heap) == 1:
            freq, curr = heapq.heappop(heap)
            if freq < -1:
                return ""
            else:
                st += curr

        return st
