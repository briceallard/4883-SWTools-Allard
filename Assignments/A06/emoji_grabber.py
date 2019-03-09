"""
Course: CMPS 4883
Assignemt: A06
Date: 03/05/2019
Github username: briceallard
Repo url: https://github.com/briceallard/4883-SWTools-Allard
Name: Brice Allard
Description: 
    Scrape https://www.webfx.com/tools/emoji-cheat-sheet/ for all available emojis
    and then compresses the folder contents into a .zip file located in the root directory
"""

import os
import sys
import urllib.request
import requests
import zipfile
from beautifulscraper import BeautifulScraper
from time import sleep
from pprint import pprint


def zip_folder(output_path, output_file):
    """
    Name:
        zip_folder
    Description:
        Compresses the path directory in a .zip format
    Params:
        output_path - the directory to store the compressed file
        output_file - the zipfile being wrote too
    Returns:
        None
    """
    zip_file = zipfile.ZipFile(output_file, 'w', zipfile.ZIP_DEFLATED)

    for root, dirs, files in os.walk(output_path):
        for file in files:
            zip_file.write(os.path.join(root, file))

    zip_file.close()


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


def get_file_name(image_path):
    """
    Name:
        get_file_name
    Description:
        Splits the string and gives us the filename
    Params:
        image_path
    Returns:
        file_name
    """
    try:
        return image_path.split('/')[2]
    except:
        print('Invalid image path format!')


def get_emojis(url, output_path):
    """
    Name:
        get_emojis
    Description:
        Navigates to the url and scrapes the page for all emojis
    Params:
        url - the url hosting all the emoji images
        output_path - the location to save each emoji image
    Returns:
        None
    """

    # Load scraper data
    bs = BeautifulScraper()
    soup = bs.go(url)
    emojis = soup.find_all("span", {"class": "emoji"})

    # To calculate completion %
    total = len(emojis)
    count = 1

    for emoji in emojis:
        # Get each images data
        image_path = emoji['data-src']
        file_name = get_file_name(image_path)

        # Check image url for validity
        r = requests.get(url + image_path, allow_redirects=True)

        # If valid
        if r.status_code == 200:
            with open(output_path + file_name, 'wb') as f:
                for chunk in r:
                    f.write(chunk)
            print('{0}/{1}: Success  \t{2:.2f}%'
                  .format(count, len(emojis), (count / total) * 100))
        # If invalid
        else:
            print('{0}/{1}: Failure  \t{2:.2f}%'
                  .format(count, len(emojis), (count / total) * 100))

        count += 1
        sleep(0.02)


if __name__ == "__main__":
    # URL to scrape
    url = 'https://www.webfx.com/tools/emoji-cheat-sheet/'

    # Save location
    output_path = get_CWD() + '/emojis/'

    # Get all emojies from the URL
    get_emojis(url, output_path)

    # Zip the contents of the '/emojis/' folder
    zip_folder('emojis/', 'Emojis.zip')
