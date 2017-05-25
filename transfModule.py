from PIL import Image

#####

def menu(img):
    print("Make another selection from the list below:")
    choice = input("1. square picture\n2. flip top to bottom\n3. flip left to right\n4. rotate\n")

    if choice is '1':
        sq(img)
    elif choice is '2':
        flipUp(img)
    elif choice is '3':
        flipSide(img)
    elif choice is '4':
        spin(img)
    else:
        print("Invalid input. Program terminated.")

###

def sq(img):
    square_img = img.resize((250, 250))
    square_img.show()

###

def flipUp(img):
    flip_pic = img.transpose(Image.FLIP_TOP_BOTTOM)
    flip_pic.show()

###

def flipSide(img):
    flip_pic = img.transpose(Image.FLIP_LEFT_RIGHT)
    flip_pic.show()

###

def spin(img):
    rot_pic = img.transpose(Image.ROTATE_90)
    rot_pic.show()