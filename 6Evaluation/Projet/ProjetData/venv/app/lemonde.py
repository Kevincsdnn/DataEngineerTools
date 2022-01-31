from bs4 import BeautifulSoup
import requests
import json

def fonctiona(link):
    response = requests.get(link)
    soup = BeautifulSoup(response.text)
    return soup


site="https://www.lemonde.fr/election-presidentielle-2022/"

def fonctionb(site):
    article=[]
    for i in fonctiona(site).find_all(class_="thread"):
        link = i.find(class_="teaser__link").get("href")
        title= i.find(class_="teaser__title").text
        description=i.find(class_="teaser__desc").text
        article.append({'Title': title,
                'Description':description,
                'Lien': link})
    return(article)
