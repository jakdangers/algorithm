from collections import defaultdict


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        r_dict = defaultdict(int)
        m_dict = defaultdict(int)

        for c in magazine:
            m_dict[c] += 1

        for c in ransomNote:
            r_dict[c] += 1

        for i, v in r_dict.items():
            if m_dict[i] < v:
                return False

        return True