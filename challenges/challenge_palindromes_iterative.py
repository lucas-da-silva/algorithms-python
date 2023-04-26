def is_palindrome_iterative(word: str) -> bool:
    if len(word) < 1:
        return False

    if word == word[::-1]:
        return True

    return False
