import pyttsx3
from playsound import playsound
from gtts import gTTS
import os
def speak(text):
	  
	# Passing the text and language to the engine, 
	# here we have marked slow=False. Which tells 
	# the module that the converted audio should 
	# have a high speed
	myobj = gTTS(text=text, lang='en', slow=False)
	  
	# Saving the converted audio in a mp3 file named
	# welcome 
	myobj.save("welcome.mp3")
	  
	# Playing the converted file
	os.system("mpg321 -q welcome.mp3")

# speak("Hello world, I am mpg321, and I am glad that I am working flawlessly")


