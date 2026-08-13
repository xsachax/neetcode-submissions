class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == "(" or i == "{" or i == "[":
                stack.append(i)
            elif len(stack) == 0:
                return False
            elif ( (i == ")" and stack.pop() != "(") or (i == "}" and stack.pop() != "{") or (i == "]" and stack.pop() != "[")):
                return False
        return len(stack) == 0
                