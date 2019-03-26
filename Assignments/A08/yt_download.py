import os
import sys
import getopt
from pytube import YouTube

DOWNLOAD_URL = ''
SAVE_PATH = ''


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


def download_video():
    global DOWNLOAD_URL

    try:
        yt = YouTube(DOWNLOAD_URL)
    except:
        print("Connection Error!")


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

    print("python3 yt_download.py [options] [--input | --output\n")
    print("--input [-i]\t: URL to YouTube Video to download.")
    print("--output [-o]\t: PATH to save the video")
    print("Ex: python3 yt_download.py --input=https://www.youtube.com/watch?v=eOrNdBpGMv8 --output=/output_folder/")
    print("Ex: python3 yt_download.py -i https://www.youtube.com/watch?v=eOrNdBpGMv8 -o /output_folder/\n")


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

    global DOWNLOAD_URL
    global SAVE_PATH

    # Get user arguments
    # --i, --input: the YouTube URL of the video to download
    # --o, --output: The PATH to save the video
    if not argv:
        usage()
        sys.exit(2)
    # otherwise default values used
    else:
        try:
            opts, args = getopt.getopt(argv, 'i:o:', ['input=', 'output='])

            for opt, arg in opts:
                if opt in ('-i', '--input'):
                    print("Setting --input = %s" % arg)
                    DOWNLOAD_URL = arg
                elif opt in ('-o', '--output'):
                    print("Setting --output = %s" % arg)
                    SAVE_PATH = get_CWD() + arg
        except getopt.GetoptError:
            usage()
            sys.exit(2)


if __name__ == '__main__':
    # Get arguments from terminal and assign them
    handle_args(sys.argv[1:])

    print(DOWNLOAD_URL)
    print(SAVE_PATH)
