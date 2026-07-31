class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for word in strs:

            result += str(len(word)) # length of the word
            result += "#" # separator
            result += word # adding the actual word

        return result  

    def decode(self, s: str) -> List[str]:

        words = []
        pos = 0  # current position in the string

        # find where the "#" is starting from pos

        while pos < len(s):
            hash_index = pos
            while s[hash_index] != "#":
                hash_index += 1

            # everything before "#" is the length number
            length = int(s[pos:hash_index])

            # The word starts after the "#" and has 'length' characters
            word = s[hash_index + 1 : hash_index + 1 + length]
            words.append(word)

            # moving pos to right after this word, for the next word
            pos = hash_index + 1 + length

        return words

            


