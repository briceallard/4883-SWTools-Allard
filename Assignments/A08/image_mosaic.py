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

import os
import sys
import string
import getopt
import PIL


INPUT_PATH = ''
OUTPUT_PATH = ''


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


if __name__ == '__main__':
    # Get arguments from terminal and assign them
    handle_args(sys.argv[1:])
