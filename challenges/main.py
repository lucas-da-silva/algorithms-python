from challenge_study_schedule import study_schedule
from challenge_palindromes_recursive import is_palindrome_recursive
from challenge_palindromes_iterative import is_palindrome_iterative
from challenge_find_the_duplicate import find_duplicate, validate_nums
from challenge_encrypt_message import encrypt_message
from challenge_anagrams import is_anagram, merge_sort


from termcolor import colored


def main():
    print("-" * 75)

    # Teste da função study_schedule
    permanence_period = [(9, 12), (14, 17), (19, 21)]
    target_time = 15
    studying_at_the_same_time = study_schedule(permanence_period, target_time)
    print("Função", colored("study_schedule:", "blue"))
    print(
        f"Período de permanência: {permanence_period}\n"
        f"Horário alvo: {target_time}\n"
        f"Estudantes estudando no mesmo horário alvo: "
        f"{colored(studying_at_the_same_time, 'green')}\n"
    )

    # Teste da função is_palindrome_recursive
    word = "reviver"
    is_palindrome = is_palindrome_recursive(word, 0, len(word) - 1)
    print("Função", colored("is_palindrome_recursive:", "blue"))
    print(
        f"Palavra: {word}\nÉ palíndromo: {colored(is_palindrome, 'green')}\n"
    )

    # Teste da função is_palindrome_iterative
    word = "reviver"
    is_palindrome = is_palindrome_iterative(word)
    print("Função", colored("is_palindrome_iterative:", "blue"))
    print(
        f"Palavra: {word}\nÉ palíndromo: {colored(is_palindrome, 'green')}\n"
    )

    # Teste da função validate_nums
    nums = [1, 2, 3, 4, 5]
    is_valid = validate_nums(nums)
    print("Função", colored("validate_nums:", "blue"))
    print(f"Números: {nums}\nÉ válido: {colored(is_valid, 'green')}\n")

    # Teste da função find_duplicate
    nums = [1, 2, 3, 4, 4, 5]
    duplicate_num = find_duplicate(nums)
    print("Função", colored("find_duplicate:", "blue"))
    print(
        f"Números: {nums}\nNúmero duplicado: "
        f"{colored(duplicate_num, 'green')}\n"
    )

    # Teste da função encrypt_message
    message = "Esta mensagem deve ser encriptada"
    key = 8
    encrypted_message = encrypt_message(message, key)
    print("Função", colored("encrypt_message:", "blue"))
    print(
        f"Mensagem: {message}\nChave: {key}\nMensagem encriptada: "
        f"{colored(encrypted_message, 'green')}\n"
    )

    # Teste da função merge_sort
    string = "openai"
    ordered_string = merge_sort(string)
    print("Função", colored("merge_sort:", "blue"))
    print(
        f"String: {string}\nString ordenada: "
        f"{colored(ordered_string, 'green')}\n"
    )

    # Teste da função is_anagram
    first_string = "Tom Marvolo Riddle"
    second_string = "I am Lord Voldemort"
    ordered_strings, are_anagrams = is_anagram(first_string, second_string)[:2]
    print("Função", colored("is_anagram:", "blue"))
    print(
        f"Primeira string: {first_string}\nSegunda string: "
        f"{second_string}\nSão anagramas: {colored(are_anagrams, 'green')}"
    )

    print("-" * 75)


if __name__ == "__main__":
    main()
