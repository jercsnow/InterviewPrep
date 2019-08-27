class Solution:
    def isValid(self, s):
        if s == "":
            return True
        if len(s) % 2 == 1:
            return False

        brackets = {'(':')', '{':'}', '[':']'}
        bracket_stack = list()

        for char in s: # Assumes char is a bracket
            for key, value in brackets.items():
                if char == key:
                    matching = value
                    break
                elif char == value:
                    matching = key
                    break

            if len(bracket_stack) > 0:
                last_unmatched = bracket_stack[-1]
                if matching == last_unmatched:
                    bracket_stack.pop()
                else:
                    bracket_stack.append(char)
            else:
                bracket_stack.append(char)

        return len(bracket_stack) == 0 # No unmatched brackets left

# Test Program
s = "()(){(())" 
# should return False
print(Solution().isValid(s))

s = ""
# should return True
print(Solution().isValid(s))

s = "()"
# should return True
print(Solution().isValid(s))

s = "([{}])()"
# should return True
print(Solution().isValid(s))