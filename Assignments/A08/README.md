## Image Mosaic
#### Purpose
This program has 2 functionallities.  
- First: Given a YouTube video ID, downloads the highest quality and frame rate available to the desired directory, then takes a screen capture of the current frame at the given interval (default: 1 second)
- Second: Using the dataset of images collected from screen capturing (or any other large dataset of images) we import an image using PIL and replace each pixel with the most "SIMILIAR" image from the dataset creating a Image Mosaic.

#### Description
In the example, I used the trailers to every Marvel Avengers movie for my dataset of images and the upcoming release poster for Avengers: Endgame as my Image Mosaic backdrop image. Each pixel is replaced with an image from one of the Avengers trailers, creating a Avengers mosaic of Avengers ;)

**Files**
* /emojis/
    * a folder holding all the available images for comparison
* output.png
    * the image found to be the most similar to your comparison image
* match.py 
    * finds the most similar in resomblance image to the image passed in by user

## Instructions
**Requirements**
* FFmpeg - A complete, cross-platform solution to record, convert and stream audio and video.
    * Install with `sudo apt install ffmpeg`  
* Pillow - Python imaging library that adds support for opening, manipulating, and saving many different image file formats.  
    * Install with `pip3 install Pillow`

**Example**  
`python3 match.py folder=emojis/ image=winkydinky.jpg` to execute program with default settings  

## Output
