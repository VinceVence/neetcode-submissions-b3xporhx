class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        m = len(s1)
        n = len(s2)

        base = ord('a')
        need = [0] * 26
        window = [0] * 26

        for i in range(m):
            window[ord(s2[i]) - base] += 1
            need[ord(s1[i]) - base] += 1

        if window == need: return True

        for i in range(m, n):
            window[ord(s2[i]) - base] += 1
            window[ord(s2[i - m]) - base] -= 1
            if window == need:
                return True

        return False        