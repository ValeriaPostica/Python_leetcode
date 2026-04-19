class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {')': '(', ']': '[', '}': '{'}
        
        for char in s:
            if char in '([{':  
                stack.append(char)
            elif char in ')]}':  
                if not stack:  
                    return False
                if stack[-1] != bracket_map[char]: 
                    return False
                stack.pop()  # Match found, remove opening bracket
           
        return len(stack) == 0  