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

# Change these based on the font you use
ascii_chars = [u'P', '4', 'H', 'a', 'a', 't', 'f', 'M', 'N', '>', 'O']

# Default settings
default_ascii_chars = [ u'#', 'A', '@', '%', 'S', '+', '<', '*', ':', ',', '.']

# Default Input Settings
input_dir = '/input_images/'
input_file = 'vans-logo.png'

# Default Output Settings
output_dir = '/output_images/'
output_file = input_file + '.txt'

# Default Font settings
font_dir = '/fonts/'
font_file = 'defaultFont.ttf'
font_size = 12

# Use default settings
default = False


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


def img_to_ascii_console(**kwargs):
    """
    Name:
        img_to_ascii_console
    Description:
        Converts a given image to ascii and prints it to screen using IO
    Params:
        None
    Returns:
        None
    """
    
    width = kwargs.get('width', 200)
    cwd = get_CWD()

    im = Image.open(cwd + input_dir + input_file)
    im = resize(im, width)

    rgb_list = list(im.convert('RGB').getdata())

    i = 0
    for val in rgb_list:
        r, g, b = (rgb_list[i][0], rgb_list[i][1], rgb_list[i][2])
        
        print(default)
        sys.exit()

        if default == True:
            ch = default_ascii_chars[int((r + b + g) / 3) // 25]
        elif default == False:
            ch = ascii_chars[int((r + b + g) / 3) // 25]
        sys.stdout.write(ch)
        i += 1
        if i % width == 0:
            sys.stdout.write('\n')


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

    print("python3 ascii_image.py [options] [--defulat | --input | --output | --font | --size]\n")
    print("--default [-d]\t: Execute program using default values preassigned by Owner")
    print("--input [-i]\t: Filename including path to the image you want to convert")
    print("--output [-o]\t: Location and filename you would like to save the file")
    print("--font [-f]\t: Location and filename to the font file. (Must be .ttf)")
    print("--size [-s]\t: Size of font you would like to use. (Must be integer)\n")
    print("Ex: python3 ascii_image.py --input=inputFileName.jpg --output=outputFileName.png --font=fontFamily.ttf --size=12")
    print("Ex: python3 ascii_image.py -i inputFileName.jpg -o outputFileName.png -f fontFamily.ttf -s 12")


def use_default():
    """
    Name:
        use_default
    Description:
        Displays default setting values to console
    Params:
        None
    Returns:
        None
    """

    print("Setting --input = %s" % input_file)
    print("Setting --output = %s" % output_file)
    print("Setting --font = %s" % font_file)
    print("Setting --size = %d" % font_size)
    default = True


def handle_args(argv):
    """
    Name:
        handle_args
    Description:
        Gets user arguments from command line and associates with:
            - input_file
            - output_file
            - font_file
            - font_size
    Params:
        argv: the arguments being passed in from command line
    Returns:
        None
    """

    # Get user arguments
    # --i, --input: the location/name of input file to convert
    # --o, --output: the location/name of output file once converted
    # --f, --font: the location/name of the font (.ttf) file to use
    # --s, --size: the font size used when writing the file
    
    if not argv:
        usage()
        sys.exit(2)
    elif len(argv) == 1:
        if argv == '-d' or argv == '--default':
            print("Setting --default = TRUE")
            use_default()
    # otherwise default values used
    else:
        try:
            opts, args = getopt.getopt(argv, 'di:o:f:s:', ['default', 'input=', 'output=', 'font=', 'size='])

            for opt, arg in opts:
                if opt in ('-d', '--default'):
                    print("Setting --default = TRUE")
                    use_default()
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
            usage()
            sys.exit(2)


if __name__ == '__main__':

    handle_args(sys.argv[1:])
    img_to_ascii_console()

