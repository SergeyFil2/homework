from mind import Mind

mind = Mind()
prompt = "Что Вас интересует?"

question = ""
while question != "До свидания": 
    print(prompt, end = ' ')
    answer = mind.think(input())
    print(answer)