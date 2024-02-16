# import speech_functions, input_processing
from modules import *

def main():
    # while True:
    #     user_input = input("Enter 'listen' to start voice recognition or type your text: ")
    #     if user_input.lower() == 'listen':
    #         text = speech_functions.listen_and_recognize()
    #         print("You said: " + text)
    #     elif user_input.lower() == "open notepad":
    #         input_processing.open_notepad_and_type("Hello, this is a test message!")
    #         print("Notepad should open and type a message.")
    #     else:
    #         print("You entered: " + user_input)

    while True:

        user_input = input("Enter 'listen' to start voice recognition or type your text: ")
        if user_input.lower() == 'listen':
            text = listen_and_recognize()
            print("You said: " + text)

if __name__ == "__main__":
    main()
