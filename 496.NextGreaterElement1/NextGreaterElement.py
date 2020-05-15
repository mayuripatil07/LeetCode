class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        hmap = collections.defaultdict(int)
        for num in nums2:
            while stack and stack[-1] < num:
                hmap[stack.pop()] = num
            stack.append(num)

        result = [hmap.get(x,-1) for x in nums1]
        return result
