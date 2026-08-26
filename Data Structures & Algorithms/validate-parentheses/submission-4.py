class Solution:
    def isValid(self, s: str) -> bool:
        m = {')': '(', '}': '{', ']': '['}
        stack = []

        for i in range(len(s)):
            if s[i] in ["(", "{", "["]:
                stack.append(s[i])
            else:
                if stack:
                    c = stack.pop()
                    if c == '(' and s[i] != ')':
                        return False
                    elif c == '{' and s[i] != '}':
                        return False
                    elif c == '[' and s[i] != ']':
                        return False
                else:
                    return False
        
        return not stack