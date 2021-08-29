from unittest import TestCase
from app import app


class BasicTestCase(TestCase):
    def setUp(self) -> None:
        self.client = app.test_client()
        self.value = 10

    def test_check_value(self):
        self.assertEqual(self.value, 10)