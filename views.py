import requests
import time

username = open("username.txt", "r").read()

while True:
    time.sleep(4)
    requests.get(f"https://github.com/{username}")