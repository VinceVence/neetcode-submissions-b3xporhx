class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cs = set()
        l = 0
        ls = 0

        for r in range(len(s)):
            while s[r] in cs:
                cs.remove(s[l])
                l += 1
            cs.add(s[r])
            ls = max(ls, r - l + 1)
        return ls


        