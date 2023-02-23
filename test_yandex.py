import unittest
from unittest import TestCase
from yandex_task import Yandex

class YandexTest(TestCase):

    def test_yandex(self):
        res = Yandex()
        self.assertIsInstance(res, int)
        self.assertEqual(res, 201)

class YandexTest_failure(TestCase):

    @unittest.expectedFailure
    def test_failure(self):
        res = Yandex()
        self.assertEqual(res,201)
        self.assertEqual(res,200)