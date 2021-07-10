# pylint: disable=C0116
"""Test legal mentions view module.
"""
from django.test import TestCase

from supersub.views.legal_mentions_view import LegalMentionsView


class TestLegalMentionsView(TestCase):
    """Test legal mentions view class.
    """
    @classmethod
    def setUpTestData(cls):
        cls.legal_mentions_view = LegalMentionsView()

    def test_init__with_legal_mentions_view(self):
        self.assertTrue(self.legal_mentions_view)

    def test_init_with_attr_data_render(self):
        self.assertEqual(
            self.legal_mentions_view.data['render'],
            'supersub/legal_mentions.html'
        )
