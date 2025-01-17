# Game Automation Script

This script automates the process of starting up and navigating in the game using GeForce NOW and PyAutoGUI.

## Description

The script performs the following steps:
1. Opens GeForce NOW using a shortcut.
2. Waits for GeForce NOW to load.
3. Clicks on the game "Elite Dangerous".
4. Logs in with Steam.
5. Starts the game and navigates through various menus to reach the galaxy map.

## Requirements

- Python 3.x
- PyAutoGUI
- Tkinter

## Installation

1. Install Python 3.x from python.org.
2. Install the required Python packages:
    ```sh
    pip install pyautogui
    ```

## Usage

1. Update the `shortcut_path` variable in the script to the path of your GeForce NOW shortcut.
2. Run the script:
    ```sh
    python your_script.py
    ```

## Notes

- Ensure that the screen resolution and game window positions match the coordinates used in the script.
- The script includes delays (`time.sleep()`) to account for loading times. Adjust these values if necessary.

## License

This project is for personal use and fun. Feel free to modify and share it.