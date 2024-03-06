import asyncio
import datetime
import os

import telegram
from dotenv import load_dotenv

import responses
import scraper
from constants import PLAYERLIST

# load the API key from the .env file
load_dotenv('.env')
TOKEN = os.getenv('API_KEY')

# Initialize the bot
bot = telegram.Bot(token=TOKEN)
response = scraper.scrape_lineup()


# Function to send the lineup information to the user
# The function sends two messages to the user, one with the active players and one with the inactive players
# The messages are created by the compare_players function from responses.py
async def send_lineup_information():
    await bot.send_message(chat_id='-1001823651702', text=responses.compare_players(PLAYERLIST)[0])
    await bot.send_message(chat_id='-1001823651702', text=responses.compare_players(PLAYERLIST)[1])


# Main function to check the time and send the lineup information
async def main():
    while True:
        now = datetime.datetime.now()
        if now.hour == 15 and now.minute == 30:
            await send_lineup_information()
            break
        await asyncio.sleep(60)


asyncio.run(main())
