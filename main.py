import webbrowser
import time
import googletrans
import speech_recognition as sr
import gtts
import playsound

recognizer = sr.Recognizer()
translator = googletrans.Translator()

# To select input language https://cloud.google.com/speech-to-text/docs/languages
input_lang = 'hi-IN'
# To select output language https://developers.google.com/admin-sdk/directory/v1/languages
output_lang = 'te'
try:
    with sr.Microphone() as source:
        print('Speak Now')
        voice = recognizer.listen(source)
        text = recognizer.recognize_google(voice, language=input_lang)
        print(text)
except:
    pass
translated = translator.translate(text, dest=output_lang)
tx = translated.text
html_content = f"<html><head></head><h1>{tx}</h1><body></body></html>"
with open("index.html", "w", encoding="utf-8") as html_file:
    html_file.write(html_content)
    print("Hurray")

time.sleep(2)
webbrowser.open_new_tab("index.html")
print(translated.text)
converted_audio = gtts.gTTS(translated.text, lang=output_lang)
converted_audio.save('example.mp3')
playsound.playsound('example.mp3')
