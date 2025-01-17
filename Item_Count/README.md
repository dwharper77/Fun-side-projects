# Item_Count

## Description
This is a graphical user interface (GUI) application for detecting and counting items in images using OpenCV and Tkinter. The application allows users to select multiple images, detect items within those images, and save the results.

## Features

- Detects items in images based on contours.
- Option to filter items by shape (circularity).
- Displays the number of detected items in a console window.
- Saves the images with detected items highlighted.

## Requirements

- Python 3.x
- OpenCV
- Tkinter
- NumPy

## Installation

1. Clone the repository or download the code.
2. Install the required packages using pip:

    ```bash
    pip install opencv-python-headless numpy
    ```

## Usage

1. Run the script:

    ```bash
    python Item_count.py
    ```

2. The GUI will open. Click the "Select Images" button to choose the images you want to process.
    !I_C_1 Image
3. A prompt will ask if all items are the same shape. Choose "Yes" or "No" based on your images.
4. The application will process the images and display the number of detected items in the console window.
    !I_C_2 Image
5. The processed images with detected items highlighted will be saved in the same directory as the original images.
    !I_C_3 Image

## Code Overview

- `detect_items(image_path, same_shape)`: Detects items in the given image and saves the result.
- `select_images()`: Prompts the user to select images and performs item detection.
- GUI setup using Tkinter.

## Example

!81 parts Image

!1134 tools Image

!detected_items_81 parts Image

!detected_items_1134 tools Image

## License

This project is not licensed.

## Contact
For any questions or issues, please contact:
- **Name**: Dennis Harper
- **Email**: dwharper77@gmail.com