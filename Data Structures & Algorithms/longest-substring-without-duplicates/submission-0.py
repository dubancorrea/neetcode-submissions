class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}   # maps the characters
        left = 0 # left edge the current window with no duplicated
        max_len = 0

        for right in range(len(s)):
            char = s[right] # current character

            if char in seen and seen[char] >= left:
                left = seen[char] + 1

            seen[char] = right
            max_len = max(max_len , right - left + 1)

        return max_len
