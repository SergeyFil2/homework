from pprint import pprint
from random import randint
answers=("да","нет")
question=""
while question != "До свидания":
    question=input()
    answer=answers[randint(0, len(answers)-1)]
    pprint(answer)
