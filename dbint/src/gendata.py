from common.db import Database
import json
import random


def gen():
    name = 'foo'
    temp = str(random.randint(1,101))
    Database.insert(collection='sensors',data={'name':name, 'temp':temp})

if __name__ == '__main__':
    Database.initialize()
    for i in range(20):
        gen()
