class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        have = [0] * 26
        need = [0] * 26
        base = ord("a")

        for i in range(len(s1)):
            have[ord(s1[i]) - base] += 1 
            need[ord(s2[i]) - base] += 1
        
        if need == have:
            return True
        
        for i in range(len(s1), len(s2)):
            
            need[ord(s2[i]) - base] += 1
            need[ord(s2[i - len(s1)]) - base] -= 1
            if have == need:
                return True
        return False

        