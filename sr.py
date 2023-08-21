import keyboard, pyttsx3, datetime
import pygetwindow as pw

engine = pyttsx3.init()

def speak_text(text):
    """Function to convert text to speech"""
    engine.say(text)
    engine.runAndWait()

def exit_program():
    speak_text("exitting AudibleView")
    exit()

def get_window():
    active_window=pw.getActiveWindow()
    if(active_window):
        speak_text("title is %s." % active_window.title)
    else:
        speak_text("unable to get title")

def current_time():
    curren_time = datetime.datetime.now().time()
    curren_time = curren_time.strftime("%H:%M")# properly formatting the time
    speak_text(curren_time)

def current_date():
    curren_date = datetime.datetime.now().date()
    curren_date = curren_date.strftime("%d-%m-%Y")# properly formatting the date
    speak_text(curren_date)

# Define the key combinations and their associated functions
key_combinations = {
    "alt+d": exit_program,
    "insert+t": get_window,
    "f12+insert": current_time,
    "f12+insert,f12": current_date,
    # Add more combinations as needed
}

def main():
    print("AudibleView is running")
    speak_text("starting AudibleView")
    while True:  # main loop
        hotkey = keyboard.read_hotkey(suppress=False)
        if hotkey in key_combinations:
            key_combinations[hotkey]()
        elif hotkey:
            print("key pressed: %s \n" % hotkey)
            speak_text("%s" % hotkey)

if __name__ == "__main__":  # don't run if imported
    main()