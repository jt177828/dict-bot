from urllib import response
import discord
from discord.ext import commands, tasks
import token
import requests
import json

endpoint = "entries"
language_code = "en-us"
word_id = "example"

response = requests.get(f"https://dictionaryapi.com/api/v3/references/thesaurus/json/test?key=b502c0fc-5b63-4d8c-a3a5-3da326b73684",
                        headers={'app_id': '8b220f60', 'app_key': 'b502c0fc-5b63-4d8c-a3a5-3da326b73684'})


def urlsynonyms(word):
    return(f"https://dictionaryapi.com/api/v3/references/thesaurus/json/{word}?key=b502c0fc-5b63-4d8c-a3a5-3da326b73684")


print(response.status_code)


client = commands.Bot(command_prefix="!dict ", case_insensitive=True)


@ client.command(aliases=["d"])
async def define(ctx, word: str):
    response = requests.get(urlsynonyms(word))
    print(response.json())
    # await ctx.send(response.json())

token = "OTYyMTgwNjU5NDg3NTg0MzA2.YlDykQ.q-vPYQY12AnrRTgEgbEU2TG10Xk"

client.run(token)
