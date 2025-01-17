import os
import time
import pyautogui
import tkinter as tk
from tkinter import messagebox

# Path to the GeForce NOW shortcut
shortcut_path = r"C:\Users\Dennis.Harper\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\NVIDIA GeForce NOW.lnk"

# Open GeForce NOW using the shortcut
os.startfile(shortcut_path)

# Wait for 5 seconds
time.sleep(10)

# Click on elite dangerous
pyautogui.click(771, 801)

time.sleep(110) # for loading

# click on send
pyautogui.click(1115, 715)
# click on log in with steam
time.sleep(4)
pyautogui.click(965,690)
pyautogui.mouseDown(965, 690)
time.sleep(0.5)
pyautogui.mouseUp(965, 690)
time.sleep(.5)
pyautogui.mouseDown(965, 690)
time.sleep(0.5)
pyautogui.mouseUp(965, 690)

# click on play
time.sleep(5)
pyautogui.mouseDown(426, 809)
time.sleep(0.5)
pyautogui.mouseUp(426, 809)

# Wait for game to load
time.sleep(500)
# Click Continue
pyautogui.mouseDown(340, 448)
time.sleep(0.5)
pyautogui.mouseUp(340, 448)

# Click open play
time.sleep(4)
pyautogui.mouseDown(294, 656)
time.sleep(0.5)
pyautogui.mouseUp(294, 656)

# Click on carrier services
time.sleep(15)
pyautogui.mouseDown(983, 964)
time.sleep(0.5)
pyautogui.mouseUp(983, 964)


# click on carrier management
time.sleep(4)
pyautogui.mouseDown(1003, 922)
time.sleep(0.5)
pyautogui.mouseUp(1003, 922)

# click on navigation
time.sleep(4)
pyautogui.mouseDown(99, 311)
time.sleep(0.5)
pyautogui.mouseUp(99, 311)

# click on open galaxy map
time.sleep(4)
pyautogui.mouseDown(372, 943)
time.sleep(0.5)
pyautogui.mouseUp(372, 943)

# click on search the galaxy
time.sleep(5)
pyautogui.mouseDown(929, 181)
time.sleep(0.5)
pyautogui.mouseUp(929, 181)

# Create a Tkinter root window
root = tk.Tk()
root.withdraw()  # Hide the root window

# Show a message box and wait for the user to press OK
messagebox.showinfo("Game Loaded", "Press OK when the game has loaded")
