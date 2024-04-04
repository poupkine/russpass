from django.shortcuts import render
from django.http import JsonResponse

import time

import requests
import json
import os

#import openai
#openai.api_key = 'YOUR_API_KEY'

def get_completion(prompt):
    url = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"
    role = f"ты - профессиональный туристический робот-планировщик путешествий для туриста. ты предлагаешь самые популярные туристические места для туристов, которые хотят посетить {prompt}, а также рассказываешь про погоду в ближайшее время в этих местах и порекомендуй, какую одежду взять"
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


def query_view(request):
    print("starting not testing")
    try:
        #if request.method == 'GET':
            #prompt = "Какие самые интересные достопримечатальности?"
            #try:
                #place = request.GET['prompt_place']
    
            #except:
                #place = "города Золотого кольца центральной части России"
            #print(place)
            ##response = get_completion(prompt, place)
            #return JsonResponse({'response': response})
        
        place = "города Золотого кольца центральной части России"
        
        if request.method == 'POST': 
            prompt = request.POST.get('prompt')
            response = "WRONG"
            #response = get_completion(prompt)  # , place)
            return JsonResponse({'response': response}) 
        return render(request, 'index.html')
    except Exception as err:
        print("error")
        print(err.args)


def test_view(request):
    try:
        if request.method == 'POST':
            prompt_test = request.POST.get('prompt_test_input_to_backend')
            text = f"I've got: {prompt_test}"
            print(text)
            response_test = text
            time.sleep(5)
            return JsonResponse({'response_test_from_backend': response_test})
    except Exception as err:
        print(err.args)
    return render(request, 'test.html')
