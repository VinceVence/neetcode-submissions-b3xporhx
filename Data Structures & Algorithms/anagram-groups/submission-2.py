class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l = defaultdict(list)

        for w in strs:
            charset = [0] * 26
            for s in w:
                charset[(ord(s) - ord("a"))] += 1
            
            l[tuple(charset)].append(w)

        return list(l.values())
          

                