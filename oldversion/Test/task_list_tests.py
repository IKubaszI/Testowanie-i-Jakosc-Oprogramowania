import unittest


from src.task_list import TaskList

class TaskListTestCase(unittest.TestCase):
        def test_add_task_should_add_task_to_list(self):
            task_list = TaskList()

            task_list.add_task("Buy milk")

            self.assertEqual(task_list.tasks(), ["Buy milk"])
        def test_remove_task(self):
            task_list = TaskList()

            task_list.remove_task("Buy milk")
            self.assertEqual(task_list.tasks(), [])


        def test_add_multiple_task(self):
            task_list = TaskList()

            task_list.add_multiple_task(["Buy Milk", "Buy cheese", "Buy smth else"])

            self.assertEqual(task_list.tasks(), ["Buy Milk", "Buy cheese", "Buy smth else"])
if __name__ == '__main__':
    unittest.main()