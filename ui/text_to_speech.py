import os
from nltk import word_tokenize

def text_to_speech(value):
    sentence_words = word_tokenize(value)
    if len(sentence_words)>13:
        value="Message is big, So I have displayed it on the screen."    
    print(format(value).encode("utf-8"))
    tts = gTTS(value, lang='en')
    path = 'static/upload/'
    str1 =str(random.random())
    str2 = ".mp3"
    filename=str1+str2
    #filename = "audio.mp3"
##    <audio controls autoplay><source src="static/upload/'+reply['path']+'" type="audio/mp3"></audio>
    tts.save(os.path.join(path, filename))
    return filename 
