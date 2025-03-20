import unittest
from src.student_management import StudentManagement

class StudentManagementTestCase(unittest.TestCase):

    def test_add_student_should_add_student(self):
        sm = StudentManagement()
        result = sm.add_student("nr1", "Jakub Sz", 22)
        self.assertTrue(result)
        self.assertEqual(sm.get_student("nr1")["name"], "Jakub Sz")
        self.assertEqual(sm.get_student("nr1")["age"], 22)

    def test_update_student_should_update_student_info(self):
        sm = StudentManagement()
        sm.add_student("nr1", "Jakub Sz", 22)
        result = sm.update_student("nr1", "Jakub Sz", 21)
        self.assertTrue(result)
        self.assertEqual(sm.get_student("nr1")["age"], 21)

    def test_remove_student_should_remove_student(self):
        sm = StudentManagement()
        sm.add_student("nr1", "Jakub Sz", 22)
        result = sm.remove_student("nr1")
        self.assertTrue(result)
        self.assertIsNone(sm.get_student("nr1"))

        # TO DO reszta ćwiczenia
    def test_add_grade_should_add_grade(self):
        sm = StudentManagement()
        sm.add_student("nr1", "Jakub Sz", 20)
        result = sm.add_grade("nr1", "Math", 4.5)
        self.assertTrue(result)
        self.assertEqual(sm.get_grades("nr1", "Math"), [4.5])

    def test_avg_grades_should_calculate_average(self):
        sm = StudentManagement()
        sm.add_student("nr1", "Jakub Sz", 20)
        sm.add_student("nr2", "Inny Typ", 22)
        sm.add_grade("nr1", "Math", 4.0)
        sm.add_grade("nr2", "Math", 5.0)
        avg = sm.avg_grades("Math")
        self.assertEqual(avg, 4.5)
if __name__ == '__main__':
    unittest.main()
