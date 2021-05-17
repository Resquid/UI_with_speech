import speech_recognition as sr

r = sr.Recognizer()
cont = True
decision = "Yes"
#Start - start, End - exit, Button - button, Input - input,
while cont:
    with sr.Microphone() as source:
        print("Enter anything")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print(f'You said {text}')
        except sr.UnknownValueError:
            print("Ne rozume")
    decision = input("Do you want to continue - type Yes/No ")
    if decision == "Yes":
        cont = True
    elif decision == "No":
        cont = False
