class Solution:
    def isValid(self, s: str) -> bool:
        # Map each closing bracket to its expected opening bracket
        brackets = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        
        # Stack to keep track of opening brackets we've seen so far
        stack_dsa = []

        for bracket in s:
            if bracket in "({[":
                # It's an opening bracket, push it onto the stack
                # We'll match it later when we encounter its closing counterpart
                stack_dsa.append(bracket)

            elif bracket in ")]}":
                # It's a closing bracket — we need to check it matches the most
                # recent unmatched opening bracket (i.e. the top of the stack)

                if not stack_dsa:
                    # Stack is empty, meaning there's no opening bracket to match
                    # against this closing bracket — invalid
                    return False

                element = stack_dsa.pop()
                # Pop the most recent opening bracket off the stack

                if brackets[bracket] != element:
                    # brackets[bracket] gives us the opening bracket this closing
                    # bracket expects (e.g. brackets[")"] == "(")
                    # If that doesn't match what we popped, the brackets are
                    # crossed or mismatched (e.g. "(]") — invalid
                    return False

        # After processing every character, the stack should be empty
        # If it's not, there are unmatched opening brackets left over — invalid
        # e.g. s = "(((" would leave 3 items on the stack
        return len(stack_dsa) == 0


	# Time Complexity: O(N)
	# Space Complexity: O(N)
