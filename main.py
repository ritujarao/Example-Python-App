#!/usr/bin/env python3

import requests
import random

if __name__ == "__main__":
    rand = random.randrange(1,10)
    r = requests.get(f"https://jsonplaceholder.typicode.com/todos/{rand}")
    print(r.text)