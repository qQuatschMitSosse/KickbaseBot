import asyncio
import constants
import telegram
import datetime
import time
import KickbaseScraper
import responses

# Telegram-Bot-API-Token eintragen
TOKEN = constants.API_KEY

# Bot initialisieren
bot = telegram.Bot(token=TOKEN)
response = KickbaseScraper.scrapeAufstellung()

# Funktion zum Senden der Nachricht definieren
async def send_Aktiv():
    await bot.send_message(chat_id='-1001823651702', text=responses.comparePlayer(constants.PLAYERLIST)[0])
    await bot.send_message(chat_id='-1001823651702', text=responses.comparePlayer(constants.PLAYERLIST)[1])


async def main():
    while True:
       now = datetime.datetime.now()
       if now.hour == 14 and now.minute == 45:
            await send_Aktiv()
            break
       await asyncio.sleep(60)

asyncio.run(main())