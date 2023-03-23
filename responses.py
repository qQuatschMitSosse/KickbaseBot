import KickbaseScraper
import constants


def comparePlayer(own_team):
    players = KickbaseScraper.scrapeAufstellung()

    aktiv = []
    inaktiv = []


    for player in own_team:
        if player in players:
            aktiv.append(player)
        else:
            inaktiv.append(player)
            #return f'{player} wird am Wochenende nicht spielen.'


    antwortAktiv = 'Am Wochenende spielen aus deinem Team: '
    for x in aktiv:
        antwortAktiv += ', ' + x

    antwortUnaktiv = 'Am Wochenende spielen aus deinem Team nicht: '
    for x in inaktiv:
        antwortUnaktiv += ', ' + x

    return antwortAktiv, antwortUnaktiv



