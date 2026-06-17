class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temps_indexes = []
        results = [0] * len(temperatures)

        i = 0
        while i < len(temperatures):
            while len(temps_indexes) > 0 and temperatures[i] > temperatures[temps_indexes[-1]]:
                result = temps_indexes.pop()
                results[result] = i - result
            temps_indexes.append(i)
            i += 1

        return results

        # Time and Space Complexity: O(n)
