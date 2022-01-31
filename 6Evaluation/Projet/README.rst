PROJET DATA ENGINEERING
===========


-> Présentation du projet :
*********

Ce projet consiste à récupérer des données sur différents sites web autour d’un même thème ( Nous avons choisi la politique en France) par des méthodes de scraping.
Nous avons donc voulu récolter des données textuelles comme des articles et des données sous forme de tableaux pour réaliser des graphiques sur les sondages à la présidentielle 2022.
Dans un second temps nous devions traiter ces données via Mongo et les afficher sur un mini site web codé sous Flask, un module de Micro Framework en python.

*********
→ Scraping et Méthodes utilisées :
*********

Tout d’abord nous avons effectué des recherches afin d’obtenir plusieurs sites à Scraper pour obtenir des données réutilisables ou même des datas pour tracer au préalable nos courbes sur notre support (flask).
Nous avons tout d’abord utilisé le site de deux médias français connus: Le Monde et le Figaro pour pouvoir scraper les dernières actualités sur la présidentielle 2022.

Ensuite, nous sommes tombés sur le site wikipédia qui regroupait à lui seul plusieurs sources de sondages. 
Ces données remontent jusqu’en octobre 2017. Cependant nous avons décidé de commencer notre Scrapping seulement à partir de septembre 2021 là où l'engouement et l’échantillon est au plus fort, c'est-à-dire que les données deviennent intéressantes à exploiter.
Pour débuter le scrapping du site ci-dessus, nous avons utilisé BeautifulSoup pour récupérer les données sur un jupyter notebook.
Une fois ces données récupérées, nous avons décidé de garder la même architecture que le tableau présenté sur wikipédia (même nom de colonne) et crée ensuite une data frame avec toutes les données obtenues en 2022 puis 2021.

Les deux datas créées ont été nettoyées puis concaténées pour n’avoir qu’une data utilisable.

Après avoir obtenu notre data final, nous avons dû la convertir en un fichier .json pour l’importer sur notre support flask.

Nous avons finalisé le scraping de celui-ci en téléchargeant notre jupyter en .py.


Dans le même dossier ou est téléchargé le scraping.py il faut créer un dossier dataP.json une fois fait, il suffit de lancer la commande : (chemin d’accès du scraping.py) Ipython Scraping.py dans un terminal afin d’avoir le fichier dataP.json à jour des données que l’on récupère du site.


Nous avons ensuite rencontré un problème lorsqu’on a voulu utiliser le fichier json car à notre niveau nous n'avons pas réussi à importer notre json dans flask.
Nous avons donc décidé de faire un copier-coller de notre fichier json dans notre javascript et ensuite de le modifier pour qu’il soit utilisable afin de créer plusieurs graphiques.

*********
→ Packages installés dans notre environnement virtuel Python (venv) :
*********

Pour ce projet nous avons dû installer plusieurs modules python dans notre (venv):
>pip install flask
>pip install socketserver
>pip install bs4
>pip install requests


*********
→ Commandes à exécuter pour lancer l’application web : 
*********

Sous windows
Télécharger le dossier Projet_Data_Engineering puis ouvrir un terminal de commande. 
Se placer dans le répertoire /venv du projet et écrire dans le terminal :

C:…\venv>Scripts\activate 

Une fois l'environnement virtuel python lancé, vous devez voir apparaître '(venv)' au début de votre ligne de commande. 
Ensuite il faut lancer le serveur local flask qui fera tourner notre site Web. 
Pour cela, dans le terminal,  toujours dans le répertoire /venv/ écrivez ces trois lignes de commande :

(venv) C:…\venv>set FLASK_APP=app
(venv) C:...\venv>FLASK_ENV=development
(venv) C:...\venv>flask run 


Enfin, il faut ouvrir l’url donné sous cette dernière commande sur un navigateur web.  (http://127.0.0.1:5000/) 

*********
→ Utilisation de flask :
*********

Flask est un module de python qui permet de mettre en place un micro framework. 
Nous avons donc eu besoin de maîtriser plusieurs langages de programmation pour obtenir une interface web convenable fonctionnelle et interactive. 
Tout d'abord, le cœur du projet tourne autour des fichiers python et des différentes fonctions qui les composent. 
Le fichier principal est le fichier ‘__init__.py’ qui assure la transition entre le moteur logique du site Web et les 'templates', les pages HTML qui décrivent l'organisation des éléments que verra l'utilisateur sur chaque page du site. 
Ces fichiers HTML ne permettent cependant que d'afficher du contenu "brut" et dénué de style. 
Pour ajouter du style à nos templates nous avons créé un fichier style.css (codé en CSS donc). 
Enfin, nous avons utilisé des scripts en Javascript pour dynamiser les éléments html et créer des graphiques à partir des données de sondages que nous avions scrapées sur Wikipedia. 

*********
→ Architecture détaillée du projet:
*********

Le projet est composé de différents fichiers.
Tout d’abord, il est composé de 3 fichiers PYTHON : les fichiers ‘lefigaro.py’, ‘lemonde.py’,  qui se chargent du scraping en temps réel des données figurant sur les sites  “Le figaro” et “Le Monde”, ,le fichier ‘__init__.py’ qui relie tous les autres en les important et en transmettant les données scrapées aux templates comme nous l’avons vu précédemment.


Il est également composé de 6 fichiers HTML . Le fichier about.html correspond au squelette des autres fichiers HTML. C'est-à-dire que tous les autres fichiers dépendent de ce dernier (héritage de templates) : le fond d'écran, la barre de navigation et la disposition des éléments. 
Le fichier ‘homepage.html’ est comme son nom l'indique la page d'accueil de notre site. 
Le fichier ‘about.html’ est la template qui décrit l'équipe projet, une sorte de "qui sommes nous ?". 
Le fichier ‘sondages.html’ reprend les données json scrapées sur Wikipedia et les affiche sous la forme de graphiques. 
Enfin les fichiers lefigaro.html et lemonde.html affichent les données scrapées en temps réel sur les sites respectifs. 
C'est dans dans le fichier ‘base.html’ que le script javascript permettant de créer les graphiques de la page sondages est situé. 

Le projet comporte enfin 1 fichier style.css avec le style donné à toutes les balises html du dossier templates et toutes les images .png et .jpg utilisées dans le projet. 


