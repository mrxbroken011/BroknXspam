import asyncio
from pyrogram import idle
from DcSpamBot import bot1, bot2, bot3, bot4, bot5, bot6, bot7, bot8, bot9, bot10, LOGGER

# List of bots
bots = [bot1, bot2, bot3, bot4, bot5, bot6, bot7, bot8, bot9, bot10]

async def start_bot(bot):
    try:
        await bot.start()
        await bot.send_message(LOGGER, "<b> Congrats!! BrokenSpamBot Started Successfully!</b>")
    except Exception as e:
        print(f"Failed to start bot {bot}: {e}")

async def main():
    # Start all bots concurrently
    await asyncio.gather(*(start_bot(bot) for bot in bots))
    # Keep the program running to maintain the bot sessions
    await idle()

if __name__ == "__main__":
    # Log message
    botlogs = "Yeah Your Spam Bot Deploying Successfully, "
    team = "© BROKEN X NETWORK"
    print(botlogs + team)

    # Run the main function
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
