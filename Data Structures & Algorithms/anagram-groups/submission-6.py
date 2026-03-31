class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for s in strs:
            charset = [0] * 26
            for st in s:
                charset[ord(st) - ord("a")] += 1
            d[tuple(charset)].append(s)
        return (list(d.values()))

                
            
        
        