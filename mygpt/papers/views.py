from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from gpt.utils import get_completion


def index(request):
    return render(request, "papers/index.html")

def process(request):
    input = request.POST.get("input")
    prompt = f"""Follow these steps to modify the content wrapped in triple quotes.
1. Please delete the redundant content in the text to make the content more compact;
2. Please add or modify the transitional content between sentences to make the content more smooth;
3. Please identify and correct typos and grammatical errors in the content;
4. If necessary, adjust the order of statements to make the content more logical;
5. Please find out where the content is not clear and use more explicit language to clarify;
6. You need to change the text to make it more academic.
7. Please give your answers in English.

'''
{input.strip()}
'''
"""
    output = get_completion(prompt)
    return JsonResponse({"content": output})