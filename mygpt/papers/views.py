from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpRequest

from .utils import *


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "papers/index.html")

def process(request: HttpRequest) -> JsonResponse:
    input_text = request.POST.get("input")
    func = request.POST.get("func")
    lang = request.POST.get("lang")
    func_list = {
        "translate": translate,
        "modify": modify
    }
    return JsonResponse({"content": func_list[func](
        input_text=input_text.strip(),
        lang=lang
        )})