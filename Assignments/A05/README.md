## Image to Ascii Art
#### Purpose
Takes an image and depicts the contents of each pixel finding the RGBA value. Based on this value we find a similiar character and display it in the pixels place. This converts the image to an Ascii format, resembling the original, but using only characters instead of colors.

**Files**
* /input_images/
    * a folder holding all the available images for conversion to ascii
* /output_images/
    * a folder storing all the images that have been converted to ascii
* /fonts/
    * a folder containing the available fonts you can choose from
* ascii_image.py 
    * converts the image given in the command line to a form of ascii art using a custom font

## Instructions
**Help**
`python3 ascii_image.py -h` to display all available options  

**Default**
`python3 ascii_image.py -d` to run with default parameters 

**Custom**
* Make sure you store any custom images you want in `./input_images/`
* Make sure you store any custom fonts you want in `./fonts/`
* Default values:
    * `input_file = 'lambo.jpg'`
    * `output_file = input_file`
    * `font_file = 'OpenSans-Regular.ttf'`
    * `font_size = 12`  

##### Execute commands:
`python3 ascii_image.py --input=inputFileName.jpg --output=outputFileName.png --font=fontFamily.ttf --size=12`  
or  
`python3 ascii_image.py -i inputFileName.jpg -o outputFileName.png -f fontFamily.ttf -s 12`

## Result
##### Input File
![Input File](/examples/input_file/lambo_input.jpg?raw=true "Input File")
##### Output File
<img src="https://www.briceallard.com/images/lambo_output.jpg" width=400 title="Output File">
