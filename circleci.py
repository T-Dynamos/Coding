import requests
import sys

url = sys.argv[1]

text_ori = ""

while True:
    text = requests.get(url).text.split("\n")[-2]
    if text_ori != text:
        print(text)
        text_ori = text
