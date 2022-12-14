import os
import imageio

imageList = sorted(os.listdir("Assignment_08/Images"))

IMAGES = []

for imageName in imageList:
    imagePath = "Assignment_08/Images/" + imageName
    image = imageio.imread(imagePath)
    IMAGES.append(image)

imageio.mimsave("Assignment_08/MyGIF.gif", IMAGES)