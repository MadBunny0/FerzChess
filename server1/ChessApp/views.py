from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import requests
import json

from ChessApp.Classes.queen import Queen

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


def home(request):
    return render(request, 'chessboard.html')

def lobby(request):
    return render(request, 'lobby.html')

@csrf_exempt
def move_piece(request):

    if request.method == 'POST':
        # Чтение и разбор JSON-данных из тела запроса
        data = json.loads(request.body.decode('utf-8'))
        row, col = map(int, data.get('position'))  # Получаем координаты ячейки
        cur_col = 1

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
    

@csrf_exempt
def process_positions(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                'chess_game',
                {
                    'type': 'send_positions',
                    'positions': data
                }
            )
            return JsonResponse({'status': 'success', 'result': data})
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)
    else:
        return JsonResponse({'status': 'error', 'message': 'Only POST method is allowed'}, status=405)