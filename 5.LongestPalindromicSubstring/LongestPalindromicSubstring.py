class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_palindrome = ""
        for i in range(len(s)):
            OddPalindrome = self.checkpalindrome(s, i, i)
            EvenPalindrome = self.checkpalindrome(s, i , i+1)

            longer_palindrome = EvenPalindrome if len(EvenPalindrome) > len(OddPalindrome) else OddPalindrome

            longest_palindrome = longest_palindrome if len(longest_palindrome) >= len(longer_palindrome) else longer_palindrome

        return longest_palindrome


    def checkpalindrome(self, s, left, right):
        left_index = 0
        right_index = 0
        while(left >= 0 and right < len(s)):
            if s[left] == s[right]:
                left_index = left
                right_index = right
            else:
                break
            left -= 1
            right += 1

        return s[left_index:right_index+1]
            
