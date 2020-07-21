class Solution:
    def countLargestGroup(self, n: int) -> int:
        hmap = {}
        for num in range(1,n+1):
            s = 0
            num_list = list(str(num))
            for i in num_list:
                s += int(i)
            if s in hmap:
                if num not in hmap[s]:
                    hmap[s].append(num)
            else:
                hmap[s] = [num]

        max_len = 0
        count = 0
        for key,value in hmap.items():
            if len(value) >= max_len:
                max_len = len(value)

        for key,value in hmap.items():
            if len(value) == max_len:
                count+= 1
        return count




            
