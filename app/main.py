import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.google.com")
#print(response.text)

##Gestion des erreurs
# url ='http://blancadosder.com'
# try: 
#     response = requests.get(url)
#     response.raise_for_status()
    
# except requests.exceptions.HTTPError as errh :
#     print("HTTP Error :", errh)
    
# except requests.exceptions.ConnectionError as errc:
#     print("Erreur Connecting :", errc)

# except requests.exceptions.Timeout as errt :
#     print("Timeout errort")

# except requests.exceptions.RequestException as err:
#     print("Oops :Something else", err)

# with open('index.html', 'w') as f :
#     f.write(response.text)  

url ="https://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser') # 'html.parser' is written in c and it is very faster than 'html5lib' (that is supported with python) and 'lxml_xml' or lxml 
#print(soup.prettify())

# Fonction pour parcourir recursivement l arbre DOM
def traverse_dom(element, level=0):
    #Afficher l element actuel
    if element.name:
        print(f"{'' *level}<{element.name}>")
        
    # si l element a des enfants, le parcourir egalement
    if hasattr(element,'children'):
        for child in element.children:
            traverse_dom(child, level+1)
#commencer le parcours depuis la racine de l arbre DOM
traverse_dom(soup)