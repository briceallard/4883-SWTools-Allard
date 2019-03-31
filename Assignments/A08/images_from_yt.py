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
import ffmpy
from pytube import YouTube

VIDEO_ID = ''
SAVE_PATH = ''
TITLE = ''
SS_INTERVAL = 0


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
    """
    Name:
        download_video
    Description:
        Given a YouTube video ID, downloads the video in the 
        highest quality and in .mp4 format
    Params:
        None
    Returns:
        None
    """
    global VIDEO_ID
    global SAVE_PATH
    global TITLE

    try:
        print('Attemping connection to: https://www.youtube.com/watch?v=' + VIDEO_ID)
        yt = YouTube('https://www.youtube.com/watch?v=' + VIDEO_ID)
    except:
        print("Connection Error!")

    TITLE = ''.join(e for e in yt.title if e.isalnum())

    print('Downloading: ' + TITLE)
    yt.streams.first().download(output_path=SAVE_PATH, filename=TITLE)

    ## Screen shot frame by frame every i (Interval)
    ss_frames()


def ss_frames():
    """
    Name:
        ss_frames
    Description:
        Given a video, captures a screen shot of a frame each second
        and stores it as .jpg format
    Params:
        None
    Returns:
        None
    """
    global SAVE_PATH
    global SS_INTERVAL
    global TITLE

    save_format = './frame_captures/' + TITLE + '%03' + 'd'

    print('Capturing frames ...')
    os.system('ffmpeg -i {0} -vf fps={1} {2}.jpg'
              .format(SAVE_PATH + TITLE + '.mp4',
                      str(SS_INTERVAL),
                      save_format))


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

    print("python3 images_from_yt.py [options] [--id | --dir | --seconds\n")
    print("--id [-i]\t: URL to YouTube Video to download.")
    print("--dir [-d]\t: PATH to save the video")
    print("--sec [-s]\t: Interval between screenshot capture")
    print("Ex: python3 images_from_yt.py --id=eOrNdBpGMv8 --dir=/output_folder/ --second=5")
    print("Ex: python3 images_from_yt.py -i eOrNdBpGMv8 -d /output_folder/ -s 5\n")


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

    global VIDEO_ID
    global SAVE_PATH
    global SS_INTERVAL

    # Get user arguments
    # --i, --input: the YouTube URL of the video to download
    # --o, --output: The PATH to save the video
    # --s, --seconds: Interval between screenshot capture
    if not argv:
        usage()
        sys.exit(2)
    # otherwise default values used
    else:
        try:
            opts, args = getopt.getopt(
                argv, 'i:d:s:', ['id=', 'dir=', 'seconds='])

            for opt, arg in opts:
                if opt in ('-i', '--id'):
                    print("Setting --id = %s" % arg)
                    VIDEO_ID = arg
                elif opt in ('-d', '--dir'):
                    print("Setting --dir = %s" % arg)
                    SAVE_PATH = get_CWD() + arg
                elif opt in ('-s', '--sec'):
                    print("Setting --sec = %s" % arg)
                    SS_INTERVAL = arg
        except getopt.GetoptError:
            usage()
            sys.exit(2)


if __name__ == '__main__':
    # Get arguments from terminal and assign them
    handle_args(sys.argv[1:])

    download_video()
