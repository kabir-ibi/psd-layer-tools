from PIL import Image

# Load your images
musk_image = Image.open("path/to/musk.jpg")  # Replace with your musk image path
real_image = Image.open("path/to/real.jpg")  # Replace with your real image path

# Assuming you want to overlay the 'musk_image' over the 'real_image' 
# Resize if necessary
if musk_image.size != real_image.size:
    musk_image = musk_image.resize(real_image.size)

# Create a new image to serve as the base 
new_image = Image.new('RGB', real_image.size) 

# Paste the 'real_image' as the background layer
new_image.paste(real_image, (0, 0))

# Paste the 'musk_image', potentially with transparency
new_image.paste(musk_image, (0, 0), mask=musk_image)

# Save the composite image as a PSD file
new_image.save("output_image.psd")
