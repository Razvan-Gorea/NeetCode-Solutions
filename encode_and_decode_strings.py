class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            string_length = str(len(string))
            encoded = encoded + string_length + "#" + string
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        length_builder = ""

        i = 0
        while i < len(s):
            if s[i] != "#":
                length_builder = length_builder + s[i]
                i += 1
            else:
                string_finder = int(length_builder)
                result = s[i + 1: i + 1 + string_finder]
                decoded.append(result)
                length_builder = ""
                i = i + 1 + string_finder
        return decoded
