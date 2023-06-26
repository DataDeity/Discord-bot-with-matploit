# Discord Bot Plotter

This is a Python code snippet that demonstrates a Discord bot capable of plotting and updating a graph based on certain messages received.

## Prerequisites

To run this code, you need to have the following dependencies installed:

- `matplotlib`: A plotting library for Python.
- `discord.py`: An API wrapper for Discord written in Python.

You can install these dependencies using `pip` by running the following command:

```
pip install matplotlib discord.py
```

## Usage

1. Import the necessary libraries:

```python
import matplotlib.pyplot as plt
import discord
import io
import datetime
```

2. Set up the Discord bot:

```python
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
```

3. Define a dictionary to keep track of message counts:

```python
counts = {}
```

4. Set up an event handler for when the bot is ready:

```python
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
```

5. Define a function to update and plot the graph:

```python
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
```

6. Set up an event handler for when a message is received:

```python
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if "winner" in message.content.lower():
        await update_and_plot(client, message.channel.id)
```

7. Run the Discord bot by providing your bot token:

```python
client.run('Discord bot token')
```

Make sure to replace `'Discord bot token'` with your actual Discord bot token.

## License

This code is released under the [MIT License](https://opensource.org/licenses/MIT).
