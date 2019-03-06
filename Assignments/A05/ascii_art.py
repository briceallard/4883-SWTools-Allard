import os
import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ascii_chars = [u'P', '4', 'H', 'a', 'a', 't', 'f', 'M', 'N', '>', 'O']

image_in_path = os.path.dirname(os.path.abspath(__file__)) + '/input_images/'
image_out_path = os.path.dirname(os.path.abspath(__file__)) + '/output_images/'


def img_to_ascii_console(**kwargs):
    """
    The ascii character set we use to replace pixels.
    The grayscale pixel values are 0-255.
    0 - 25 = '#' (darkest character)
    250-255 = '.' (lightest character)
    """

    width = kwargs.get('width', 200)
    filename = kwargs.get('filename', None)

    im = Image.open(image_in_path + filename)

    im = resize(im, width)

    w, h = im.size

    print(w, h)

    rgb_im = im.convert('RGB')
    rgb_list = list(rgb_im.getdata())

    i = 0
    for val in rgb_list:
        r, g, b = (rgb_list[i][0], rgb_list[i][1], rgb_list[i][2])
        val = int((r + b + g) / 3)
        ch = ascii_chars[val // 25]
        sys.stdout.write(ch)
        i += 1
        if i % width == 0:
            sys.stdout.write("\n")

    return im


def img_to_ascii_file(**kwargs):
    """
    The ascii character set we use to replace pixels.
    The grayscale pixel values are 0-255.
    0 - 25 = '#' (darkest character)
    250-255 = '.' (lightest character)
    """

    width = kwargs.get('width', 200)
    filename = kwargs.get('filename', None)

    im = Image.open(image_in_path + filename)

    im = resize(im, width)

    w, h = im.size

    print(w, h)

    rgb_im = im.convert('RGB')
    rgb_list = list(rgb_im.getdata())

    if not os.path.exists(image_out_path):
        os.makedirs(image_out_path)

    f = open(image_in_path + filename + '.txt', 'w+')

    i = 0
    for val in rgb_list:
        r, g, b = (rgb_list[i][0], rgb_list[i][1], rgb_list[i][2])
        val = int((r + b + g) / 3)
        ch = ascii_chars[val // 25]
        f.write(ch)
        i += 1
        if i % width == 0:
            f.write("\n")

    f.close()
    return im


def ascii_to_img(**kwargs):
    filename = kwargs.get('filename', None)

    im = Image.open(image_in_path + filename)

    w, h = im.size

    # Open a new image using 'RGBA' (a colored image with alpha channel for transparency)
    #              color_type      (w,h)     (r,g,b,a)
    #                   \           /            /
    #                    \         /            /
    newImg = Image.new('RGBA', im.size, (255, 255, 255, 255))

    # Open a TTF file and specify the font size
    fnt = ImageFont.truetype('Militaria.ttf', 12)

    # get a drawing context for your new image
    drawOnMe = ImageDraw.Draw(newImg)

    # You would loop through your old image and write on the newImg with the
    # lines of code below:
    rgb_im = im.convert('RGB')
    rgb_im.load()

    for x in [w - 1]:
        for y in [h - 1]:
            r, g, b = rgb_im.getpixel((x,y))
            val = int((r + b + g) / 3)
            ch = ascii_chars[val // 25]
            drawOnMe.text((x, y), ch, font=fnt, fill=(r, g, b))

    # Display your new image with all the stuff `drawOnMe` placed on it
    newImg.show()

    # Save the image.
    newImg.save(image_out_path + filename)


def resize(img, width):
    """
    This resizes the img while maintining aspect ratio. Keep in 
    mind that not all images scale to ascii perfectly because of the
    large discrepancy between line height line width (characters are 
    closer together horizontally then vertically)
    """

    wpercent = float(width / float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((width, hsize), Image.ANTIALIAS)

    return img


if __name__ == '__main__':
    filename = 'vans-logo.png'
    img_to_ascii_console(filename=filename, width=150)
    img_to_ascii_file(filename=filename, width=150)
    ascii_to_img(filename=filename)
