from bs4 import BeautifulSoup
import requests
import csv
from datetime import date

def scrape(url):
    r = requests.get(url)
    return r.text


movieName = input("Enter movie/TV name   :   ")

urlDir = "https://www.google.co.in/search?q="+movieName+"+director"
urlCast = "https://www.google.co.in/search?q="+movieName+"+cast"

html = scrape(urlDir)
soup = BeautifulSoup(html, "html.parser")
#director = 

#print(soup.prettify())
dirString = (soup.findAll("div", {"class": "BNeawe s3v9rd AP7Wnd"}))[0]
dirName = (dirString.text.partition("is")[0])

html = scrape(urlCast)
soup = BeautifulSoup(html, "html.parser")

casts = (soup.findAll("div", {"class":"BNeawe s3v9rd AP7Wnd"}))
cast = []
for i in casts:
    cast.append(i.text)
print(cast)
today = date.today()
d = today.strftime("%B %d, %Y")



'''with open("movies2020.csv", 'a+', newline="") as movie:
    write = csv.writer(movie)
    #write.writerow(['sl.no','MOVIE NAME','DIRECTOR', 'CAST', 'RATING', 'MY RATING', 'REVIEW'])
    write.writerow(['sl.no',str(d) ,dirName, cast[:4], 'RATING', 'MY RATING', 'REVIEW'])
'''
