def merge_sort(string: str) -> str:
    "Ordena uma string usando o algoritmo de merge sort"

    if len(string) <= 1:
        return string

    mid = len(string) // 2
    left = string[:mid]
    right = string[mid:]

    ordered_left = merge_sort(left)
    ordered_right = merge_sort(right)

    return "".join(merge(ordered_left, ordered_right))


def merge(left: list[str], right: list[str]) -> list[str]:
    "Faz o merge de duas listas ordenadas"

    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]

    return result


def is_anagram(first_string: str, second_string: str) -> tuple:
    "Verifica se duas strings são anagramas uma da outra"

    first_string_lower = first_string.lower() if first_string else ""
    second_string_lower = second_string.lower() if second_string else ""

    ordered_first_string = merge_sort(first_string_lower)
    ordered_second_string = merge_sort(second_string_lower)

    if not first_string or not second_string:
        return (ordered_first_string, ordered_second_string, False)

    are_anagrams = ordered_first_string == ordered_second_string

    return (ordered_first_string, ordered_second_string, are_anagrams)
