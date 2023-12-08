class Solution:
    def checkIfPangram(self, sentence: str) -> bool:

        dic = {}

        for c in sentence:
            if c not in dic:
                dic[c] = True

        for c in "abcdefghijklmnopqrstuvwxyz":
            if c not in dic:
                return False

        return True

