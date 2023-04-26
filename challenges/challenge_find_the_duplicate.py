def validate_nums(nums: list[int]) -> bool:
    "Valida se uma lista de números é válida."

    try:
        if any(n < 0 for n in nums):
            return False
    except TypeError:
        return False

    return True


def find_duplicate(nums: list[int]):
    "Encontra o número duplicado em uma lista de números."

    if not validate_nums(nums):
        return False

    unique_nums = set()
    for num in nums:
        if num in unique_nums:
            return num
        else:
            unique_nums.add(num)

    return False
