import matplotlib.pyplot as plt
import discord
import io
import datetime

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

counts = {}

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


async def update_and_plot(client, channel_id):

    current_time = datetime.datetime.now()
    counts[current_time] = counts.get(current_time, 0) + 1


    fig, ax = plt.subplots()
    ax.plot(list(counts.keys()), list(counts.values()))
    ax.set_xlabel('Time')
    ax.set_ylabel('Count')


    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)


    file = discord.File(buf, filename='plot.png')
    channel = client.get_channel(channel_id)
    await channel.send(file=file)


    plt.close(fig)


@client.event
async def on_message(message):
    async def update_and_plot(client, channel_id):

        current_time = datetime.datetime.now()
        counts[current_time] = counts.get(current_time, 0) + 1


        fig, ax = plt.subplots()
        ax.plot(list(counts.keys()), list(counts.values()))
        ax.set_xlabel('Time')
        ax.set_ylabel('Count')


        buf = io.BytesIO()
        fig.savefig(buf, format='png')
        buf.seek(0)


        file = discord.File(buf, filename='plot.png')
        channel = client.get_channel(channel_id)
        await channel.send(file=file)


        plt.close(fig)
    if message.author == client.user:
        return
    if "winner" in message.content.lower():
        await update_and_plot(client, message.channel.id)

client.run('MTA1NjMyNzYyOTE5NzgyNDEwMA.G-dv4C.NZcvfc-UpmDbWG4oaDZjgw0GlgAZNKtGGhFbRE')
