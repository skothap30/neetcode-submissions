class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapWords = {}
        for word in strs:
            w = "".join(sorted(word))
            if w in mapWords:
                mapWords[w].append(word)
            else:
                mapWords[w] = [word]
        
        res = []
        for k,v in mapWords.items():
            res.append(v)

        return res


