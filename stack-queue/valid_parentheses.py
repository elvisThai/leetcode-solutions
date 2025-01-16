class Solution:
    def isValid(self, s: str) -> bool:
        """
        Given a string `s` containing just the characters '(', ')', '{', '}', '[' and ']',
        determine if the input string is valid.
        
        A valid string must satisfy the following conditions:
        1. Open brackets must be closed by the same type of brackets.
        2. Open brackets must be closed in the correct order.
        3. Every closing bracket must have a corresponding opening bracket.
        
        Args:
        s: str - A string containing just the characters '(', ')', '{', '}', '[' and ']'
        
        Returns:
        bool - True if the input string is valid, False otherwise
        """

        #initialize stack and dictionary where keys are closing bracket, values are opening
        stack = []
        brackets = {")":"(", "}": "{", "]":"["}

        #iterate over each char of string, append to stack if opening bracket
        for char in s:
            if char in brackets.values():
                stack.append(char)
            #otherwise if not opening bracket, must be closing, check to make sure the corresponding opening bracket is at the top of the stack and stack not empty
            elif stack and brackets[char] == stack[-1]:
                stack.pop() #pop the opening bracket if so 

            #else if neither work then this string does not have valid parentheses and can return false
            else:
                return False 
            
        #if we exit the loop and the stack is not empty it is not valid as that means we did not have correct amount of closing brackets for each opening
        return stack == [] 
