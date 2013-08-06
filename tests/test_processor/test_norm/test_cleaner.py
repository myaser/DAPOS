from django.test import TestCase
from DAPOS.processor.norm import split


class DefaultTest(TestCase):
    def test_split(self):
        self.assertEqual('the first test <CD>123</CD> ',
                         split('the first test 123', '(\d+)', 'CD'))
        self.assertEqual('the first test123',
                         split('the first test123', '(\d+)', 'CD'))
        self.assertEqual('text not matching regex',
                         split('text not matching regex', '(\d+)', 'CD'))
