class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        base = ord('a')
        need = [0] * 26
        window = [0] * 26
        
        for i in range(len(s1)):
            need[ord(s1[i]) - base] += 1     
            window[ord(s2[i]) - base] += 1   

        if window == need:
            return True

        for i in range(len(s1), len(s2)):
            window[ord(s2[i - len(s1)]) - base] -= 1
            window[ord(s2[i]) - base] += 1
            if window == need:
                return True
        return False