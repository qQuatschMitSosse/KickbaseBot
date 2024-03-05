import requests
from bs4 import BeautifulSoup

from constants import CLUBLIST


def scrape_lineup():
    lineups = []

    for club in CLUBLIST:
        html_text = requests.get(club).text
        soup = BeautifulSoup(html_text, 'lxml')
        lineup = soup.find_all('div', class_='player_name')

        for player in lineup:
            lineups.append(player.text)

    return lineups

