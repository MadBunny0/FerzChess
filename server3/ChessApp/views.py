from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def move_piece(request):
    def is_safe(board, row, col):
        # Проверяем вертикаль
        for i in range(row):
            if board[i][col] == 1:
                return False

        # Проверяем левую верхнюю диагональ
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False

        # Проверяем правую верхнюю диагональ
        for i, j in zip(range(row, -1, -1), range(col, len(board))):
            if board[i][j] == 1:
                return False

        return True

    def solve_queens(board, row, start_col):
        if row >= len(board):
            return True

        for col in range(start_col, len(board)):
            if is_safe(board, row, col):
                board[row][col] = 1
                if solve_queens(board, row + 1, 0):
                    return True
                board[row][col] = 0

        return False

    def print_board(board):
        for row in board:
            print(row)

    def place_queens(initial_row, initial_col):
        board = [[0] * 8 for _ in range(8)]
        board[initial_row - 1][initial_col - 1] = 1

        if solve_queens(board, 0, initial_col):
            print("Ферзи успешно расставлены:")
            print_board(board)
        else:
            print("Невозможно расставить ферзей.")

    if request.method == 'POST':
        # Чтение и разбор JSON-данных из тела запроса
        data = json.loads(request.body.decode('utf-8'))
        row, col = map(int, data.get('position'))  # Получаем координаты ячейки
        cur_col = 3
        
        # Выполняем какую-то логику для обработки хода, например, выводим координаты ячейки
        print('Ход на позицию:', row, col)

        board = place_queens(row, col)
        print(board)

        # Возвращаем JSON-ответ
        return JsonResponse({'success': True, 'message': 'Ход успешно выполнен', "data":data})
    else:
        # Если метод запроса не POST, возвращаем ошибку
        return JsonResponse({'success': False, 'message': 'Метод не поддерживается'})