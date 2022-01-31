from bs4 import BeautifulSoup
import requests
import json

def fonction1(link):
    response = requests.get(link)
    soup = BeautifulSoup(response.text)
    return soup

##site="https://www.lefigaro.fr/elections/presidentielles"

def fonction2(site,nb):
    article=[]
    if nb==1:
        page =site
    else :
        page = site + '?page=' + str(nb)
    for i in fonction1(page).find(class_="fig-bottom fig-layout fig-layout--wrapped").find_all(class_="fig-profile__link"):
        link = i.get("href")
        soup1 = fonction1(link)
        title= soup1.find(class_="fig-headline").text
        description=""

        for j in soup1.find_all(class_="fig-content-body"):
            description = j.text
        article.append({'Title': title,
                'Description':description,
                'Lien': link})
                
    for i in fonction1(page).find(class_="fig-main-col").find_all(class_="fig-profile__link"):
        link = i.get("href")
        soup1 = fonction1(link)
        title= soup1.find(class_="fig-headline").text
        description=""    
        
        for j in soup1.find_all(class_="fig-content-body"):
            description = j.text
        article.append({'Title': title,
                'Description':description,
                'Lien': link})
    return(article)