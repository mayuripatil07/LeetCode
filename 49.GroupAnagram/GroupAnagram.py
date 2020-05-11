class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = collections.defaultdict(list)
        result = []
        for i in strs:
            a =  "".join(sorted(i))
            if a in hmap:
                hmap[a].append(i)
            else:
                hmap[a] = [i]

        for key,values in hmap.items():
            result.append(values)

        return result
            
