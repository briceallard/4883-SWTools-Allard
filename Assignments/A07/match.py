"""
Course: CMPS 4883
Assignemt: A07
Date: 03/20/2019
Github username: briceallard
Repo url: https://github.com/briceallard/4883-SWTools-Allard
Name: Brice Allard
Description: 
    Loops through images in a folder and finds the closest match
    to the test image using a MSE formula for comparative differences
"""

from skimage.measure import compare_ssim as ssim
from PIL import Image, ImageMath
import matplotlib.pyplot as plt
import numpy as np
import cv2
import sys
import os


def mse(imageA, imageB):
    """
    Name:
        mse
    Description:
        the 'Mean Squared Error' between the two images is the
        sum of the squared difference between the two images.
        NOTE: the two images must have the same dimension
    Params:
        imageA, imageB - the images to be compared
    Returns:
        err - the % of error in MSE
    """

    imgA = Image.open(imageA)
    imgB = Image.open(imageB)

    err = np.sum(ImageMath.eval(
        "(convert(imgA, 'F') - convert(imgB, 'F'))**2", imgA=imgA, imgB=imgB))
    err /= float(imgA.size[0] * imgA.size[1])

    # return the MSE, the lower the error, the more "similar"
    # the two images are
    return err


def compare_images(imageA, imageB, title):
    """
    Name:
        compare_images
    Description:
        compute the mean squared error and structural similarity
    Params:
        imageA, imageB, title - the images to be compared
    Returns:
        none
    """

    # index for the images
    m = mse(imageA, imageB)
    s = ssim(imageA, imageB)

    # setup the figure
    fig = plt.figure(title)
    plt.suptitle("MSE: %.2f, SSIM: %.2f" % (m, s))

    # show first image
    ax = fig.add_subplot(1, 2, 1)
    plt.imshow(imageA, cmap=plt.gray())
    plt.axis("off")

    # show the second image
    ax = fig.add_subplot(1, 2, 2)
    plt.imshow(imageB, cmap=plt.gray())
    plt.axis("off")

    # show the images
    plt.show()


def get_CWD():
    """
    Name:
        get_CWD
    Description:
        Finds the current working directory
    Params:
        None
    Returns:
        cwd
    """

    return os.path.dirname(os.path.abspath(__file__))


def verify_input(folder, image):
    """
    Name:
        verify_input
    Description:
        Determines whether the file and folders are valid
    Params:
        folder - the directory location given by user
        image - the image location and name given by user
    Returns:
        bool
    """

    if(os.path.isfile(image)):
        if(os.path.isdir(folder)):
            return True
    else:
        return False


if __name__ == '__main__':

    args = {}

    # loops throug arguments to get folder and image paths
    for arg in sys.argv[1:]:
        k, v = arg.split('=')
        args[k] = v

    folder = get_CWD() + '/' + args['folder']
    compare_image = get_CWD() + '/' + args['image']
    mserror = sys.maxsize
    lowest_image = ''

    if(verify_input(folder, compare_image)):
        for images in os.listdir(folder):
            image = folder + images

            error = mse(compare_image, image)

            if(error < mserror):
                mserror = error
                lowest_image = image
    else:
        print('Check your directory and file inputs and try again.')

    print(lowest_image)
    print(mserror)

    # Display the most similiar image
    im = Image.open(lowest_image)
    im.show()
    im.save(get_CWD() + '/output.png')