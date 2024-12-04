from django.shortcuts import render, redirect, reverse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import connection


@csrf_exempt
def chatbot_view(request):
    print("At chatbot_view")
    if request.method == 'POST':
        user_input = request.POST.get('message', '')
        print("user_input", user_input)

        # query to get one movie similarity from chatbot_chatmodel
        # query = f"SELECT answer\
        #         FROM chatbot_chatmodel\
        #         WHERE similarity(question, '{user_input}') > 0.3\
        #         ORDER BY similarity(question, '{user_input}') DESC\
        #         LIMIT 1;"
        # with connection.cursor() as cursor:
        #     cursor.execute(query)
        #     result = cursor.fetchone()

        # query to get one movie similarity from custom function get_a_similarity(USER INPUT)
        query = f"SELECT get_a_similarity('{user_input}');"
        with connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchone()

        # response_message = result[0] if result else "Sorry..😣 plz type message again.."
        response_message = result[0]
        print("response_message at chatbot_view", response_message)

        return JsonResponse({'response': response_message})
    else:
        return render(request, "chatbot/index.html")
