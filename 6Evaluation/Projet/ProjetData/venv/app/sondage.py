from IPython import get_ipython
import pandas as pd 
import numpy as np
from datetime import datetime
from bs4 import BeautifulSoup
import requests


def fonction(string):
    string2 = ""
    for i in range(len(string)):
        if string[i:i+1] != "\t" and string[i:i+1] != "\n":
            string2+=string[i:i+1]
    return string2



from bs4 import BeautifulSoup
import requests

def fonctionA(link):
    response = requests.get(link)
    print(response)
    soup = BeautifulSoup(response.text,'html.parser')
    return soup



url2 = "https://fr.wikipedia.org/wiki/Liste_de_sondages_sur_l%27%C3%A9lection_pr%C3%A9sidentielle_fran%C3%A7aise_de_2022#Ann%C3%A9e_2022"

soup = fonctionA(url2)



def fonctionB(site):
    sondage2022 = soup.find(class_='wikitable')
    sondage2021 = soup.find(class_='NavFrame')

    X2022=[]
    X2021=[]
    for i in sondage2022.find_all('td'):
        T= i.text
        if len (T)<20:
            X2022.append(T)
            
    for i in sondage2021.find_all('td'):
        T= i.text
        if len (T)<20:
            X2021.append(T)

    col = []

    p = 1
    for i in sondage2022.find_all('th'):
        if p < 38 :
            title = (fonction(i.text))
            col.append(title)
            while '' in col:
                col.remove('')
        p = p + 1

    mois = ["janvier","février","mars","avril","mai","juin","juillet","aout","septembre","octobre","novembre","décembre"]
    k= 1
    for i in range (0,12) :
        mois[i] = k
        k = k+1


    


    Y = []
            
    for i in range (0,len(X2021)):
        if X2021[i] == 'OpinionWay\n':
            ligne= X2021[i:i+20]
            Y.append(ligne)
        if X2021[i] == 'Ifop\n' :
            ligne= X2021[i:i+20]
            Y.append(ligne)
        if X2021[i] == 'Harris Interactive\n' :
            ligne= X2021[i:i+20]
            Y.append(ligne)
        if X2021[i] == 'Harris-Interactive\n' :
            ligne= X2021[i:i+20]
            Y.append(ligne)
        if X2021[i] == 'Cluster17\n' :
            ligne= X2021[i:i+20]
            Y.append(ligne)
        if X2021[i] == 'BVA\n' :
            ligne= X2021[i:i+20]
            Y.append(ligne)
        if X2021[i] == 'Ipsos\n' :
            ligne= X2021[i:i+20]
            Y.append(ligne)
        if X2021[i] == 'Elabe\n' :
            ligne= X2021[i:i+20]
            Y.append(ligne)


        
    data21 = pd.DataFrame(data = Y, columns = col)
    data21[col] = data21[col].replace({'\n':''}, regex=True)
    data21[col] = data21[col].replace({'\<':''}, regex=True)
    data21[col] = data21[col].replace({'\,5':''}, regex=True)
    data21.drop('Échantillon', inplace=True, axis=1)
    data21['Date'] = data21['Date'].astype(str) + ' 2021'
    data21['Date'] = data21['Date'].str.split('-').str.get(-1)
    data21.drop(data21.tail(26).index,inplace=True)


    W=[]
    for i in range (0,len(X2022)):
        if X2022[i] == 'OpinionWay\n':
            ligne= X2022[i:i+20]
            W.append(ligne)
        if X2022[i] == 'Ifop\n' :
            ligne= X2022[i:i+20]
            W.append(ligne)
        if X2022[i] == 'Harris Interactive\n' :
            ligne= X2022[i:i+20]
            W.append(ligne)
        if X2022[i] == 'Harris-Interactive\n' :
            ligne= X2022[i:i+20]
            W.append(ligne)
        if X2022[i] == 'Cluster17\n' :
            ligne= X2022[i:i+20]
            W.append(ligne)
        if X2022[i] == 'BVA\n' :
            ligne= X2022[i:i+20]
            W.append(ligne)
        if X2022[i] == 'Ipsos\n' :
            ligne= X2022[i:i+20]
            W.append(ligne)
        if X2022[i] == 'Elabe\n' :
            ligne= X2022[i:i+20]
            W.append(ligne)
        
    data22 =pd.DataFrame(data = W, columns = col)
    data22[col] = data22[col].replace({'\n':''}, regex=True)
    data22[col] = data22[col].replace({'\<':''}, regex=True)
    data22[col] = data22[col].replace({'\,5':''}, regex=True)

    data22.drop('Échantillon', inplace=True, axis =1)
    data22['Date'] = data22['Date'].astype(str) + ' 2022'
    data22['Date'] = data22['Date'].str.split('-').str.get(-1)

    lst1=[]
    for j in range (2,19) :
        for i in data21[data21.columns[j]] :
            o1 = i.split('\xa0%')[0]
            if o1 == '<1':
                o1 = '1'
            if o1 == "—" :
                o1 = '0'
            if o1 == '<0,5':
                o1 = '0'
            if o1 == '0,5':
                o1 = '0'
            if o1 == '1%' :
                o1 = '1'
            o1 = int(o1)
            lst1+=[o1]
        nvSerie1 = pd.Series(lst1)
        data21[data21.columns[j]]=nvSerie1
        del lst1[:]



    lst2=[]
    import numpy as np
    import re


    for j in range (2,19) :
        for i in data22[data22.columns[j]] :
            
            o2 = i.split('\xa0%')[0]
            
            
            if o2 == '<1':
                o2 = '1'
            if o2 == "—" :
                o2 = '0'
            if o2 == '<0,5':
                o2 = '0'
            if o2 == '0,5':
                o2 = '0'

            o2 = int(o2)
            lst2+=[o2]
        nvSerie2 = pd.Series(lst2)
        data22[data22.columns[j]]=nvSerie2
        del lst2[:]
        


    dataP = pd.concat([data22,data21],ignore_index=True)
    dataP['Date'] = dataP['Date'].replace("", " ")
    print(dataP)


    g = dataP['Date'].astype(str).str.split(' ')

    mc=[]

    for j in range (len(dataP['Date'])) :
        for i in dataP['Date'] :
            
            f = dataP['Date'].str.split(' ')[j][0]
            t = dataP['Date'].str.split(' ')[j][1]
            if t == 'janvier' :
                t = '1'
            if t == 'février' :
                t = '2'
            if t == 'mars' :
                t = '3'
            if t == 'avril' :
                t = '4'
            if t == 'mai' :
                t = '5'
            if t == 'juin' :
                t = '6'
            if t == 'juillet' :
                t = '7'
            if t == 'août' :
                t = '8'
            if t == 'septembre' :
                t = '9'
            if t == 'octobre' :
                t = '10'
            if t == 'novembre' :
                t = '11'
            if t == 'décembre' :
                t = '12'
            p = dataP['Date'].str.split(' ')[j][2]
        m = f +str(" ") + t +str(" ") + p
        dataP['Date'] = m
    dataP['Date'] = pd.to_datetime(dataP['Date'], format ='%d %m %Y')


    return(dataP)