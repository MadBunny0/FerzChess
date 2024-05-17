from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import json
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


def home(request):
    return render(request, 'chessboard.html')

def lobby(request):
    return render(request, 'lobby.html')

@csrf_exempt
def move_piece(request):
    if request.method == 'POST':
        # Получаем данные о ходе из тела POST-запроса
        data = request.POST  # или request.body, в зависимости от формата данных

        

        # Возвращаем успешный JSON-ответ
        render(request, 'gen_website.html')

@csrf_exempt
def move_piece(request):
    if request.method == 'POST':
        # Получаем данные о ходе из тела POST-запроса
        data = request.POST  # или request.body, в зависимости от формата данных

        # Выполняем логику обработки хода
        # Например, сохраняем информацию о ходе в базе данных или обновляем игровое состояние

        # Возвращаем успешный JSON-ответ
        return JsonResponse({'success': True, 'message': 'Ход успешно обработан'})
    else:
        # Если запрос не является POST-запросом, возвращаем JSON-ответ с ошибкой
        return JsonResponse({'success': False, 'message': 'Метод не разрешен'})
    

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