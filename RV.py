import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    print("tell something")
    audio = r.listen(source)
try:
    text = r.recognize_google(audio)
    print("you said:".format(text))
except sr.UnknownValueError:
    print("sorry i don't understand")
except sr.RequestError as e:
   print("sorry google speech API doesn't work anymore "+ format(e))