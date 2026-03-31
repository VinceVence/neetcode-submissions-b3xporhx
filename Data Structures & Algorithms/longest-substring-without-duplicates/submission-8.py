class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ns = set()

        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in ns:
                ns.remove(s[l])
                l += 1
            res = max(res, r - l + 1)
            ns.add(s[r])  
        return res      