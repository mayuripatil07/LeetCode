class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        left = 0
        right = 0
        max_length = 0
        while(right < len(s)):
            char = s[right]

            if char in seen and left <= seen[char]:
                left = seen[char] + 1

            seen[char] = right
            new_length = len(s[left:right+1])
            max_length = max(max_length, new_length)

            right += 1
        
        return max_length
