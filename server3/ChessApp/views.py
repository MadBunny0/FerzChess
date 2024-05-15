from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def move_piece(request):
    if request.method == 'POST':
        # Чтение и разбор JSON-данных из тела запроса
        data = json.loads(request.body.decode('utf-8'))
        position = data.get('position')  # Получаем координаты ячейки

        # Выполняем какую-то логику для обработки хода, например, выводим координаты ячейки
        print('Ход на позицию:', position)

        # Возвращаем JSON-ответ
        return JsonResponse({'success': True, 'message': 'Ход успешно выполнен', "data":data})
    else:
        # Если метод запроса не POST, возвращаем ошибку
        return JsonResponse({'success': False, 'message': 'Метод не поддерживается'})