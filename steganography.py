from PIL import Image

# Function to convert text to binary
def text_to_binary(text):
binary = ' '.join(format(ord(char), '08b') for char in text)
return binary

# Function to hide text in an image using LSB
def hide_text(image_path, output_path, text):
# Open the image
img = Image.open(image_path)

# Convert text to binary
binary_text = text_to_binary(text)
binary_text += '1111111111111110' # Add a termination sequence

# Check if image can hold the text
if len(binary_text) > img.size[0] * img.size[1]:
raise ValueError("Text too long to be hidden in the image.")

# Convert the image to RGB (if not already in RGB mode)
img = img.convert('RGB')
pixels = img.load()

# Counter for binary text
text_index = 0

# Traverse through each pixel
for i in range(img.size[0]):
for j in range(img.size[1]):
r, g, b = pixels[i, j]

# Hide binary text in LSB of RGB values
r = (r & ~1) | int(binary_text[text_index])
text_index += 1

if text_index < len(binary_text):
g = (g & ~1) | int(binary_text[text_index])
text_index += 1

if text_index < len(binary_text):
b = (b & ~1) | int(binary_text[text_index])
text_index += 1

# Update pixel with modified RGB values
pixels[i, j] = (r, g, b)

# Break loop if all text is hidden
if text_index >= len(binary_text):
break
if text_index >= len(binary_text):
break

# Save the modified image with hidden text
img.save(output_path)

# Example usage
image_path = 'input_image.jpg'
output_path = 'output_image.png'
text_to_hide = "This is a secret message!"

hide_text(image_path, output_path, text_to_hide)
print(f"Text hidden successfully in {output_path}")