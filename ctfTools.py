import PIL
from PIL import Image


def www():
    print("hello world")


def metaDataGrabber():
    fileInput = input("enter the absolute path to the file")
    filename = fileInput
    im = Image.open(filename)
    im.load()  # Needed only for .png EXIF data (see citation above)
    print(im.info['meta_to_read'])

def osint():
    print("it works")