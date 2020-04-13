import os
import requests
import discord
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
TOKEN = "Njk0MjUyODE4MjAyMjMwNzg0.XoI-Mg.7yNRFrJkRTHdIfzd2BVpTEcAQsc"

client = discord.Client()


@client.event
async def on_ready():
    for guild in client.guilds:
        print(
            f'{client.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})'
        )


@client.event
async def on_message(message):
    if message.content.lower().startswith('!covid '):
        country = message.content.lower().replace('!covid ', '')
        try:
            if country == "western sahara":
                embed = discord.Embed(title="SE7RA MGHRIBIA ")
                embed.set_thumbnail(url="https://i.ytimg.com/vi/LmgSMNqhMXQ/hqdefault.jpg")
                # embed.add_field(name="Last Update", value=updated, inline=False)
                await message.channel.send(embed=embed)
            else:
                rsp = requests.get("https://corona.lmao.ninja/countries/" + country)
                # timestamp = rsp.json()["updated"]
                # updated = datetime.fromtimestamp(timestamp)
                embed = discord.Embed(title="COVID-19 Stats for " + str(rsp.json()["country"]))
                embed.set_thumbnail(url=rsp.json()["countryInfo"]["flag"])
                embed.add_field(name="Total Cases", value=str(rsp.json()["cases"]), inline=False)
                embed.add_field(name="Total Deaths", value=str(rsp.json()["deaths"]), inline=False)
                embed.add_field(name="Total Recovered", value=str(rsp.json()["recovered"]), inline=False)
                # embed.add_field(name="Last Update", value=updated, inline=False)
                await message.channel.send(embed=embed)
        except Exception as e:
            print(repr(e))
            await message.channel.send("something went wrong maybe country name typo")


client.run(TOKEN)
