from django.test import TestCase
from .functions import longest_word


class LongestWordTestCases(TestCase):

    def test_it_should_return_saturn(self):
        assert longest_word(
            'ajsxuytcnhre', 
            ['mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune']
        ) == 'saturn'

    def test_it_should_not_return_uranus(self):
        assert longest_word(
            'ajsxuytcnhre', 
            ['mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune']
        ) != 'uranus'
    
    def test_it_against_file(self):
        with open('valerdat/google-10000-english.txt') as f:
            lines = [line.strip() for line in f.readlines()]
            assert longest_word('optonoceari', lines) == 'cooperation'