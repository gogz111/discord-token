import discord
import threading

tokens = ["token1", "token2", "token3"]  # ⚠️ These are user tokens

def run_selfbot(token):
    client = discord.Client()

    @client.event
    async def on_ready():
        print(f"{client.user} is online")

    client.run(token, bot=False)  # bot=False means it's a selfbot (TOS violation)

for token in tokens:
    t = threading.Thread(target=run_selfbot, args=(token,))
    t.start()
