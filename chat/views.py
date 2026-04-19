from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import json

from .utils import generate_python_answer   # ✅ only this


def home(request):
    return render(request, 'chat/index.html')


@csrf_exempt
def chat_view(request):

    if request.method == "GET":
        return JsonResponse({"message": "API working"})

    if request.method == "POST":
        data = json.loads(request.body)
        message = data.get("message", "")

        reply = generate_python_answer(message)

        return JsonResponse({
            "response": reply
        })