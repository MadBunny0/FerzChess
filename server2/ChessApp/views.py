from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import requests
from ChessApp.Classes.queen import Queen

@csrf_exempt
def move_piece(request):

    if request.method == 'POST':
        # Чтение и разбор JSON-данных из тела запроса
        data = json.loads(request.body.decode('utf-8'))
        row, col = map(int, data.get('position'))  # Получаем координаты ячейки
        cur_col = 2

        # Выполняем какую-то логику для обработки хода, например, выводим координаты ячейки
        print('Ход на позицию:', row, col)
        
        q = Queen(8)
        q.run()

        print(f"Number of Solutions: {len(q.solutions)}")
        response = None
        for solution in q.solutions:
            print('for')
            if solution[col - 1] == row - 1:
                print(f'solution[cur_col] = {solution[cur_col - 1]}')
                print(f'solution: {solution}')
                print(f'row = {row}')
                res_row = solution[cur_col - 1] + 1
                result = {
                    'row': res_row,
                    'col': cur_col
                }
                print(result)
                response = requests.post('http://127.0.0.1:8001/process_positions/', json=result)
                print(response)
                break

        # Возвращаем JSON-ответ
        return JsonResponse({'data': response.json()})
    else:
        # Если метод запроса не POST, возвращаем ошибку
        return JsonResponse({'success': False, 'message': 'Метод не поддерживается'})