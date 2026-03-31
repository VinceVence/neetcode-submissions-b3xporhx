class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        
        for s in strs:
            charset = [0] * 26
            for c in s:
                charset[ord(c) - ord("a")] += 1
            d[tuple(charset)].append(s)
        print(d)
        return list(d.values())