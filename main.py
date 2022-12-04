import speech_recognition as sr
import pyttsx3

# initializing vars
listener = sr.Recognizer()
engine = pyttsx3.init()


def SpeechToText():
  # Exception handling
  try:
    # Microphone as the source
    with sr.Microphone() as source:
      # whatever we speak, is stored in the var "speech"
      speech = listener.listen(source)
      # Convert our speech to Text using "google"
      Text = listener.recognize_google(speech)
      #lower or upper anything works fine
      Text = Text.lower()
      print(Text)
      
      # open Text file, write the Text and close it
      file = open("Text.txt", "a")
      file.write(f"{Text}\n")
      file.close()
  except:
    pass

# Runs infinetley until we terminate the process
while True:
  SpeechToText()