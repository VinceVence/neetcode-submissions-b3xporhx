class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ss = set()
        longest = 0
        l = 0

        for i in range(len(s)):
            while s[i] in ss:
                ss.remove(s[l])
                l += 1
            ss.add(s[i])
            longest = max(longest, i - l + 1)
        return longest

        