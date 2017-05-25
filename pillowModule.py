from PIL import Image

#####

def cropDat(img):
    print("Input the dimensions of your desired cropped image.")
    print("Seperate them by 'enter' keys")

    x1 = int(input("Starting x coordinate: "))
    y1 = int(input("Starting y coordinate: "))
    x2 = int(input("Ending x coordinate: "))
    y2 = int(input("Ending y coordinate: "))

    area = (x1, y1, x2, y2)

    cropped_img = img.crop(area)
    cropped_img.show()

###

def combineDat(img):
    choice = input("What is the second image you would like to work with?\n")

    img2 = Image.open(choice)

    print("SIZE:", img2.size)
    print("FORMAT:", img2.format, "\n")
    img2.show()

    print("Input the exact dimensions of the second image in reference to the first image.")
    x1 = int(input("Starting x coordinate: "))
    y1 = int(input("Starting y coordinate: "))
    x2 = int(input("Ending x coordinate: "))
    y2 = int(input("Ending y coordinate: "))

    where = (x1, y1, x2, y2)
    img.paste(img2, where)

    img.show()

###

def getChan(img):
    print(img.mode)
    r, g, b = img.split()

    c_img = Image.merge("RGB", (r, b, g))
    c_img.show()

    c_img = Image.merge("RGB", (g, b, r))
    c_img.show()

    c_img = Image.merge("RGB", (g, r, b))
    c_img.show()

    c_img = Image.merge("RGB", (b, r, g))
    c_img.show()

    c_img = Image.merge("RGB", (b, g, r))
    c_img.show()

    c_img = Image.merge("RGB", (b, r, g))
    c_img.show()