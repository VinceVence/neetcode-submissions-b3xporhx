class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        if m > n:
            return False

        need = [0] * 26
        win  = [0] * 26

        # for ch in s1:
        #     need[ord(ch) - 97] += 1

        for i in range(m):
            need[ord(s1[i]) - 97] += 1
            win[ord(s2[i]) - 97] += 1

        if win == need:
            return True

        for i in range(m, n):
            win[ord(s2[i]) - 97] += 1
            win[ord(s2[i - m]) - 97] -= 1
            if win == need:
                return True

        return False
