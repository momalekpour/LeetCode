class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = 0

        while students:
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                count = 0
            else:
                s = students.pop(0)
                students.append(s)
                count += 1

            if count == len(students):
                break

        return count
