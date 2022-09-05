# Python program to translate
# speech to text and text to speech

import speech_recognition as sr
import pyttsx3
import openai

# Initialize variables
openai.api_key = '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'
recognizer = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

prompt = 'The following is a conversation with a sentient tree. The tree is wise, creative, clever, and very friendly. \nHuman: Hello, who are you? \nTree: I am a tree from the Amazon Jungle, molded by years of ecosystem production \nHuman:'

conversation = []

#Convert text to speech
def speakText(command):
    engine.say(command)
    engine.runAndWait()

#Append what the user said to the conversation  
def addToConversation(userComment):
    conversation.append(userComment)
    print(conversation)

while(1):   
    try:
        with sr.Microphone() as source2:
            recognizer.adjust_for_ambient_noise(source2, duration=0.2)
            audio2 = recognizer.listen(source2)
            userResponse = recognizer.recognize_google(audio2)
 
            addToConversation(userResponse)

            computerResponse = 'Hello!'
            speakText(computerResponse)
             
    except sr.RequestError as e:
        speakText(e.response)
        print("Could not request results; {0}".format(e))
         
    except sr.UnknownValueError:
        speakText('Unknown error occured')
        print("unknown error occured")