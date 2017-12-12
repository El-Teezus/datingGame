import json
from collections import namedtuple

jdat = json.load(open("dialog2.json"))
decodedJsonStr = json.dumps(jdat)
data = json.loads(decodedJsonStr, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))

def EmmaIntroduction():
    print(data.Person[0].Emma[0][0][1].Introduction[0])
    print(data.Person[0].Emma[0][0][0].Question1)
    print(data.Person[0].Emma[0][0][0].Answers1[0])
    print(data.Person[0].Emma[0][0][0].Answers1[1])
    print(data.Person[0].Emma[0][0][0].Answers1[2])
    selection = input('--->   ')
    if selection == data.Person[0].Emma[0][0][0].Answers1[0] or selection == '1':
        print(data.Person[0].Emma[0][0][0].Responses1[0])
    elif selection == data.Person[0].Emma[0][0][0].Answers1[1] or selection == '2':
        print(data.Person[0].Emma[0][0][0].Responses1[1])
    elif selection == data.Person[0].Emma[0][0][0].Answers1[2] or selection == '3':
        print(data.Person[0].Emma[0][0][0].Responses1[2])
    print(data.Person[0].Emma[0][0][1].Question2)
    print(data.Person[0].Emma[0][0][1].Answers2[0])
    print(data.Person[0].Emma[0][0][1].Answers2[1])
    print(data.Person[0].Emma[0][0][1].Answers2[2])
    selection = input('--->   ')
    if selection == data.Person[0].Emma[0][0][1].Answers2[0] or selection == '1':
        print(data.Person[0].Emma[0][0][1].Responses2[0])
    elif selection == data.Person[0].Emma[0][0][1].Answers2[1] or selection == '2':
        print(data.Person[0].Emma[0][0][1].Responses2[1])
    elif selection == data.Person[0].Emma[0][0][1].Answers2[2] or selection == '3':
        print(data.Person[0].Emma[0][0][1].Responses2[2])
    print(data.Person[0].Emma[0][0][1].Introduction[1])

EmmaIntroduction()