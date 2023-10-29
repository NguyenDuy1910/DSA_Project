from googletrans import Translator
import json

def translate_definition(text):
    translator = Translator(service_urls=['translate.google.com'])
    translation = translator.translate(text, src='en', dest='vi')
    return translation.text

def translate_keys(json_data):
    for entry in json_data:
        meanings = entry.get("meanings")
        if meanings:
            for meaning in meanings:
                definitions = meaning.get("definitions")
                if definitions:
                    for definition in definitions:
                        definition_text = definition.get("definition")
                        if definition_text:
                            translated_text = translate_definition(definition_text)
                            definition["definition_vi"] = translated_text

# Load JSON data from 'response.json'
with open('data.json', 'r') as f:
    json_data = json.load(f)
    

# Translate definitions
for a in json_data:
    translate_keys(a)

# Save translated data to 'en_vi.json'
with open('vi.json', 'w', encoding='utf-8') as f:
    json.dump(json_data, f, ensure_ascii=False, indent=4)
# Print the translated definitions
# print(json_data)