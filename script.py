import math
import sys
from os import rename

import requests

name = input("Your Name? ")
print("Hello, ", name)

print(sys.executable)


def greet(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


r = requests.get("naver.com")
print(r.status_code)
