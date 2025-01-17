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
   ![I_C_1](https://github.com/user-attachments/assets/78b7b840-97c8-433e-a24c-f42cdf380767)

3. A prompt will ask if all items are the same shape. Choose "Yes" or "No" based on your images.
4. The application will process the images and display the number of detected items in the console window.
    ![I_C_2](https://github.com/user-attachments/assets/48eeee4e-664a-483c-8e4d-ab1192e3b744)

5. The processed images with detected items highlighted will be saved in the same directory as the original images.
    


## Code Overview

- `detect_items(image_path, same_shape)`: Detects items in the given image and saves the result.
- `select_images()`: Prompts the user to select images and performs item detection.
- GUI setup using Tkinter.

## Example

![81 parts](https://github.com/user-attachments/assets/f46aa2cf-a465-4d0f-85e9-003a094188f6)

![1134 tools](https://github.com/user-attachments/assets/b379b7e1-5047-424e-9461-e9dec3995a31)

![detected_items_81 parts](https://github.com/user-attachments/assets/8f264603-13ed-4765-9908-11d228f7aeda)

![detected_items_1134 tools](https://github.com/user-attachments/assets/58f83a27-1605-450a-952d-f7a1c64f9d2e)


## License

This project is not licensed.

## Contact
For any questions or issues, please contact:
- **Name**: Dennis Harper
- **Email**: dwharper77@gmail.com
