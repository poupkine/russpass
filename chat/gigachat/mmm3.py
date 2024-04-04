import requests
import json



def req(role_input, question):
    url = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"
    payload = json.dumps({
      "model": "GigaChat",
      "messages": [ {
              "role": "system",
              "content": role_input,
              },   {
          "role": "user",
          "content": question,
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
      'Authorization': 'Bearer eyJjdHkiOiJqd3QiLCJlbmMiOiJBMjU2Q0JDLUhTNTEyIiwiYWxnIjoiUlNBLU9BRVAtMjU2In0.oR3Px5PZQiwFTeOzjVzdqHaY9TuO4c3TspT1sl3Q8aOx3EX0XFcubNnB3eg4sYbu3iCGuAmhLUT8-GXSmiRqDka5G-tjYkIK3XcQ9JVpGLcGsAR7iInhx1EeWwrhEll4PB287wk38huBRtLZbhbXmiBzGXXkp7SxRfnM2WfXtZ2B6mll4Ftvlr0BiOe1TyqTFl_5HDfaXV52jylsvsvkVhTqzTTts-NTB4D0m1FY2a6cwV7wDzXL5KxwL90HPuLuTFZ146TCxZQdU4M8QLV1DqVdZdT-a5HJ4XyISQ1225fqaZBgk1mC0ABcS2DmlT4xaVBC5691p-m0vGjb2TJeNw.SYjZ3pBROqAIr2U3LMc7uQ.YgGrCxKuIuVmqAypxIlT8fzatWHhRFxo1qJcuj3zwU-xapMdx6SE8GdIDLtkG8vwuMBAEcktj-rWVTb5sLvLKFCNnwCvw_FQoHF4hacidkz-taWST0Iq7eUiMHVlu43AT_rO3YN2tEXOjg8uHHWzT--9My0nvHPz8OOpr1xVHAZMQOB76HfNEOeVRD9gz5BG_mhepoEZw1WA5fKaHp2pX_-jT0SLwbeusJeOstEuW6SMVgte6QiJLhmf-8GNaFUdL2aqi6tsvtJP4uk_8I2Q-gbslTFk-VoGtK4rYztj4VvhfF71DlMGWLHdwPCovrC5sf5hiemGF3Lje7duMpll2t01P4dhXJqbcnJnYpdfVvMoz3CjUqeJR18vHiCPYpsmVb3bpuuQKFeeoOntythtWbI70yt223hvxmc80tfq3xrW0Qv1ygHRNJ7e7huIbDQkTo-v1Y8Ld_miNAK2OpowdoacCzN41GNFekDOmA_N_8cskxO3PgIlZtuDZVxQAmpCttKsUhZIn9Wq7hdWISJUO0xT7tvJA0mlh--fwrKsBf1ZrjAMKzzoNDJ5AnACjs4BIbh-_leUPvX8l8rOj8i0QkbACFe89cABdbZuTMSCfzUwBu3lv0zBuFs7t8-Bv-gTqeyEGRvvDCq0kcG97Z5M5OjrwPVsp4-N7h3_mVHwlBYiLzP-ZVTXspA9elGPSGyrOHUT_Nv6Yfn9e21soUSl3scxbqxVp8_an1GuPTjDNmQ.HHQLKcfGkA7CWmpDtH33rdQ0f7JHohGo1dKvfwHWZoY'
}
    
    response = requests.request("POST", url, headers=headers, data=payload, verify='ca.cer')
    answer = dict(json.loads(response.text))['choices'][0]['message']['content']
    
    return answer

def start(role_input):
    i = 0
    while i < 12:
        
        user_input = input("введите ваш вопрос: ")
        print(req(role_input, user_input))
        i += 1
    
role_input = input("введите, какая роль модели, например, должна модель отвечать как академик или как школьник: ")
start(role_input)
