from PIL import Image

# pip install pillow

img = Image.open("A.png")
blackAndWhite = img.convert("L")
blackAndWhite.save("Br.png")
blackAndWhite.show()