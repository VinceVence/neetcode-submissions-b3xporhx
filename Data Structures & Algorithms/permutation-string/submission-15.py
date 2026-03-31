class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)

        if m > n:
            return False

        base = ord("a")
        have = [0] * 26
        win = [0] * 26

        for i in range(m):
            have[ord(s1[i]) - base] += 1
            win[ord(s2[i])- base] += 1

        if win == have:
            return True

        for i in range(m, n):
            win[ord(s2[i]) - base] += 1
            win[ord(s2[i-m]) - base] -= 1
            if win == have:
                return True
        return False