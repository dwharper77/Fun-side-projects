import pyautogui

def get_mouse_position_once():
    print("Move your mouse to the desired position and press 'Enter'.")
    input("Press Enter to capture the position...")
    x, y = pyautogui.position()
    print(f"Captured position: ({x}, {y})")

get_mouse_position_once()
