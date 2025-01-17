from PIL import Image

"""
This script takes an image and creates a 3x3 grid of that image.
It can be used to duplicate a picture of tools or items into a larger grid.
"""

def create_image_grid(image_path, output_path, grid_size=(3, 3)):
    try:
        # Load the image
        image = Image.open(image_path)

        # Create a blank canvas for the grid
        canvas_width, canvas_height = image.width * grid_size[0], image.height * grid_size[1]
        canvas = Image.new("RGBA", (canvas_width, canvas_height), (255, 255, 255, 0))

        # Paste the image in a grid pattern
        for i in range(grid_size[0]):
            for j in range(grid_size[1]):
                canvas.paste(image, (i * image.width, j * image.height))

        # Save the resulting image
        canvas.save(output_path)
        print(f"The {grid_size[0]}x{grid_size[1]} grid image has been saved as {output_path}")

    except FileNotFoundError:
        print(f"Error: The file {image_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Define the image path and output path
image_path = "grid_image.png"
output_path = "3x3_grid_image.png"

# Create a 3x3 grid of the image
create_image_grid(image_path, output_path)
