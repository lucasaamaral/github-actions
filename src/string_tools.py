"""Small string helpers used by the unit tests."""


def reverse_text(text: str) -> str:
    return text[::-1]


def is_palindrome(text: str) -> bool:
    normalized = "".join(char.lower() for char in text if char.isalnum())
    return normalized == normalized[::-1]


def count_words(text: str) -> int:
    return len(text.split())


def title_case(text: str) -> str:
    return text.title()


def remove_vowels(text: str) -> str:
    vowels = set("aeiouAEIOU")
    return "".join(char for char in text if char not in vowels)
