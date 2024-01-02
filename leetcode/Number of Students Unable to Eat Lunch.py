from collections import deque


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        de = deque(students)
        count = 0

        while len(de) > count:
            if de[0] == sandwiches[0]:
                de.popleft()
                sandwiches = sandwiches[1:]
                count = 0
            else:
                pop = de.popleft()
                de.append(pop)
                count += 1

        return len(de)


