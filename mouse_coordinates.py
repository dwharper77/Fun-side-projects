import pyautogui

def get_mouse_positions():
    positions = []
    print("Move your mouse to the desired positions and press 'Enter' to capture each position.")
    print("Press 'q' and 'Enter' to quit.")

    while True:
        user_input = input("Press Enter to capture the position or 'q' to quit: ")
        if user_input.lower() == 'q':
            break
        x, y = pyautogui.position()
        positions.append((x, y))
        print(f"Captured position: ({x}, {y})")

    print("Captured positions:", positions)

get_mouse_positions()