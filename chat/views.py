from django.shortcuts import render, HttpResponse
from django.http import JsonResponse

import time

import requests
import json
import os

#import openai
#openai.api_key = 'YOUR_API_KEY'

def get_completion(prompt):
    url = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"
    role = f"ты - профессиональный туристический робот-планировщик путешествий для туриста. Сначала ты должен спросить о городе, который пользователь хочет посетить. Далее ты предлагаешь самые популярные туристические места для туристов, которые хотят посетить {prompt}, а также рассказываешь о самых интересных местах в этом городе. Расскажи об этом в 3-4 красочных предложениях. Далее дай ссылку на russpass.ru, и спроси пользователя все ли вам понравилось. Не повторяй слова"
    with open('token.txt', 'r') as f:
        token = f.read().rstrip()
        payload = json.dumps({
          "model": "GigaChat",
          "messages": [{
              "role": "system",
              "content": role,
          }, {
              "role": "user",
              "content": prompt,
          },

          ],

          "temperature": 1,
          "top_p": 0.1,
          "n": 1,
          "stream": False,
          "max_tokens": 450,
          "repetition_penalty": 1,
          "update_interval": 0
        })
        headers = {
          'Content-Type': 'application/json',
          'Accept': 'application/json',
          'Authorization': f'Bearer {token}'
        }

        response = requests.request("POST", url, headers=headers, data=payload, verify='ca.cer')
        answer = dict(json.loads(response.text))['choices'][0]['message']['content']

    return answer


def chat_view(request):
    print("starting not testing 1")
    try:
        if request.method == 'POST':
            prompt = request.POST.get('prompt')
            response = get_completion(prompt)  # , place)
            print(12)
            print(response)
            return JsonResponse({'response': response})
        return render(request, 'chat.html')
    except Exception as err:
        print("error")
        print(err.args)
        return render(request, 'chat.html')
        


def index_view(request):
    try:
        if request.method == 'POST':
            prompt = request.POST.get('prompt')
            text = f"I've got: {prompt}"
            print(text)
            response = text
            return JsonResponse({'response_test_from_backend': response})
    except Exception as err:
        print(err.args)
    return render(request, 'chat.html')


#def test_view(request):
    #try:
        #if request.method == 'POST':
            #prompt_test = request.POST.get('prompt_test_input_to_backend')
            #text = f"I've got: {prompt_test}"
            #print(text)
            #response_test = text
            #time.sleep(5)
            #return JsonResponse({'response_test_from_backend': response_test})
    #except Exception as err:
        #print(err.args)
    #return render(request, 'test.html')


def map_view(request):
    try:
        if request.method == 'POST':
            prompt_test = request.POST.get('prompt_test_input_to_backend')
            text = f"I've got: {prompt_test}"
            print(text)
            response_test = text
            return JsonResponse({'response_test_from_backend': response_test})
    except Exception as err:
        print(err.args)
    return render(request, 'map.html')


def game_view(request):
    try:
        if request.method == 'POST':
            prompt_test = request.POST.get('prompt_test_input_to_backend')
            text = f"I've got: {prompt_test}"
            print(text)
            response_test = text
            return JsonResponse({'response_test_from_backend': response_test})
    except Exception as err:
        print(err.args)
    return render(request, 'game_1.html')




