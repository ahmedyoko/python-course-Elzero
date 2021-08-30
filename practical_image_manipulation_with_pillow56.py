#..............................................
# practical_image_manipulation_with_pillow
#..............................................
from PIL import Image

# print(dir(PIL))
# open the image 
myimage = Image.open(r'D:\css-revision\image\intricate-explorer-h7L-SRej-sw-unsplash.jpg')

# show image
myimage.show()

# mycropped image
mybox = (100,100,400,400) # size of cropping
myNewImage = myimage.crop(mybox)

# show the new image
myNewImage.show()

# my converted mode image
myconverted = myimage.convert("L")
myconverted.show()