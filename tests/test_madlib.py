from textwrap import dedent

from madlib_cli.madlib import read_file, replace_words


class TestMadlib:
    def test_read_file(self):
        expected = 'I am a test file'
        actual = read_file('tests/test_file.txt')
        assert actual == expected

    def test_replace_words(self):
        test_string = """Do not replace me{replace me}{replace me too}{and me as well 123}"""
        expected = 'Do not replace me123'
        actual = replace_words('{[^\}]*}', ['1', '2', '3'], test_string)
