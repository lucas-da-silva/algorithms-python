def is_palindrome_recursive(
    word: str, low_index: int, high_index: int
) -> bool:
    "Verifica se uma palavra é um palíndromo usando recursão."

    try:
        if word[low_index] != word[high_index]:
            return False

        if low_index >= high_index:
            return True

        return is_palindrome_recursive(word, low_index + 1, high_index - 1)
    except IndexError:
        return False
