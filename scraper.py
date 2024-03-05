from bs4 import BeautifulSoup
from constants import VEREINSLISTE
import requests

def scrapeAufstellung():
    aufstellungen = []

    for verein in VEREINSLISTE:
        html_text = requests.get(verein).text
        soup = BeautifulSoup(html_text, 'lxml')
        aufstellung = soup.find_all('div', class_='player_name')

        for spieler in aufstellung:
            aufstellungen.append(spieler.text)

    return aufstellungen

print(scrapeAufstellung())
