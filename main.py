from translate_texts import translate_directory
from speak_text import choose_and_speak

def main():
    print("🌍 Tekst Vertaler en Voorlezer")

    source = input("📂 Pad naar map met tekstbestanden: ").strip()
    target = input("📁 Pad voor vertaalde teksten: ").strip()
    language = input("🌐 Doeltaal (bijv. 'nl' of 'en'): ").strip()

    translate_directory(source, target, language)
    choose_and_speak(target)

if __name__ == "__main__":
    main()
