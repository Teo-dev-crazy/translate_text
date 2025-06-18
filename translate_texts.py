import os
from deep_translator import GoogleTranslator

CHUNK_SIZE = 4500

def read_in_chunks(text, size=CHUNK_SIZE):
    return [text[i:i+size] for i in range(0, len(text), size)]

def translate_text(text, target_lang='nl'):
    translated = ""
    chunks = read_in_chunks(text)
    for chunk in chunks:
        translated += GoogleTranslator(source='auto', target=target_lang).translate(chunk) + "\n"
    return translated

def translate_directory(source_dir, dest_dir, target_lang='nl'):
    os.makedirs(dest_dir, exist_ok=True)
    files = [f for f in os.listdir(source_dir) if f.endswith('.txt')]

    for filename in files:
        source_path = os.path.join(source_dir, filename)
        dest_path = os.path.join(dest_dir, filename)

        with open(source_path, 'r', encoding='utf-8') as infile:
            original_text = infile.read()

        print(f"Vertalen: {filename}")
        translated_text = translate_text(original_text, target_lang)

        with open(dest_path, 'w', encoding='utf-8') as outfile:
            outfile.write(translated_text)

    print(f"\nKlaar! Bestanden opgeslagen in: {dest_dir}")
