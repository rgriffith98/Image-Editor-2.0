from PIL import Image
from imageEditor import pillowModule
from imageEditor import transfModule
from imageEditor import modefilt
from PIL import ImageFilter

#####

choice = input("Input the name of the image you want to work with...\n")
img = Image.open(choice)

print("SIZE:", img.size)
print("FORMAT:", img.format, "\n")
img.show()

###
print("0. crop an image\n1. combine images\n2. Mess with colors\n3. transform\n4. grayscale\n5. blur\n6. detail\n7. magic pen\n")
func = input("Choose from the menu options above...(enter the corresponding number)\n")

if func is '0':
    pillowModule.cropDat(img)
elif func is '1':
    pillowModule.combineDat(img)
elif func is '2':
    pillowModule.getChan(img)
elif func is '3':
    transfModule.menu(img)
elif func is '4':
    modefilt.bw(img)
elif func is '5':
    modefilt.bl(img)
elif func is '6':
    modefilt.dt(img)
elif func is '7':
    modefilt.ed(img)
else:
    print("Invalid input. Program exited.")
###

print("PROCESS COMPLETE")
