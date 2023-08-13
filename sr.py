import keyboard
import pyttsx3
import pygetwindow as gw

# Initialize the speech synthesizer


def speak_text(text):
    engine = pyttsx3.init()
    """Function to convert text to speech"""
    engine.say(text)
    engine.runAndWait()  # Process the speech request asynchronously
    engine.stop()  # Stop the speech synthesizer

def process_key_event(e):
    """Process keyboard events and speak the pressed key"""
    if e.event_type == keyboard.KEY_DOWN:
        key_name = e.name
        if key_name:
            print(f"Key Pressed: {key_name}")
            speak_text(key_name)

# Hook to capture keyboard events
keyboard.hook(process_key_event)

# Run the screen reader
try:
    print("Screen Reader is running. Press 'Ctrl + C' to exit.")
    while True:
#        engine.iterate()  # Process the speech requests

        # Check for "Insert + T" key combination
        if keyboard.is_pressed("insert+t"):
            active_window = gw.getActiveWindow()
            if active_window:
                window_title = active_window.title
                print(f"Active Window Title: {window_title}")
                speak_text(f"Active Window Title: {window_title}")

except KeyboardInterrupt:
    print("Screen Reader is exiting.")

