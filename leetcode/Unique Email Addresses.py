class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:

        s = set()

        for email in emails:

            words = email.split("@")
            local = []
            for c in words[0]:

                if c.isalpha():
                    local.append(c)
                if c == "+":
                    break
            u = "".join(local) + "@" + words[1]
            s.add(u)

        return len(s)