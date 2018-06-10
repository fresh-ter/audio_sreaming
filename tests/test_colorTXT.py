import json

color_list = {1 : "#ff0000",
			  2 : "#008000",
			  3 : "#483d8b",
			  4 : "#6a5acd",
			  5 : "#800080",
			  6 : "#ffffff",
			  7 : "#ffff00",
			  8 : "#ff8c00",
			  9 : "#ff60cb"}

with open(r"c:\audio_streaming\color.txt", "w", encoding="utf-8") as file:
    json.dump(color_list, file)

#загрузить из json
with open(r"c:\audio_streaming\color.txt", 'r', encoding='utf-8') as f: #открываем файл на чтение
    data = json.load(f) #загружаем из файла данные в словарь data

print(data)
input()