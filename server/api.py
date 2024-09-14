import http.client
import json
import random

def question(question):
    connection = http.client.HTTPSConnection("chatgpt-42.p.rapidapi.com")
    params_to_search = {
        "messages": [
            {
                "role": "user",
                "content": type_quest(question)
            }
        ],
        "system_prompt": "",
        "temperature": random_temperature(),
        "top_k": random_topk(),
        "top_p": random_topp(),
        "max_tokens": random_token(),
        "web_access": random_web()
    }

    params_to_search_json = json.dumps(params_to_search)
    
    connection_key = {
        'x-rapidapi-key': "03f5a33791msh11c0f158e2383b6p192c6fjsn9e903461d4fc",
        'x-rapidapi-host': "chatgpt-42.p.rapidapi.com",
        'Content-Type': "application/json"
    }

    connection.request("POST", "/conversationgpt4-2", params_to_search_json, connection_key)

    res = connection.getresponse()
    search_result = res.read()
    search_result_decode = search_result.decode("utf-8")

    search_result_decode = json.loads(search_result_decode)

    return search_result_decode['result']

def type_quest(quest):
    list = [" (resposta curta)"," (resposta com linguagem coloquial)", " (resposta longa)", " (resposta detalhada)", " (resposta curta com linguagem informal)", " (resposta errada)"]
    random_choice = random.choice(list)
    result_string = quest + random_choice
    return result_string

def random_temperature():
    random_temperature = random.randint(1, 10)
    random_temperature = random_temperature / 10
    float(random_temperature)
    return random_temperature

def random_topk():
    return random.randint(1, 10)

def random_topp():
    random_topp = random.randint(1, 10)
    random_topp = random_topp / 10
    float(random_topp)
    return random_topp

def random_token():
    return random.randint(100, 250)

def random_web():
    list = [True, False]
    return random.choice(list)

