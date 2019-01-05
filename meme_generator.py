import requests
from bs4 import BeautifulSoup
import os
import random
import datetime
from pathlib import Path
import time

header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'}


# call first 20 pages
def call_urls():
    index = 20  # change back to 20
    try:
        os.remove("memes.txt")
    except:
        pass
    with open("memes.txt", "a") as f:
        f.write(str(datetime.datetime.now())[8:10] + "\n")
    url = "https://www.reddit.com/r/memes/top/?sort=top&t=all"
    while index > 0:
        request = requests.get(url, headers=header)
        soup = BeautifulSoup(request.content, "html.parser")
        link = soup.find("a", attrs={"rel": "nofollow next"})
        url = link["href"]
        index -= 1
        store_memes(soup)


# store 25 links from each soup object
def store_memes(soup):
    memes = soup.find_all("div")
    trueMemes = []
    for meme in memes:
        try:

            if meme["class"][0] == "thing":
                trueMemes.append(meme)
        except:
            pass

    urls = []
    for tm in trueMemes:
        try:
            if tm["data-url"]:
                urls.append(tm["data-url"])
        except:
            pass

    for url in urls:
        # print(url + " \n")
        pass
    urls.remove(urls[0])
    with open("memes.txt", "a") as f:
        for url in urls:
            f.write(url + "\n")


def get_meme():
    myFile = Path("memes.txt")
    if myFile.is_file():
        with open("memes.txt") as f:
            firstLine = f.readline()
            now = str(datetime.datetime.now())[8:10] + "\n"
            if (firstLine == now):
                rnd = random.randint(2, 499)
                while rnd > 0:
                    rnd -= 1
                    link = f.readline()
                print("type of link" + str(type(link)))
                return link
            else:
                call_urls()
                return get_meme()
    else:
        print("calling urls")
        call_urls()
        print("urls called, calling get_meme")
        return get_meme()