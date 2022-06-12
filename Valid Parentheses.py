class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if len(stack)== 0:
                if s[i]== '(' or s[i]== '{' or s[i]== '[':
                    stack.append(s[i])
                else:
                    return False
            elif len(stack)!= 0:
                if s[i]== '(' or s[i]== '{' or s[i]== '[':
                    stack.append(s[i])
                elif stack[-1] == '{' and s[i] == '}':
                    stack.pop()
                elif stack[-1] == '(' and s[i] == ')':
                    stack.pop()
                elif stack[-1] == '[' and s[i] == ']':
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
