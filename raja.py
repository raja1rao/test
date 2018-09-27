import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak Anything :")
    audio = r.listen(source)
    try:
		text = r.recognize_google(audio)
		r=text.split()
		for x in r:
			print(x)
    except:
        print("Sorry could not recognize what you said")
