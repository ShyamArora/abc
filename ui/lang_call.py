
from translate import Translator


def eng_to_french(text):
    x=translator('en', 'fr', text)
    y =x[0][0][0]
    return y

def french_to_eng(text):
    x=translator('fr', 'en', text)
    y =x[0][0][0]
    return y

def german_to_eng(text):
    x=translator('de', 'en', text)
    y =x[0][0][0]
    return y
def italian_to_eng(text):
    x=translator('it', 'en', text)
    y =x[0][0][0]
    return y
def spanish_to_eng(text):
    x=translator('es', 'en', text)
    y =x[0][0][0]
    return y
def eng_to_german(text):
    x=translator('en', 'de', text)
    y =x[0][0][0]
    return y
def eng_to_spanish(text):
    x=translator('en', 'es', text)
    y =x[0][0][0]
    return y
def eng_to_italian(text):
    x=translator('en', 'it', text)
    y =x[0][0][0]
    return y
def japanese_to_eng(text):
    x=translator('ja', 'en', text)
    y =x[0][0][0]
    return y
def eng_to_japanese(text):
    x=translator('en', 'ja', text)
    y =x[0][0][0]
    return y

    

def lan_to_eng(msg1,language_):
    
    if language_=="Spanish":
        msg =spanish_to_eng(msg1)
    elif language_=="German":
        
        msg =german_to_eng(msg1)
        
    elif language_=="Italian":
        msg =italian_to_eng(msg1)
    elif language_=="Japanese":
        msg =japanese_to_eng(msg1)
    elif language_=="French":
        msg =french_to_eng(msg1)
    else:
        msg =msg1
       

    return msg
    

def eng_to_lang(sa1,language_):
    
    if language_=="Spanish":
        sa12 =eng_to_spanish(sa1)
    elif language_=="German":
        
        sa12 =eng_to_german(sa1)
    elif language_=="Italian":
        sa12 =eng_to_italian(sa1)
    elif language_=="Japanese":
        sa12 =eng_to_japanese(sa1)
    
    elif language_=="French":
        sa12 =eng_to_french(sa1)
    else:
        sa12 =sa1
   

    return sa12

