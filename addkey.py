import json

with open('dataset/data_vi.json', 'r', encoding='utf-8') as f:
    json_data = json.load(f)

result = {}
for item in json_data:
    word = item[0]["word"]
    result[word] = item
with open('dataset/result_vi.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=4)    
