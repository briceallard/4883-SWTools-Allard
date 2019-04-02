"""
Course: CMPS 4883
Assignemt: A08
Date: 03/26/2019
Github username: briceallard
Repo url: https://github.com/briceallard/4883-SWTools-Allard
Name: Brice Allard
Description: 
    Using an image dataset, create an image mosaic (image made of other images)
"""

import cv2
import os
import sys
import json
import string
import getopt
import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint
from sklearn.cluster import KMeans
from PIL import Image, ImageDraw, ImageMath


INPUT_PATH = ''
OUTPUT_PATH = ''
DATASET_FILE = '/dominant_data/avengers/avengers.json'
ENLARGEMENT = 20


def resize(img, width):
    """
    Name:
        resize
    Description:
        Resizes the image to passed in width value while maintaining aspect ratio
    Params:
        img - the image being resized
        width - designated width (height will be resized to keep aspect ratio)
    Returns:
        img
    """

    wpercent = float(width / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((width, hsize), Image.ANTIALIAS)

    return img


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


def usage():
    """
    Name:
        usage
    Description:
        Displays instructional data for user
    Params:
        None
    Returns:
        None
    """

    print("python3 images_from_yt.py [options] [--i | --o\n")
    print("--id [-i]\t: PATH of input file used for conversion")
    print("--dir [-d]\t: PATH to save the video")
    print("Ex: python3 images_from_yt.py --i=/input_folder/ --o=/output_folder/")
    print("Ex: python3 images_from_yt.py -i /input_folder/ -o /output_folder/\n")


def handle_args(argv):
    """
    Name:
        handle_args
    Description:
        Gets user arguments from command line and associates with:
            - DOWNLOAD_URL
            - SAVE_PATH
    Params:
        argv: the arguments being passed in from command line
    Returns:
        None
    """

    global INPUT_PATH
    global OUTPUT_PATH

    # Get user arguments
    # --i, --input: the image path used for conversion
    # --o, --output: The PATH to save the video
    if not argv:
        usage()
        sys.exit(2)
    # otherwise default values used
    else:
        try:
            opts, args = getopt.getopt(
                argv, 'i:o:', ['in=', 'out='])

            for opt, arg in opts:
                if opt in ('-i', '--in'):
                    print("Setting --in = %s" % arg)
                    INPUT_PATH = arg
                elif opt in ('-o', '--out'):
                    print("Setting --out = %s" % arg)
                    OUTPUT_PATH = get_CWD() + arg
        except getopt.GetoptError:
            usage()
            sys.exit(2)


def process_input_file(img):

    print('Processing Input Image ...')
    image = Image.open(img)

    w, h = image.size

    rgb_list = list(image.convert('RGB').getdata())

    new_image = Image.new(
        'RGB', (w * ENLARGEMENT, h * ENLARGEMENT), (255, 255, 255))

    for y in range(w):
        for x in range(h):
            pixel = find_closest_image(image.getpixel((x, y)))
            paste_image = Image.open('./frame_captures/' + pixel, 'r')
            paste_image = resize(paste_image, 20)
            new_image.paste(paste_image, (x, y))
            
            print('.', end='', flush=True)

    new_image.save('mosaic.jpg')


def process_pixel(color):
    rgb_a = np.asarray(color)
    find_closest_image(rgb_a)


def find_closest_image(color):
    a = np.asarray(color)
    distance = sys.maxsize
    closest_image = ''

    with open(get_CWD() + DATASET_FILE, 'r') as f:
        data = json.load(f)

    for filename in data:
        b = np.asarray(data[filename])

        dist = np.linalg.norm(a-b)

        if(dist < distance):
            distance = dist
            closest_image = filename

    return closest_image


if __name__ == '__main__':
    # Get arguments from terminal and assign them
    handle_args(sys.argv[1:])

    process_input_file(INPUT_PATH)
