import speech_functions, input_processing

def main():
    while True:
        user_input = input("Enter 'listen' to start voice recognition or type your text: ")
        if user_input.lower() == 'listen':
            text = speech_functions.listen_and_recognize()
            print("You said: " + text)
        else:
            print("You entered: " + user_input)

if __name__ == "__main__":
    main()
