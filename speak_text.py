import os
import pyttsx3

def list_text_files(directory):
    return [f for f in os.listdir(directory) if f.endswith(".txt")]

def read_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 160)  # spreektempo
    engine.say(text)
    engine.runAndWait()

def choose_and_speak(directory):
    files = list_text_files(directory)

    if not files:
        print("Geen tekstbestanden gevonden.")
        return

    print("Beschikbare vertaalde bestanden:")
    for i, file in enumerate(files):
        print(f"{i+1}. {file}")

    try:
        choice = int(input("Kies een nummer om voor te lezen: "))
        selected_file = files[choice - 1]
    except (ValueError, IndexError):
        print("Ongeldige keuze.")
        return

    full_path = os.path.join(directory, selected_file)
    content = read_file(full_path)
    print(f"Voorlezen van {selected_file}...\n")
    speak(content)
