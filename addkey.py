import json

with open('vi.json', 'r', encoding='utf-8') as f:
    json_data = json.load(f)

result = {}
for item in json_data:
    word = item[0]["word"]
    result[word] = item
with open('result.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=4)    
