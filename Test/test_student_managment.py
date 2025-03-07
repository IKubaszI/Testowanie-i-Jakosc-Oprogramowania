import unittest
from src.student_management import StudentManagement

class StudentManagementTestCase(unittest.TestCase):

    def test_add_student_should_add_student(self):
        sm = StudentManagement()
        result = sm.add_student("S001", "John Doe", 20)
        self.assertTrue(result)
        self.assertEqual(sm.get_student("S001")["name"], "John Doe")
        self.assertEqual(sm.get_student("S001")["age"], 20)

    def test_update_student_should_update_student_info(self):
        sm = StudentManagement()
        sm.add_student("S001", "John Doe", 20)
        result = sm.update_student("S001", "John Doe", 21)
        self.assertTrue(result)
        self.assertEqual(sm.get_student("S001")["age"], 21)

    def test_remove_student_should_remove_student(self):
        sm = StudentManagement()
        sm.add_student("S001", "John Doe", 20)
        result = sm.remove_student("S001")
        self.assertTrue(result)
        self.assertIsNone(sm.get_student("S001"))

    def test_add_grade_should_add_grade(self):
        sm = StudentManagement()
        sm.add_student("S001", "John Doe", 20)
        result = sm.add_grade("S001", "Math", 4.5)
        self.assertTrue(result)
        self.assertEqual(sm.get_grades("S001", "Math"), [4.5])

    def test_avg_grades_should_calculate_average(self):
        sm = StudentManagement()
        sm.add_student("S001", "John Doe", 20)
        sm.add_student("S002", "Jane Smith", 22)
        sm.add_grade("S001", "Math", 4.0)
        sm.add_grade("S002", "Math", 5.0)
        avg = sm.avg_grades("Math")
        self.assertEqual(avg, 4.5)

if __name__ == '__main__':
    unittest.main()
