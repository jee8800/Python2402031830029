
from PIL import Image, ImageFilter

# Load image
image = Image.open("sample.jpg")

# Apply grayscale filter
gray_image = image.convert("L")
gray_image.save("output_grayscale.jpg")

# Rotate the image
rotated_image = image.rotate(45)  # Rotate by 45 degrees
rotated_image.save("output_rotated.jpg")

# Resize the image
resized_image = image.resize((300, 300))
resized_image.save("output_resized.jpg")

# Apply blur
blurred_image = image.filter(ImageFilter.BLUR)
blurred_image.save("output_blurred.jpg")

print("All image edits are done and saved!")
