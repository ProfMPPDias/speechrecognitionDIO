import speech_recognition as sr
import pyttsx3
import webbrowser

# Inicializa o reconhecedor de fala e o motor de text-to-speech
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Função para transformar texto em áudio
def text_to_speech(text):
    engine.say(text)
    engine.runAndWait()

# Função para transformar fala em texto
def speech_to_text():
    with sr.Microphone() as source:
        print("Ajustando o limiar de ruído...")
        recognizer.adjust_for_ambient_noise(source, duration=1.5)  # Ajuste de ruído mais longo
        print("Ouvindo...")

        try:
            audio = recognizer.listen(source)  # Sem timeout para evitar cortes
            text = recognizer.recognize_google(audio, language="pt-BR")
            print(f"Você disse: {text}")
            return text.lower().strip()  # Normaliza o texto
        except sr.WaitTimeoutError:
            print("Tempo de escuta esgotado. Nenhum áudio detectado.")
            return None
        except sr.UnknownValueError:
            print("Não entendi o que você disse.")
            return None
        except sr.RequestError:
            print("Erro na conexão com o serviço de reconhecimento de fala.")
            return None

# Função para abrir uma pesquisa no Wikipedia
def search_wikipedia(query):
    url = f"https://pt.wikipedia.org/wiki/{query.replace(' ', '_')}"
    webbrowser.open(url)
    text_to_speech(f"Abrindo a página da Wikipedia para {query}.")

# Função para abrir o YouTube
def open_youtube():
    webbrowser.open("https://www.youtube.com")
    text_to_speech("Abrindo o YouTube.")

# Função para abrir o Google Maps
def open_google_maps():
    webbrowser.open("https://www.google.com/maps")
    text_to_speech("Abrindo o Google Maps.")

# Função principal do assistente virtual
def virtual_assistant():
    text_to_speech("Olá! Como posso ajudar você hoje?")
    
    while True:
        command = speech_to_text()
        if not command:
            text_to_speech("Não entendi. Pode repetir?")
            continue

        if "wiki" in command:
            query = command.replace("wiki", "").strip()
            search_wikipedia(query if query else "Página principal")
        elif "youtube" in command:
            open_youtube()
        elif "google maps" in command:
            open_google_maps()
        elif "sair" in command or "parar" in command:
            text_to_speech("Até logo!")
            break
        else:
            text_to_speech("Desculpe, não entendi o comando. Tente novamente.")

# Executa o assistente virtual
if __name__ == "__main__":
    virtual_assistant()