import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver



# Lunch Webdrive to open target URL  / [the webdriver Could be stored on it's own instead of a whole code]

driver = webdriver.Chrome()
driver.get("https://thelevesque.com/collections/all")
results=[]

content = driver.page_source
soup= BeautifulSoup(content)



def parseImageUrls(classes,location,source):
    for a in soup.findAll(attrs={'class':classes}):
        name = a.find(location)
        if name not in results:
            results.append(name.get(source))
            



classes = 'image__img'
location ="img"
source = "src"

parseImageUrls("image__img", "img", "src")

df = pd.DataFrame({"links":results})
df.to_csv("links.csv", index=False, encoding="utf-8")
