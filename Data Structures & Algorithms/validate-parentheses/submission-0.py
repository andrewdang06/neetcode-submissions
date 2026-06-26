class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {
         ")" : "(",
         "]" : "[", 
         "}" : "{" }

        for bracket in s:
            if bracket in closeToOpen:
                #close bracket
                if not stack:
                    return False
                top = stack.pop()
                if closeToOpen[bracket] != top:
                    return False
            else:
                #open bracket
                stack.append(bracket)
        
        if stack:
            return False
        else:
            return True
