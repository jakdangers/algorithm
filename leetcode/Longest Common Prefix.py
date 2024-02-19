class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]

        if len(strs) == 1:
            return res

        for v in strs[1:]:
            temp = ""
            res_length = len(res)
            curr_length = len(v)
            idx = 0

            while idx < res_length and idx < curr_length:
                if res[idx] != v[idx]:
                    break
                temp += v[idx]
                idx += 1
            res = temp

        return res

