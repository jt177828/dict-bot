from urllib import response
import discord
from discord.ext import commands, tasks
import token
import requests
import json

endpoint = "entries"
language_code = "en-us"
word_id = "example"

response = requests.get(f"https://dictionaryapi.com/api/v3/references/collegiate/json/test?key=23bbc9d1-539a-4827-94a2-ee37eb6ee1c1",
                        headers={'app_id': '8b220f60', 'app_key': '23bbc9d1-539a-4827-94a2-ee37eb6ee1c1'})

response = requests.get(f"https://dictionaryapi.com/api/v3/references/thesaurus/json/test?key=b502c0fc-5b63-4d8c-a3a5-3da326b73684",
                        headers={'app_id': '8b220f60', 'app_key': 'b502c0fc-5b63-4d8c-a3a5-3da326b73684'})


def url(word):
    return(f"https://dictionaryapi.com/api/v3/references/collegiate/json/{word}?key=23bbc9d1-539a-4827-94a2-ee37eb6ee1c1")


def urlsynonyms(word):
    return(f"https://dictionaryapi.com/api/v3/references/thesaurus/json/{word}?key=b502c0fc-5b63-4d8c-a3a5-3da326b73684")


print(response.status_code)


client = commands.Bot(command_prefix="!dict ", case_insensitive=True)


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('Prefix: !dict'))
    print('Bot is ready.')


@ client.command(aliases=["d"])
async def define(ctx, word: str):
    response = requests.get(url(word))

    output = response.json()

    if len(output) == 0:
        await ctx.send("Word doesn't exist!")
    else:
        print(output)
        await ctx.send(f"__**Word: {word}**__")
        await ctx.send(f"**Part of Speech**: {output[0]['fl']}")
        await ctx.send(f"**Pronounciation**: {output[1]['hwi']['prs'][0]['mw']}")
        await ctx.send(f"**Most Common Definition**: {output[1]['def'][0]['sseq'][0][0][1]['dt'][0][1]}")


@ client.command(aliases=["t"])
async def synonym(ctx, word: str):
    response = requests.get(urlsynonyms(word))

    output = response.json()
    if len(output) == 0:
        await ctx.send("Word doesn't exist!")
    else:
        await ctx.send(f"__**Word: {word}**__")
        # for syn in output[0]
        await ctx.send(f"**Synonyms:** {output[0]['meta']['syns'][0]}")
        await ctx.send(f"**Anyonyms:** {output[0]['meta']['ants'][0]}")
        print(output)


token = "OTYyMTgwNjU5NDg3NTg0MzA2.YlDykQ.q-vPYQY12AnrRTgEgbEU2TG10Xk"

client.run(token)
