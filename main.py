# wiki url https://en.wikipedia.org/wiki/NAME_OF_SEARCH

from bs4 import BeautifulSoup
import requests
import datetime
import os
import re


def steal():
    print("Enter wikipedia item to get all images from: ")
    myInput = input()
    try:
        html_page = requests.get(f"https://en.wikipedia.org/wiki/{myInput}")
    except:
        print("Could not find page")
        steal()
    soup = BeautifulSoup(html_page.text, features="html.parser")

    # ? makedir for the page folder
    path = f"{os.path.abspath(os.curdir)}\{myInput}"
    os.makedirs(path, exist_ok=True)

    i = 0
    for img in soup.findAll('img'):

        # ? makedir to every images in page (the name if the time)
        dir_name = str(datetime.datetime.now()).replace(
            " ", "_").replace(":", "_")

        # ? Create dir
        os.makedirs(f"{path}\{dir_name}")

        # ? Find original name
        print(img.get('src')[2:])

        filename = img.get('src')[2:].split("/")[-1]
        try:
            # ? Get image
            image = requests.get("http://" + img.get('src')[2:]).content
            try:
                # ? Possibility of decode
                image = str(image, "utf-8")
            except:
                print("download image")
                # ? Download image
                with open(f"{path}\{dir_name}\{filename}", "wb+") as f:
                    f.write(image)
        except:
            print("error")
            pass


steal()


#! MAKE DIR = os.makedirs(f"{os.path.abspath(os.curdir)}/{NAME}", exist_ok=True)
