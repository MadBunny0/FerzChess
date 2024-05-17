from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def home(request):
    return render(request, 'chessboard.html')

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