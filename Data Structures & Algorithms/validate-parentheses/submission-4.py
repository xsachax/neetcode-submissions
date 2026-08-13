class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        p = {")": "(", "}": "{", "]": "["}
        for c in s:
            if c in p:
                if stack and stack[-1] == p[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return not stack
            
            



                