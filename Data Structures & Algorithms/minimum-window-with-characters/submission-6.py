class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        
        window, countT = {}, {}

        for c in t:
            countT[c] = countT.get(c, 0) + 1

        res = [-1, -1]
        resLen = float('infinity')
        need = len(countT)
        have = 0

        l = 0

        for r in range(len(s)):
            curr = s[r]
            window[curr] = window.get(curr, 0) + 1

            if curr in countT and window[curr] == countT[curr]:
                have += 1

            while need == have:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l: r + 1] if resLen != float('infinity') else ""
