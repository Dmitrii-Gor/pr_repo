
from unittest import TestCase
from old_tasks import first_task, second_task, third_task

class HomeworkTask1(TestCase):
    def test_1(self):
        res = first_task()
        self.assertIsInstance(res, list)
        self.assertListEqual(res, [{'visit1': ['Москва', 'Россия']}, {'visit3': ['Владимир', 'Россия']}, {'visit7': ['Тула', 'Россия']}, {'visit8': ['Тула', 'Россия']}, {'visit9': ['Курск', 'Россия']}, {'visit10': ['Архангельск', 'Россия']}])

    def test_2(self):
        res = second_task()
        self.assertIsInstance(res, set)
        self.assertSetEqual(res,{98, 35, 213, 54, 119, 15})

    def test_3(self):
        res = third_task()
        self.assertIsInstance(res, tuple)
        self.assertIsNotNone(res)
        self.assertIn('yandex', str(res))