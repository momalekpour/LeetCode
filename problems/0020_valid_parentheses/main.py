class Solution:
    def isValid(self, s: str) -> bool:
        # valid parentheses must follow a last-opened, first-closed order (like stack)
        stack = []
        close_to_open = {")": "(", "}": "{", "]": "["}

        for b in s:
            if b in close_to_open:
                if stack and stack[-1] == close_to_open[b]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(b)

        return False if stack else True
