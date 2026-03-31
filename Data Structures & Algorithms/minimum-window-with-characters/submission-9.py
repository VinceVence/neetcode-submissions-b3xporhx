class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return False

        countT, window = {}, {}

        for c in t:
            countT[c] = countT.get(c, 0) + 1
        
        need = len(countT)
        have = 0

        res, resLen = [-1, -1], float('infinity')
        l = 0

        for r in range(len(s)):
            curr = s[r]
            window[curr] = window.get(curr, 0) + 1

            if curr in countT and countT[curr] == window[curr]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                window[s[l]] -= 1

                if s[l] in countT and countT[s[l]] > window[s[l]]:
                    have -= 1
                    
                l += 1
        l,r = res
        return s[l: r + 1] if resLen != float('infinity') else ""
        