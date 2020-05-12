import math
import sys
from os import rename
import requests

print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


print(greet("Alice"))
r = requests.get("https://pl.wikipedia.org/wiki/Programowanie_neurolingwistyczne")
print(r.status_code)

name = input("name?")
print("Hello,", name)
