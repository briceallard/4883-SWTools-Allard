## Image Compare - Mean Square Error
#### Purpose
Takes and image and using the Mean Square Error formula finds the most similar image from within a folder.

**Files**
* /emojis/
    * a folder holding all the available images for comparison
* output.png
    * the image found to be the most similar to your comparison image
* match.py 
    * finds the most similar in resomblance image to the image passed in by user

## Instructions
**Example**  
`python3 match.py folder=emojis/ image=winkydinky.jpg` to execute program with default settings  

**Note**
Comparison images are in the emojis/ directory by default  
Closest comparison will be saved as `output.png` in the root directory