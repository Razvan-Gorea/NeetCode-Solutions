from collections import Counter

from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Iterative Approach:

        # if len(s) != len(t):
        #     return False

        # for char in s:
        #     if char in first_dict:
        #         first_dict[char] += 1
        #     else:
        #         first_dict[char] = 1
        
        # for char in t:
        #     if char in second_dict:
        #         second_dict[char] += 1
        #     else:
        #         second_dict[char] = 1

        # Using Counter
        first_dict = Counter(s)
        second_dict = Counter(t)

        return first_dict == second_dict
