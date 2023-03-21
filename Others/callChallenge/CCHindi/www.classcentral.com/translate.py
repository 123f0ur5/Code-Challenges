# coding=utf8


import json
import re
from deep_translator import GoogleTranslator
import os


with open("dict.json", "r") as f:
    data = f.read()
cache_dict = json.loads(data)

GT = GoogleTranslator(target='hi')

def replace(word):
    word = word.group(0)
    if word == " " or "&&" in word or str(word).isnumeric():
        return word
                
    if word in cache_dict.keys():
        return cache_dict[word]
    else:
        cache_dict[word] = GT.translate(word)
        return cache_dict[word]

for root, dirs, files in os.walk("."):
    for file in files:
        path = os.path.join(root, file)

        if '.html' in path:
            print("Working on file: ", path)
            with open(path, encoding="utf-8") as f:
                data = f.read()
            
            html = data

            filtro = re.compile(u"(?<=(>))(\w|\d|\n|[().,\-…:\u00AD­­­­­­­­⌨️;@#$—%^& *\[\]’\"\'+–“”\/®°⁰!?|`~]| )+?(?=(<))")

            new_html = re.sub(filtro, replace, html)
                    
            with open(path, "w", encoding="utf-8") as f:
                f.write(new_html)

            data = json.dumps(cache_dict)
            with open('dict.json', 'w') as f:
                f.write(data)