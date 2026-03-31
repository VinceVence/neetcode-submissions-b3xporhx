class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        if m > n: return False

        base = ord("a")
        win = [0] * 26
        need = [0] * 26

        for c in range(m):
            need[ord(s1[c]) - base] += 1
            win[ord(s2[c]) - base] += 1
        
        if win == need: return True

        for r in range(m, n):
            win[ord(s2[r]) - base] += 1
            win[ord(s2[r - m]) - base] -= 1
            if win == need: return True
        return False