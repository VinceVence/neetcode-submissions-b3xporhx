class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        
        for s in strs:
            charset = [0] * 26
            for st in s:
                charset[ord(st) - ord("a")] += 1
            res[tuple(charset)].append(s)
        return list(res.values())


        