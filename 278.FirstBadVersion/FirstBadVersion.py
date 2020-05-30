# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        high = n
        low = 0
        while(low < high):
            mid = (low + high) // 2
            if isBadVersion(mid) == False:
                low = mid + 1
            else:
                high = mid
        return low
