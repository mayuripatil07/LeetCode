class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter= {}
        curr_time = 0
        for task in tasks:
            if task in counter:
                counter[task] += 1
            else:
                counter[task] = 1

        heap = [(-freq,val) for val, freq in counter.items()]
        heapq.heapify(heap)

        while(heap):
            count = 0
            temp = []
            while(count <= n):
                curr_time += 1

                if heap:
                    freq, val = heapq.heappop(heap)

                    if freq < -1:
                        temp.append(((freq+1), val))

                if not temp:
                    break

                else:
                    count += 1

            for item in temp:
                heapq.heappush(heap,item)

        return curr_time
