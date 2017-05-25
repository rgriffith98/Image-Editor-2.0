from PIL import Image
from PIL import ImageFilter

#####

def bw(img):
    gray = img.convert("L")
    gray.show()

###

def bl(img):
    blurred = img.filter(ImageFilter.BLUR)
    blurred.show()

###

def dt(img):
    det = img.filter(ImageFilter.DETAIL)
    det.show()

def ed(img):
    edges = img.filter(ImageFilter.FIND_EDGES)
    edges.show()