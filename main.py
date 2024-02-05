from speech_functions import listen_and_recognize

def main():
    while True:
        text = listen_and_recognize()
        print("You said: " + text)

if __name__ == "__main__":
    main()
