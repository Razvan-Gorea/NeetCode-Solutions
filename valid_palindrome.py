class Solution:
    def isPalindrome(self, s: str) -> bool:
        low_string = s.lower()
        no_space_string = [x for x in low_string if x.isalnum()]

        i = 0
        while i < len(no_space_string):
            if no_space_string[i] != no_space_string[len(no_space_string) - 1 - i]:
                return False
            i += 1
        
        return True

        # Time Complexity: N
        # Space Complexity: N
