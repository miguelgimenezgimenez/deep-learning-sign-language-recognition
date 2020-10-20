import re
import random
import time
import speech_recognition as sr
import numpy as np

import matplotlib.pyplot as plt

print(sr.__version__)
import cv2
font = cv2.FONT_HERSHEY_SIMPLEX 
org = (50, 50) 
fontScale = 0.75
thickness = 2
color = (255, 0, 0) 

r = sr.Recognizer()
m = sr.Microphone()


def recognize_speech_from_mic(recognizer, microphone):
   
    # check that recognizer and microphone arguments are appropriate type
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    # adjust the recognizer sensitivity to ambient noise and record audio
    # from the microphone
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    # set up the response object
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

   
    try:
        response["transcription"] = recognizer.recognize_google(audio, language="es-ES")
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        # speech was unintelligible
        response["error"] = "Unable to recognize speech"

    return response


if __name__ == "__main__":
 
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    
    first_loop = True
    while True:
        blank_image = 255 * np.ones(shape=[512, 512, 3], dtype=np.uint8)
        print("Que letra te gustaria saber?")
        cv2.putText(blank_image, f"Que letra te gustaria saber?", org, font,  
                   fontScale, (255, 0, 0), thickness , cv2.LINE_AA) 
        guess = {}
        if not first_loop:
            print('before guess')
            guess = recognize_speech_from_mic(recognizer, microphone)
            print('after guess',guess)
        
        if guess.get("transcription",None):
          cv2.putText(blank_image, f"Transcripcion : {guess['transcription'].upper()}",  (org[0]+20,org[1]+280), font,  
                   fontScale, (0, 255, 0), thickness , cv2.LINE_AA) 
          match = re.findall(r"(\w)$",guess['transcription'],re.IGNORECASE)
          if match and match[0]:
            cv2.putText(blank_image, f"Match : {match[0].upper()}",  (org[0]+100,org[1]+330), font,  
                   fontScale, (255, 0, 0), thickness , cv2.LINE_AA) 
            letter = match[0].upper()
            picfile = f"data/asl_alphabet_test/{letter}_test.jpg"
            im = cv2.imread(picfile)
            blank_image[80:280,150:350] = im

    
        else:
            if not first_loop:
                cv2.putText(blank_image,"No te he entendido",  (org[0],org[1]+280), font,  
                       fontScale, (0, 0, 255), thickness , cv2.LINE_AA) 
                print("I didn't catch that. What did you say?\n")

            if guess.get("error", None):
                print("ERROR: {}".format(guess["error"]))
                cv2.putText(blank_image, f"ERROR {guess['error']}", (org[0],org[1]+480), font,  
                       fontScale, (0, 0, 255), thickness , cv2.LINE_AA) 
        first_loop=False
        cv2.imshow("Sign Language conversion", blank_image)
        if (cv2.waitKey(1) & 0xFF == ord("q")) or (cv2.waitKey(1) == 27):
              break 
        

        
