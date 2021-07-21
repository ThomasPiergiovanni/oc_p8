# pylint: disable=C0116, W0212
"""Test result view module.
"""
from django.test import TestCase

from supersub.views.result_view import ResultView


class TestResultView(TestCase):
    """Test result view class.
    """
    @classmethod
    def setUpTestData(cls):
        cls.result_view = ResultView()

    def test_init__with_result_view(self):
        self.assertTrue(self.result_view)

    def test_init_with_attr_data_render(self):
        self.assertEqual(
            self.result_view._data['render'],
            'supersub/results.html'
        )

    def test_init_with_attr_data_redirect(self):
        self.assertEqual(
            self.result_view._data['redirect'],
            'supersub:index'
        )
