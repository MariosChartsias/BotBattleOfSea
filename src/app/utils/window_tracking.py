import subprocess
import time
import pygetwindow as gw

# Start Notepad
subprocess.Popen('C:\\Games\\Gamepatron\\Battle of Sea\\Game\\launcher.exe')
time.sleep(2)  # Give Notepad time to open

# Function to continuously check if Notepad is in focus
def continuously_check_notepad_focus():
    while True:
        notepad_windows = gw.getWindowsWithTitle('Battle of Sea')
        if notepad_windows:
            notepad = notepad_windows[0]  # Assuming the first Notepad window should be focused
            if notepad.isActive:
                print("Notepad is in focus.")
            else:
                print("Notepad is not in focus.")
        else:
            print("Notepad is not running.")
        time.sleep(1)  # Check every second

continuously_check_notepad_focus()
