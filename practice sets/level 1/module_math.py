import math
import pyttsx3
import pyfiglet #its a module to create ASCII art from text
a=25
print(math.sqrt(a))
print(math.pow(a,2))
print(math.pi)
Figlet = input("Enter the text : ")
print(pyfiglet.figlet_format(Figlet))

engine = pyttsx3.init()
engine.say("Yushaa I LOVE YOU")
engine.runAndWait()