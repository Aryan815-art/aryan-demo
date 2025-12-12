from PIL import Image

img = Image.new("RGB", (300, 300), (255, 0, 0))  # Red
img.save("red.png")
img.show()
