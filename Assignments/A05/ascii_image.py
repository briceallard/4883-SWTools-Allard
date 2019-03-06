"""
Course: CMPS 4883
Assignemt: A05
Date: 03/05/2019
Github username: briceallard
Repo url: https://github.com/briceallard/4883-SWTools-Allard
Name: Brice Allard
Description: 
    Converts an image (.png, .jpg, .bmp, .jpeg) to Ascii Art
"""

import os
import sys
import getopt
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ascii_chars = [u'P', '4', 'H', 'a', 'a', 't', 'f', 'M', 'N', '>', 'O']
input_file = 'defaultInput.jpg'
output_file = 'defaultOutput.png'
font_file = 'defaultFont.ttf'
font_size = 12


def get_CWD():
    """
    # get_CWD -
    #   Finds the current working directory
    #
    # Params:
    #   None
    # Returns:
    #   string: cwd
    """
    return os.path.dirname(os.path.abspath(__file__))


def img_to_ascii_console(**kwargs):
    """
    # img_to_ascii_console -
    #   Converts a given image to ascii and prints it to screen using IO
    #
    # Params:
    #   None
    # Returns:
    #   string: cwd
    """
    pass


def handle_args(argv):
    """
    # handle_args -
    #   Gets user arguments from command line and associates with:
    #       - input_file
    #       - output_file
    #       - font_file
    #       - font_size
    #
    # Params:
    #   argv: the arguments being passed in from command line
    # Returns:
    #   None
    """

    # Get user arguments
    # --i, --input: the location/name of input file to convert
    # --o, --output: the location/name of output file once converted
    # --f, --font: the location/name of the font (.ttf) file to use
    # --s, --size: the font size used when writing the file
    try:
        opts, args = getopt.getopt(
            argv, 'i:o:f:s:', ['input=', 'output=', 'font=', 'size='])

        for opt, arg in opts:
            if opt in ('-i', '--input'):
                print("Setting --input = %s" % arg)
                input_file = arg
            elif opt in ('-o', '--output'):
                print("Setting --output = %s" % arg)
                output_file = arg
            elif opt in ('-f', '--font'):
                print("Setting --font = %s" % arg)
                font_file = arg
            elif opt in ('-s', '--size'):
                print("Setting --size = %d" % int(arg))
                font_size = int(arg)
    except getopt.GetoptError:
        print("Whoops, something went wrong!")


if __name__ == '__main__':

    # Get user arguments for conversion files
    if len(sys.argv) == 5:
        handle_args(sys.argv[1:])
    # otherwise default values used
    else:
        print("Setting --input = %s" % input_file)
        print("Setting --output = %s" % output_file)
        print("Setting --font = %s" % font_file)
        print("Setting --size = %d" % font_size)
