class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hmap = {}
        result = []
        if not nums1 or not nums2:
            return []

        for i in nums1:
            if i in hmap:
                hmap[i] += 1
            elif i not in hmap:
                hmap[i] = 1

        for j in nums2:
            if j in hmap:
                hmap[j] -= 1
                if j not in result:
                    result.append(j)

        return result
         
