class Solution:
    def isValid(self, s: str) -> bool:
        m = {')': '(', '}': '{', ']': '['}
        stack = []
        
        for char in s:
            if char in m and stack:
                t = stack.pop()
                if m[char] != t:
                    return False
            else:
                stack.append(char)
        
        return not stack