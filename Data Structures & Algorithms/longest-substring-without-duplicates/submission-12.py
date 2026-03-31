class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cs = set()
        res = 0
        l = 0

        for r in range(len(s)):
            while s[r] in cs:
                cs.remove(s[l])
                l += 1
            cs.add(s[r]) 
            res = max(r - l + 1, res)
        return res
        