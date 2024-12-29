from itertools import permutations


def derangements(arr):
    n = len(arr)
    result = []

    for perm in permutations(arr):
        if all(perm[i] != arr[i] for i in range(n)):
            result.append(perm)

    return result


# Пример использования
N = 6
array = list(range(1, N + 1))  # Создаем массив [1, 2, 3, 4, 5]
deranged_permutations = derangements(array)

print(f"Количество дерangements для массива {array}: {len(deranged_permutations)}")
for perm in deranged_permutations:
    print(perm)