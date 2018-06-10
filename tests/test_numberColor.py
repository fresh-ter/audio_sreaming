import json

with open(r"c:\audio_streaming\number_color.txt", 'r', encoding='utf-8') as f:
    numberColor = json.load(f)

print(numberColor)
input()