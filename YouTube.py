import requests
from bs4 import BeautifulSoup
import webCrawler

header = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'}


def search(item):
    url = "https://www.google.com/search?hl=en&q=" + str(item.replace(" ", "%20")) + "%20site%3Ayoutube.com&tbm=vid"
    request = requests.get(url, headers = header)
    soup = BeautifulSoup(request.content, "html.parser")
    rs = soup.find_all("div", class_ = "r")
    a = rs[0].find("a")
    return a["href"]


