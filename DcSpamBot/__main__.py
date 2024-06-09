
sudo apt-get update
sudo apt-get install ntp

sudo service ntp start
sudo ntpdate -u pool.ntp.org

date


pip install ntplib


import asyncio
import ntplib
from time import ctime
from pyrogram import idle
from DcSpamBot import bot1, bot2, bot3, bot4, bot5, bot6, bot7, bot8, bot9, bot10, LOGGER

# List of bots
bots = [bot1, bot2, bot3, bot4, bot5, bot6, bot7, bot8, bot9, bot10]

def sync_time():
    try:
        client = ntplib.NTPClient()
        response = client.request('pool.ntp.org')
        print(f"System time synchronized: {ctime(response.tx_time)}")
    except Exception as e:
        print(f"Failed to synchronize time: {e}")

async def start_bot(bot):
    try:
        await bot.start()
        await bot.send_message(LOGGER, "<b> Congrats!! BrokenSpamBot Started Successfully!</b>")
    except Exception as e:
        print(f"Failed to start bot {bot}: {e}")

async def main():
    sync_time()
    await asyncio.gather(*(start_bot(bot) for bot in bots))
    await idle()

if __name__ == "__main__":
    botlogs = "Yeah Your Spam Bot Deploying Successfully, "
    team = "© BROKEN X NETWORK"
    print(botlogs + team)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
