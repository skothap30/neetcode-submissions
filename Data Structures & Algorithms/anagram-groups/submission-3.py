class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapWords = {}
        for word in strs:
            w = "".join(sorted(word))
            if w in mapWords:
                mapWords[w].append(word)
            else:
                mapWords[w] = [word]

        return list(mapWords.values())


