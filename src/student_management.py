class StudentManagement:
    def __init__(self):
        self.students = {}

    def add_student(self, id: str, name: str, age: int) -> bool:
        if id in self.students:
            return False
        self.students[id] = {"name": name, "age": age, "grades": {}}
        return True

    def update_student(self, id: str, name: str, age: int) -> bool:
        if id not in self.students:
            return False
        self.students[id].update({"name": name, "age": age})
        return True

    def remove_student(self, id: str) -> bool:
        if id not in self.students:
            return False
        del self.students[id]
        return True

    def add_grade(self, student_id: str, subject: str, grade: float) -> bool:
        if student_id not in self.students:
            return False
        if grade not in [2.0, 3.0, 3.5, 4.0, 4.5, 5.0]:
            return False
        if subject not in self.students[student_id]["grades"]:
            self.students[student_id]["grades"][subject] = []
        self.students[student_id]["grades"][subject].append(grade)
        return True

    def avg_grades(self, subject: str) -> float:
        total_grade = 0
        total_students = 0
        for student in self.students.values():
            if subject in student["grades"]:
                grades = student["grades"][subject]
                total_grade += sum(grades)
                total_students += len(grades)
        if total_students == 0:
            return 0.0
        return total_grade / total_students

    def get_student(self, id: str):
        return self.students.get(id)

    def get_grades(self, student_id: str, subject: str):
        if student_id in self.students and subject in self.students[student_id]["grades"]:
            return self.students[student_id]["grades"][subject]
        return []
