from gtts import gTTS

text = str(input("Enter the text you want to convert to speech: "))

tts = gTTS(text=text, lang='en')
tts.save("output.mp3")

print("Audio save successfulyy!!")
