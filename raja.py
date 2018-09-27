import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak Anything :")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        y=text.split( )
	if x in y:
		print(x)
    except:
        print("Sorry could not recognize what you said")
