import json
with open('data(1).json', 'r', encoding='utf-8') as f:
    json_data = json.load(f)
# first_500_words = json_data[:3000]
with open('data3000.json', 'w', encoding='utf-8') as f:
    json.dump(json_data[:3000], f, ensure_ascii=False, indent=4)
