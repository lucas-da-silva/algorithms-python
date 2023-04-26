def is_palindrome_iterative(word: str) -> bool:
    "Verifica se uma palavra é um palíndromo usando iteração."

    if len(word) < 1:
        return False

    if word == word[::-1]:
        return True

    return False
