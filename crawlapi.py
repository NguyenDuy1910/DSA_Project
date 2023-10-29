import requests
import json
import nltk
import random

# Tải dữ liệu từ nltk
nltk.download('words')

# Lấy danh sách các từ tiếng Anh
english_words = nltk.corpus.words.words()

# Lựa chọn ngẫu nhiên 10 từ tiếng Anh
selected_words = random.sample(english_words, 2500)

# Lưu trữ dữ liệu từ API
api_data = []
count = 0

# Gọi API và lưu dữ liệu từng từ vào danh sách api_data
for word in selected_words:
    response = requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}')
    if response.status_code == 200:
        data = response.json()
        if data:  # Kiểm tra xem phản hồi có dữ liệu không
            api_data.append(data)
            count += 1
            print(count)
        # if count >= 10:
        #     break
    else:
        print(f'Lỗi trong quá trình gọi API cho từ "{word}".')

# Lưu dữ liệu vào file JSON
with open('data.json', 'w') as f:
    json.dump(api_data, f)