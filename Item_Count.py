import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox, ttk
import cv2
import numpy as np

def detect_items(image_path, same_shape):
    """Detect items in the given image and save the result."""
    target_image = cv2.imread(image_path)
    if target_image is None:
        console.insert(tk.END, f"Error: The image file '{image_path}' could not be loaded. Please check the file path and try again.\n")
        return

    gray_image = cv2.cvtColor(target_image, cv2.COLOR_BGR2GRAY)
    blurred_image = cv2.GaussianBlur(gray_image, (15, 15), 0)

    adaptive_thresh = cv2.adaptiveThreshold(blurred_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
    edges = cv2.Canny(adaptive_thresh, 20, 80)

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))
    closed_edges = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)

    contours, _ = cv2.findContours(closed_edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    filtered_contours = []
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 50:
            if same_shape:
                perimeter = cv2.arcLength(cnt, True)
                circularity = 4 * np.pi * (area / (perimeter * perimeter))
                if 0.7 < circularity < 1.3:
                    filtered_contours.append(cnt)
            else:
                filtered_contours.append(cnt)

    count = len(filtered_contours)
    console.insert(tk.END, f'Number of items detected in {image_path}: {count}\n')

    cv2.drawContours(target_image, filtered_contours, -1, (0, 255, 0), 2)
    output_file_name = f'detected_items_{image_path.split("/")[-1]}'
    cv2.imwrite(output_file_name, target_image)
    console.insert(tk.END, f'The image with detected items has been saved to {output_file_name}\n')

def select_images():
    """Prompt the user to select images and perform item detection."""
    file_paths = filedialog.askopenfilenames(filetypes=[("Image files", "*.jpg *.png")])
    if not file_paths:
        return

    same_shape = messagebox.askyesno("Item Shape", "Are all of the items the same shape?")
    progress['maximum'] = len(file_paths)
    progress.start()

    for i, file_path in enumerate(file_paths):
        detect_items(file_path, same_shape)
        progress['value'] = i + 1
        root.update_idletasks()

    progress.stop()

# Create the main window
root = tk.Tk()
root.title("Item Count Tool")
root.configure(bg='black')

# Create and place the welcome message
welcome_label = tk.Label(root, text="Welcome to the Item Count Tool", fg='light green', bg='black', font=("Helvetica", 16, "bold"))
welcome_label.pack(pady=10)

prompt_label = tk.Label(root, text="Please click the button below to begin", fg='light green', bg='black', font=("Helvetica", 12))
prompt_label.pack(pady=5)

# Create and place the button to select images
select_button = ttk.Button(root, text="Select Images", command=select_images)
select_button.pack(pady=10)

# Create and place the console window
console = scrolledtext.ScrolledText(root, width=80, height=20, fg='light green', bg='black', font=("Helvetica", 10))
console.pack(pady=10)

# Add a progress bar
progress = ttk.Progressbar(root, orient='horizontal', mode='determinate', length=280)
progress.pack(pady=10)

# Start the main event loop
root.mainloop()