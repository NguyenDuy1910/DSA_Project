# import json
# import time
# import concurrent.futures
# import requests
# from requests.exceptions import Timeout
# from googletrans import Translator

# def translate_definition(text):
#     try:
#         response = requests.get('https://translate.google.com/', timeout=5)
#     except Timeout:
#         return "Translation service is not available at the moment. Please try again later."
    
#     translator = Translator(service_urls=['translate.google.com'])
#     translation = translator.translate(text, src='en', dest='vi')
#     return translation.text

# def translate_keys(json_data):
#     with concurrent.futures.ThreadPoolExecutor() as executor:
#         futures = []
#         for entry in json_data:
#             meanings = entry.get("meanings")
#             if meanings:
#                 for meaning in meanings:
#                     definitions = meaning.get("definitions")
#                     if definitions:
#                         for definition in definitions:
#                             definition_text = definition.get("definition")
#                             if definition_text:
#                                 future = executor.submit(translate_definition, definition_text)
#                                 futures.append((definition, future))
        
#         for definition, future in futures:
#             try:
#                 translated_text = future.result()
#                 definition["definition_vi"] = translated_text
#             except Exception as e:
#                 print("Error translating definition:", str(e))

# # Load JSON data from file
# with open('dataset/word_vi.json', 'r', encoding='utf-8') as f:
#     json_data = json.load(f)

# first_500_words = json_data[:1000]

# # Measure execution time
# start_time = time.time()
# for a in first_500_words:
# # Translate definitions
#     translate_keys(a)

# # Calculate execution time
# execution_time = time.time() - start_time
# print("Execution time:", execution_time, "seconds")

# # Save translated data to file
# with open('dataset/data(1).json', 'w', encoding='utf-8') as f:
#     json.dump(json_data, f, ensure_ascii=False, indent=4)
import json
import time
import concurrent.futures
import requests

API_KEY = "AIzaSyCD6VlJ1yI18hGdOsP690GNvlOHxpI6d8I"

def translate_definition(text):
    try:
        response = requests.get('https://translate.google.com/', timeout=5)
    except TimeoutError:
        return "Dịch vụ dịch không khả dụng vào lúc này. Vui lòng thử lại sau."

    # Gọi API Dịch Google Translate
    params = {
        "key": API_KEY,
        "q": text,
        "source": "en",
        "target": "vi"
    }
    response = requests.get("https://translation.googleapis.com/language/translate/v2", params=params)
    translation = response.json()["data"]["translations"][0]["translatedText"]
    return translation

def translate_keys(json_data):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for entry in json_data:
            meanings = entry.get("meanings")
            if meanings:
                for meaning in meanings:
                    definitions = meaning.get("definitions")
                    if definitions:
                        for definition in definitions:
                            definition_text = definition.get("definition")
                            if definition_text:
                                future = executor.submit(translate_definition, definition_text)
                                futures.append((definition, future))

        for definition, future in futures:
            try:
                translated_text = future.result()
                definition["definition_vi"] = translated_text
            except Exception as e:
                print("Lỗi dịch định nghĩa:", str(e))

# Tải dữ liệu JSON từ tệp
with open('dataset/word_vi.json', 'r', encoding='utf-8') as f:
    json_data = json.load(f)

first_500_words = json_data[:3000]

# Đo thời gian thực thi
start_time = time.time()
for a in first_500_words:
    # Dịch các định nghĩa
    translate_keys(a)

# Tính thời gian thực thi
execution_time = time.time() - start_time
print("Thời gian thực thi:", execution_time, "giây")

# Lưu dữ liệu đã dịch vào tệp
with open('dataset/data(1).json', 'w', encoding='utf-8') as f:
    json.dump(json_data, f, ensure_ascii=False, indent=4)