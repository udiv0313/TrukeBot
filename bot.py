import discord
import responses

async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)

def run_discord_bot():
    Token = 'MTA1NTg3MTk2MDIzMzU1Mzk4MA.G6d6Ma.vnHducWaU5bQYfBZxH-2beZKscE9IdhPr5oDJE'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)
    # client = discord.Client()

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said: "{user_message} ({channel})"')

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=True)

    client.run(Token)

