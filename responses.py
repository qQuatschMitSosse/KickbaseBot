import scraper


# Compare the players in the own team with the players in the predicted lineup
# and return a message with the active and inactive players
def compare_players(own_team):
    players = scraper.scrape_lineup()

    active = []
    inactive = []

    for player in own_team:
        if player in players:
            active.append(player)
        else:
            inactive.append(player)

    message_active = "Am Wochenende spielen aus deinem Team: "
    for player in active:
        message_active += player + ", "

    message_inactive = "Am Wochenende spielen aus deinem Team nicht: "
    for x in inactive:
        message_inactive += x + ", "

    return message_active[:-2], message_inactive[:-2]
