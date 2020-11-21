import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')
            print('Message from {0.author}: {0.content}'.format(message))

try:
    token = os.environ['DISCORD_GREMLIN_TOKEN']
    client = MyClient()
    client.run(token)
except Error as e:
    log.error("Server died")
    log.error(e)
    
