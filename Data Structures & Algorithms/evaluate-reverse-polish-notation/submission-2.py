class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == "+" or i == "-" or i == "*" or i == "/":
                s1 = stack.pop()
                s2 = stack.pop()
                match i:
                    case "+":
                        stack.append(s2 + s1)
                    case "-":
                        stack.append(s2 - s1)              
                    case "*":
                        stack.append(s2 * s1)                       
                    case "/":
                        stack.append(int(s2 / s1))                     
            else:
                stack.append(int(i))
        return stack[0]