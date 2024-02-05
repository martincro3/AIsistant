import speech_recognition as sr

def listen_and_recognize():
    # Initialize the recognizer test
    r = sr.Recognizer()

    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Listening...")
        # Listen for the first phrase and extract the audio data
        try:
            audio = r.listen(source, timeout=5)
            # Recognize speech using Google's speech recognition
            return r.recognize_google(audio)
        except sr.UnknownValueError:
            return "Could not understand audio"
        except sr.RequestError:
            return "Could not request results"
        except sr.WaitTimeoutError:
            return "No speech detected"