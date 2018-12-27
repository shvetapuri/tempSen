from common.db import Database
import json
import random


def gen():
    name = 'foo'
    temp = str(random.randint(1,101))
    print("inserting " + temp)
    Database.insert(collection='sensors',data={'name':name, 'temp':temp})

if __name__ == '__main__':
    Database.initialize()
    gen()
