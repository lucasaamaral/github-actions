import unittest

from src.string_tools import (
    count_words,
    is_palindrome,
    remove_vowels,
    reverse_text,
    title_case,
)


class StringToolsTest(unittest.TestCase):
    def test_reverse_text(self):
        self.assertEqual(reverse_text("github"), "buhtig")

    def test_is_palindrome_ignores_case_and_punctuation(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))

    def test_count_words(self):
        self.assertEqual(count_words("GitHub Actions executa testes"), 4)

    def test_title_case(self):
        self.assertEqual(title_case("github actions"), "Github Actions")

    def test_remove_vowels(self):
        self.assertEqual(remove_vowels("Continuous Integration"), "Cntns ntgrtn")


if __name__ == "__main__":
    unittest.main()
