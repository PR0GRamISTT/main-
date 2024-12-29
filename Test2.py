def max_rook_sum(n, k):
    # Создаем доску n x n
    board = [[(i + 1) * (j + 1) for j in range(n)] for i in range(n)]

    # Список для хранения выбранных позиций ладей
    rooks_positions = []
    used_rows = set()
    used_cols = set()

    # Найдем максимальные элементы
    for _ in range(k):
        max_value = -1
        max_position = (-1, -1)

        for i in range(n):
            for j in range(n):
                if i not in used_rows and j not in used_cols:
                    if board[i][j] > max_value:
                        max_value = board[i][j]
                        max_position = (i, j)

        # Запоминаем позицию и отмечаем строку и столбец как занятые
        if max_position != (-1, -1):
            rooks_positions.append(max_position)
            used_rows.add(max_position[0])
            used_cols.add(max_position[1])

    # Вычисляем сумму значений на полях с ладьями
    total_sum = sum(board[i][j] for i, j in rooks_positions)

    return total_sum, rooks_positions


# Пример использования
n = 8  # Размер доски
k = 7  # Количество ладей
max_sum, positions = max_rook_sum(n, k)
print(f"Максимальная сумма: {max_sum}")
print(f"Позиции ладей: {positions}")