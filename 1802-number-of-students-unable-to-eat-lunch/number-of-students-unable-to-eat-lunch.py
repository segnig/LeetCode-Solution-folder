class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        while True:
            if students[0]==sandwiches[0]:
                students.remove(students[0])
                sandwiches.remove(sandwiches[0])
            else:
                students=students[1:]+[students[0]]
            if students==sandwiches==[]:
                return 0
            elif sandwiches[0] not in students:
                return len(students)