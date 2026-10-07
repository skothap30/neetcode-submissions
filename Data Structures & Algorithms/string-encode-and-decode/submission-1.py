class Solution:

    def encode(self, strs: List[str]) -> str:
        enc = ""
        for string in strs:
            enc = enc + str(len(string)) + ":" + string
        return enc

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != ":":
                j += 1
            n = int(s[i:j]) #Goes all the way till index j but not including it
            # Goes to the first char after the delimiter until the end of string which is the current idx plus length (j + 1 + n)
            start = j + 1
            end = start + n
            res.append(s[start : end])
            i = end
        return res