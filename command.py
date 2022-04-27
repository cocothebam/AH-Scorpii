import random as rnd
import string
import requests
import webbrowser
from bs4 import BeautifulSoup


class openImage:
    def getdata(url):
        r = requests.get(url)
        return r.text

    def findImage():
        URL = "http://prnt.sc/"
        numExtension = str(rnd.randint(1, 1000000000))
        URL += numExtension
        webbrowser.open(URL)
        htmldata = openImage.getdata("https://www.google.com/")

        soup = BeautifulSoup(htmldata, "html.parser")
        for item in soup.find_all("img"):
            print(item["src"])
