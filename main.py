import matplotlib.pyplot as plt
import discord
import io

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

def some_plot_function():
    # Data goes here!!!
    x = [1, 2, 3, 4]
    y = [1, 4, 9, 16]

    
    fig, ax = plt.subplots()

    
    ax.plot(x, y)

    
    ax.set_xlabel('x')
    ax.set_ylabel('y')

    return fig


@client.event
async def on_message(message):
    async def send_plot_to_discord(client, plot_function, channel_id):
        
        fig = plot_function()

        # When saving using buf makes it so much easier cause then its unnecessary to download each png
        buf = io.BytesIO()
        fig.savefig(buf, format='png')
        buf.seek(0)

        
        file = discord.File(buf, filename='plot.png')
        await message.author.send(channel_id, file=file)

        # Close the plot and clear it from memory
        plt.close(fig)

    if message.author == client.user:
        return
    if message.content == "!plot":
        await send_plot_to_discord(client, some_plot_function, message.channel)


client.run('Discord bot key here')
