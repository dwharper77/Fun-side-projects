from PIL import Image

# Load the image
image_path = "grid_image.png"
image = Image.open(image_path)

# Create a blank canvas for the 3x3 grid
canvas_width, canvas_height = image.width * 3, image.height * 3
canvas = Image.new("RGBA", (canvas_width, canvas_height), (255, 255, 255, 0))

# Paste the image 9 times in a 3x3 grid
for i in range(3):
    for j in range(3):
        canvas.paste(image, (i * image.width, j * image.height))

# Save the resulting image
canvas.save("grid_image.png")

print("The 3x3 grid image has been saved as 3x3_grid_image.png")