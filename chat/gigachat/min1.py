"""Пример работы с чатом через gigachain"""
from langchain.schema import HumanMessage, SystemMessage
from langchain.chat_models.gigachat import GigaChat

# Авторизация в сервисе GigaChat
chat = GigaChat(credentials='M2JiMTRlODgtZmM3OS00NDVmLThkZWQtODhlYWUzNzI5M2ViOmFmYWU2ZWI4LTBjYzItNDQ0NC1hYTM0LTgwNGNkMmRiYTEzMQ==', verify_ssl_certs=False)

messages = [
    SystemMessage(
        content="Ты профессиональный гид-организатор туристических поездок"
    )
]

while(True):
    # Ввод пользователя
    user_input = input("User: ")
    print(chat.get_num_tokens(user_input))
    messages.append(HumanMessage(content=user_input))
    res = chat(messages)
    messages.append(res)
    # Ответ модели
    print("Bot: ", res.content)
