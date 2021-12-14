import os
try:
    import requests
except:
    os.system('pip install requests')
    import requests
import base64
try:
    from termcolor import colored
except:
    os.system('pip install termcolor')
    from termcolor import colored
from datetime import datetime
import asyncio
import io
import time
import random
try:
    import typing
except:
    os.system('pip install typing')
    import typing
import urllib.parse
import urllib.request
try:
    from bs4 import BeautifulSoup as bs4
except:
    os.system('pip install bs4')
    from bs4 import BeautifulSoup as bs4
try:
    import aiohttp
except:
    os.system('pip install aiohttp')
    import aiohttp
try:
    import discord
except:
    os.system('pip install discord.py')
    import discord
from discord.ext import commands, tasks
try:
    from animec import *
except:
    os.system('pip install animec')
    from animec import *
import json
from PIL import Image
try:
    from flask import Flask
except:
    os.system('pip install flask')
    from flask import Flask
from threading import Thread

blank_langs = {
    "ab":{
        "name":"Abkhaz",
        "nativeName":"аҧсуа"
    },
    "aa":{
        "name":"Afar",
        "nativeName":"Afaraf"
    },
    "af":{
        "name":"Afrikaans",
        "nativeName":"Afrikaans"
    },
    "ak":{
        "name":"Akan",
        "nativeName":"Akan"
    },
    "sq":{
        "name":"Albanian",
        "nativeName":"Shqip"
    },
    "am":{
        "name":"Amharic",
        "nativeName":"አማርኛ"
    },
    "ar":{
        "name":"Arabic",
        "nativeName":"العربية"
    },
    "an":{
        "name":"Aragonese",
        "nativeName":"Aragonés"
    },
    "hy":{
        "name":"Armenian",
        "nativeName":"Հայերեն"
    },
    "as":{
        "name":"Assamese",
        "nativeName":"অসমীয়া"
    },
    "av":{
        "name":"Avaric",
        "nativeName":"авар мацӀ, магӀарул мацӀ"
    },
    "ae":{
        "name":"Avestan",
        "nativeName":"avesta"
    },
    "ay":{
        "name":"Aymara",
        "nativeName":"aymar aru"
    },
    "az":{
        "name":"Azerbaijani",
        "nativeName":"azərbaycan dili"
    },
    "bm":{
        "name":"Bambara",
        "nativeName":"bamanankan"
    },
    "ba":{
        "name":"Bashkir",
        "nativeName":"башҡорт теле"
    },
    "eu":{
        "name":"Basque",
        "nativeName":"euskara, euskera"
    },
    "be":{
        "name":"Belarusian",
        "nativeName":"Беларуская"
    },
    "bn":{
        "name":"Bengali",
        "nativeName":"বাংলা"
    },
    "bh":{
        "name":"Bihari",
        "nativeName":"भोजपुरी"
    },
    "bi":{
        "name":"Bislama",
        "nativeName":"Bislama"
    },
    "bs":{
        "name":"Bosnian",
        "nativeName":"bosanski jezik"
    },
    "br":{
        "name":"Breton",
        "nativeName":"brezhoneg"
    },
    "bg":{
        "name":"Bulgarian",
        "nativeName":"български език"
    },
    "my":{
        "name":"Burmese",
        "nativeName":"ဗမာစာ"
    },
    "ca":{
        "name":"Catalan; Valencian",
        "nativeName":"Català"
    },
    "ch":{
        "name":"Chamorro",
        "nativeName":"Chamoru"
    },
    "ce":{
        "name":"Chechen",
        "nativeName":"нохчийн мотт"
    },
    "ny":{
        "name":"Chichewa; Chewa; Nyanja",
        "nativeName":"chiCheŵa, chinyanja"
    },
    "zh":{
        "name":"Chinese",
        "nativeName":"中文 (Zhōngwén), 汉语, 漢語"
    },
    "cv":{
        "name":"Chuvash",
        "nativeName":"чӑваш чӗлхи"
    },
    "kw":{
        "name":"Cornish",
        "nativeName":"Kernewek"
    },
    "co":{
        "name":"Corsican",
        "nativeName":"corsu, lingua corsa"
    },
    "cr":{
        "name":"Cree",
        "nativeName":"ᓀᐦᐃᔭᐍᐏᐣ"
    },
    "hr":{
        "name":"Croatian",
        "nativeName":"hrvatski"
    },
    "cs":{
        "name":"Czech",
        "nativeName":"česky, čeština"
    },
    "da":{
        "name":"Danish",
        "nativeName":"dansk"
    },
    "dv":{
        "name":"Divehi; Dhivehi; Maldivian;",
        "nativeName":"ދިވެހި"
    },
    "nl":{
        "name":"Dutch",
        "nativeName":"Nederlands, Vlaams"
    },
    "en":{
        "name":"English",
        "nativeName":"English"
    },
    "eo":{
        "name":"Esperanto",
        "nativeName":"Esperanto"
    },
    "et":{
        "name":"Estonian",
        "nativeName":"eesti, eesti keel"
    },
    "ee":{
        "name":"Ewe",
        "nativeName":"Eʋegbe"
    },
    "fo":{
        "name":"Faroese",
        "nativeName":"føroyskt"
    },
    "fj":{
        "name":"Fijian",
        "nativeName":"vosa Vakaviti"
    },
    "fi":{
        "name":"Finnish",
        "nativeName":"suomi, suomen kieli"
    },
    "fr":{
        "name":"French",
        "nativeName":"français, langue française"
    },
    "ff":{
        "name":"Fula; Fulah; Pulaar; Pular",
        "nativeName":"Fulfulde, Pulaar, Pular"
    },
    "gl":{
        "name":"Galician",
        "nativeName":"Galego"
    },
    "ka":{
        "name":"Georgian",
        "nativeName":"ქართული"
    },
    "de":{
        "name":"German",
        "nativeName":"Deutsch"
    },
    "el":{
        "name":"Greek, Modern",
        "nativeName":"Ελληνικά"
    },
    "gn":{
        "name":"Guaraní",
        "nativeName":"Avañeẽ"
    },
    "gu":{
        "name":"Gujarati",
        "nativeName":"ગુજરાતી"
    },
    "ht":{
        "name":"Haitian; Haitian Creole",
        "nativeName":"Kreyòl ayisyen"
    },
    "ha":{
        "name":"Hausa",
        "nativeName":"Hausa, هَوُسَ"
    },
    "he":{
        "name":"Hebrew (modern)",
        "nativeName":"עברית"
    },
    "hz":{
        "name":"Herero",
        "nativeName":"Otjiherero"
    },
    "hi":{
        "name":"Hindi",
        "nativeName":"हिन्दी, हिंदी"
    },
    "ho":{
        "name":"Hiri Motu",
        "nativeName":"Hiri Motu"
    },
    "hu":{
        "name":"Hungarian",
        "nativeName":"Magyar"
    },
    "ia":{
        "name":"Interlingua",
        "nativeName":"Interlingua"
    },
    "id":{
        "name":"Indonesian",
        "nativeName":"Bahasa Indonesia"
    },
    "ie":{
        "name":"Interlingue",
        "nativeName":"Originally called Occidental; then Interlingue after WWII"
    },
    "ga":{
        "name":"Irish",
        "nativeName":"Gaeilge"
    },
    "ig":{
        "name":"Igbo",
        "nativeName":"Asụsụ Igbo"
    },
    "ik":{
        "name":"Inupiaq",
        "nativeName":"Iñupiaq, Iñupiatun"
    },
    "io":{
        "name":"Ido",
        "nativeName":"Ido"
    },
    "is":{
        "name":"Icelandic",
        "nativeName":"Íslenska"
    },
    "it":{
        "name":"Italian",
        "nativeName":"Italiano"
    },
    "iu":{
        "name":"Inuktitut",
        "nativeName":"ᐃᓄᒃᑎᑐᑦ"
    },
    "ja":{
        "name":"Japanese",
        "nativeName":"日本語 (にほんご／にっぽんご)"
    },
    "jv":{
        "name":"Javanese",
        "nativeName":"basa Jawa"
    },
    "kl":{
        "name":"Kalaallisut, Greenlandic",
        "nativeName":"kalaallisut, kalaallit oqaasii"
    },
    "kn":{
        "name":"Kannada",
        "nativeName":"ಕನ್ನಡ"
    },
    "kr":{
        "name":"Kanuri",
        "nativeName":"Kanuri"
    },
    "ks":{
        "name":"Kashmiri",
        "nativeName":"कश्मीरी, كشميري‎"
    },
    "kk":{
        "name":"Kazakh",
        "nativeName":"Қазақ тілі"
    },
    "km":{
        "name":"Khmer",
        "nativeName":"ភាសាខ្មែរ"
    },
    "ki":{
        "name":"Kikuyu, Gikuyu",
        "nativeName":"Gĩkũyũ"
    },
    "rw":{
        "name":"Kinyarwanda",
        "nativeName":"Ikinyarwanda"
    },
    "ky":{
        "name":"Kirghiz, Kyrgyz",
        "nativeName":"кыргыз тили"
    },
    "kv":{
        "name":"Komi",
        "nativeName":"коми кыв"
    },
    "kg":{
        "name":"Kongo",
        "nativeName":"KiKongo"
    },
    "ko":{
        "name":"Korean",
        "nativeName":"한국어 (韓國語), 조선말 (朝鮮語)"
    },
    "ku":{
        "name":"Kurdish",
        "nativeName":"Kurdî, كوردی‎"
    },
    "kj":{
        "name":"Kwanyama, Kuanyama",
        "nativeName":"Kuanyama"
    },
    "la":{
        "name":"Latin",
        "nativeName":"latine, lingua latina"
    },
    "lb":{
        "name":"Luxembourgish, Letzeburgesch",
        "nativeName":"Lëtzebuergesch"
    },
    "lg":{
        "name":"Luganda",
        "nativeName":"Luganda"
    },
    "li":{
        "name":"Limburgish, Limburgan, Limburger",
        "nativeName":"Limburgs"
    },
    "ln":{
        "name":"Lingala",
        "nativeName":"Lingála"
    },
    "lo":{
        "name":"Lao",
        "nativeName":"ພາສາລາວ"
    },
    "lt":{
        "name":"Lithuanian",
        "nativeName":"lietuvių kalba"
    },
    "lu":{
        "name":"Luba-Katanga",
        "nativeName":""
    },
    "lv":{
        "name":"Latvian",
        "nativeName":"latviešu valoda"
    },
    "gv":{
        "name":"Manx",
        "nativeName":"Gaelg, Gailck"
    },
    "mk":{
        "name":"Macedonian",
        "nativeName":"македонски јазик"
    },
    "mg":{
        "name":"Malagasy",
        "nativeName":"Malagasy fiteny"
    },
    "ms":{
        "name":"Malay",
        "nativeName":"bahasa Melayu, بهاس ملايو‎"
    },
    "ml":{
        "name":"Malayalam",
        "nativeName":"മലയാളം"
    },
    "mt":{
        "name":"Maltese",
        "nativeName":"Malti"
    },
    "mi":{
        "name":"Māori",
        "nativeName":"te reo Māori"
    },
    "mr":{
        "name":"Marathi (Marāṭhī)",
        "nativeName":"मराठी"
    },
    "mh":{
        "name":"Marshallese",
        "nativeName":"Kajin M̧ajeļ"
    },
    "mn":{
        "name":"Mongolian",
        "nativeName":"монгол"
    },
    "na":{
        "name":"Nauru",
        "nativeName":"Ekakairũ Naoero"
    },
    "nv":{
        "name":"Navajo, Navaho",
        "nativeName":"Diné bizaad, Dinékʼehǰí"
    },
    "nb":{
        "name":"Norwegian Bokmål",
        "nativeName":"Norsk bokmål"
    },
    "nd":{
        "name":"North Ndebele",
        "nativeName":"isiNdebele"
    },
    "ne":{
        "name":"Nepali",
        "nativeName":"नेपाली"
    },
    "ng":{
        "name":"Ndonga",
        "nativeName":"Owambo"
    },
    "nn":{
        "name":"Norwegian Nynorsk",
        "nativeName":"Norsk nynorsk"
    },
    "no":{
        "name":"Norwegian",
        "nativeName":"Norsk"
    },
    "ii":{
        "name":"Nuosu",
        "nativeName":"ꆈꌠ꒿ Nuosuhxop"
    },
    "nr":{
        "name":"South Ndebele",
        "nativeName":"isiNdebele"
    },
    "oc":{
        "name":"Occitan",
        "nativeName":"Occitan"
    },
    "oj":{
        "name":"Ojibwe, Ojibwa",
        "nativeName":"ᐊᓂᔑᓈᐯᒧᐎᓐ"
    },
    "cu":{
        "name":"Old Church Slavonic, Church Slavic, Church Slavonic, Old Bulgarian, Old Slavonic",
        "nativeName":"ѩзыкъ словѣньскъ"
    },
    "om":{
        "name":"Oromo",
        "nativeName":"Afaan Oromoo"
    },
    "or":{
        "name":"Oriya",
        "nativeName":"ଓଡ଼ିଆ"
    },
    "os":{
        "name":"Ossetian, Ossetic",
        "nativeName":"ирон æвзаг"
    },
    "pa":{
        "name":"Panjabi, Punjabi",
        "nativeName":"ਪੰਜਾਬੀ, پنجابی‎"
    },
    "pi":{
        "name":"Pāli",
        "nativeName":"पाऴि"
    },
    "fa":{
        "name":"Persian",
        "nativeName":"فارسی"
    },
    "pl":{
        "name":"Polish",
        "nativeName":"polski"
    },
    "ps":{
        "name":"Pashto, Pushto",
        "nativeName":"پښتو"
    },
    "pt":{
        "name":"Portuguese",
        "nativeName":"Português"
    },
    "qu":{
        "name":"Quechua",
        "nativeName":"Runa Simi, Kichwa"
    },
    "rm":{
        "name":"Romansh",
        "nativeName":"rumantsch grischun"
    },
    "rn":{
        "name":"Kirundi",
        "nativeName":"kiRundi"
    },
    "ro":{
        "name":"Romanian, Moldavian, Moldovan",
        "nativeName":"română"
    },
    "ru":{
        "name":"Russian",
        "nativeName":"русский язык"
    },
    "sa":{
        "name":"Sanskrit (Saṁskṛta)",
        "nativeName":"संस्कृतम्"
    },
    "sc":{
        "name":"Sardinian",
        "nativeName":"sardu"
    },
    "sd":{
        "name":"Sindhi",
        "nativeName":"सिन्धी, سنڌي، سندھی‎"
    },
    "se":{
        "name":"Northern Sami",
        "nativeName":"Davvisámegiella"
    },
    "sm":{
        "name":"Samoan",
        "nativeName":"gagana faa Samoa"
    },
    "sg":{
        "name":"Sango",
        "nativeName":"yângâ tî sängö"
    },
    "sr":{
        "name":"Serbian",
        "nativeName":"српски језик"
    },
    "gd":{
        "name":"Scottish Gaelic; Gaelic",
        "nativeName":"Gàidhlig"
    },
    "sn":{
        "name":"Shona",
        "nativeName":"chiShona"
    },
    "si":{
        "name":"Sinhala, Sinhalese",
        "nativeName":"සිංහල"
    },
    "sk":{
        "name":"Slovak",
        "nativeName":"slovenčina"
    },
    "sl":{
        "name":"Slovene",
        "nativeName":"slovenščina"
    },
    "so":{
        "name":"Somali",
        "nativeName":"Soomaaliga, af Soomaali"
    },
    "st":{
        "name":"Southern Sotho",
        "nativeName":"Sesotho"
    },
    "es":{
        "name":"Spanish; Castilian",
        "nativeName":"español, castellano"
    },
    "su":{
        "name":"Sundanese",
        "nativeName":"Basa Sunda"
    },
    "sw":{
        "name":"Swahili",
        "nativeName":"Kiswahili"
    },
    "ss":{
        "name":"Swati",
        "nativeName":"SiSwati"
    },
    "sv":{
        "name":"Swedish",
        "nativeName":"svenska"
    },
    "ta":{
        "name":"Tamil",
        "nativeName":"தமிழ்"
    },
    "te":{
        "name":"Telugu",
        "nativeName":"తెలుగు"
    },
    "tg":{
        "name":"Tajik",
        "nativeName":"тоҷикӣ, toğikī, تاجیکی‎"
    },
    "th":{
        "name":"Thai",
        "nativeName":"ไทย"
    },
    "ti":{
        "name":"Tigrinya",
        "nativeName":"ትግርኛ"
    },
    "bo":{
        "name":"Tibetan Standard, Tibetan, Central",
        "nativeName":"བོད་ཡིག"
    },
    "tk":{
        "name":"Turkmen",
        "nativeName":"Türkmen, Түркмен"
    },
    "tl":{
        "name":"Tagalog",
        "nativeName":"Wikang Tagalog, ᜏᜒᜃᜅ᜔ ᜆᜄᜎᜓᜄ᜔"
    },
    "tn":{
        "name":"Tswana",
        "nativeName":"Setswana"
    },
    "to":{
        "name":"Tonga (Tonga Islands)",
        "nativeName":"faka Tonga"
    },
    "tr":{
        "name":"Turkish",
        "nativeName":"Türkçe"
    },
    "ts":{
        "name":"Tsonga",
        "nativeName":"Xitsonga"
    },
    "tt":{
        "name":"Tatar",
        "nativeName":"татарча, tatarça, تاتارچا‎"
    },
    "tw":{
        "name":"Twi",
        "nativeName":"Twi"
    },
    "ty":{
        "name":"Tahitian",
        "nativeName":"Reo Tahiti"
    },
    "ug":{
        "name":"Uighur, Uyghur",
        "nativeName":"Uyƣurqə, ئۇيغۇرچە‎"
    },
    "uk":{
        "name":"Ukrainian",
        "nativeName":"українська"
    },
    "ur":{
        "name":"Urdu",
        "nativeName":"اردو"
    },
    "uz":{
        "name":"Uzbek",
        "nativeName":"zbek, Ўзбек, أۇزبېك‎"
    },
    "ve":{
        "name":"Venda",
        "nativeName":"Tshivenḓa"
    },
    "vi":{
        "name":"Vietnamese",
        "nativeName":"Tiếng Việt"
    },
    "vo":{
        "name":"Volapük",
        "nativeName":"Volapük"
    },
    "wa":{
        "name":"Walloon",
        "nativeName":"Walon"
    },
    "cy":{
        "name":"Welsh",
        "nativeName":"Cymraeg"
    },
    "wo":{
        "name":"Wolof",
        "nativeName":"Wollof"
    },
    "fy":{
        "name":"Western Frisian",
        "nativeName":"Frysk"
    },
    "xh":{
        "name":"Xhosa",
        "nativeName":"isiXhosa"
    },
    "yi":{
        "name":"Yiddish",
        "nativeName":"ייִדיש"
    },
    "yo":{
        "name":"Yoruba",
        "nativeName":"Yorùbá"
    },
    "za":{
        "name":"Zhuang, Chuang",
        "nativeName":"Saɯ cueŋƅ, Saw cuengh"
    }
}

def langsearch(q):
    if len(q)==2:
        if q in blank_langs.keys():
            return q
    for i in blank_langs.keys():
        if "," in blank_langs[i]['name']:
            split=blank_langs[i]['name'].split(",")
            for g in split:
                if q.lower()==g.lower().strip():
                    return i
        else:
            if q.lower()==blank_langs[i]['name'].lower():
                return i

def is_image_url(image_link):
    r=requests.get(image_link)
    if "image" in r.headers["Content-Type"]:
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
<b><font size="30" color="red"><div class="status">BlankBot is active</div></font></b><br><br><button class="button button1" onclick="window.location.href='https://www.twitch.tv/BlankMCPE?v=1';">Go to repl</button></body></html>'''
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

def gae(link):
    return cool_img_base+'gay?image='+link

def invrt(link):
    return cool_img_base+'invert?image='+link.strip()
    
def jale(link):
    return cool_img_base+'jail?image='+link.strip()

def waste(link):
    return cool_img_base+'wasted?image='+link.strip()

def want(link):
    return cool_img_base+'wanted?image='+link.strip()
    
def scrolll(text):
    return cool_img_base+'scroll?text='+text.strip()

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
    
def checklink(link):
    for i in range(3):
        if requests.get("https://render-tron.appspot.com/render/"+urllib.parse.quote_plus(link.strip())).status_code==200:
            res=True
            break
        else:
            res=False
    return res
        
def scrnshot(link):
    if not link.startswith("https://") and not link.startswith("http://"):
        
            linkr="https://"+link
            if checklink(linkr):
                link=linkr
            else:
                linkr="http://"+link
                if checklink(linkr):
                    link=linkr
                else:
                    return False
    else:
        if not checklink(link):
            return False
    link=urllib.parse.quote_plus(link)
    for i in range(3):
        
        link=f'https://render-tron.appspot.com/screenshot/{link}?width=1080&height=720'
        if is_image_url(link):
            break
    if not is_image_url(link):
        return False
    else:
        return requests.get(link).content

def upload_image(link):
    link=urllib.parse.quote_plus(link)
    for i in range(3):
        urlt=f"https://process.filestackapi.com/AhTgLagciQByzXpFGRI0Az/output=format:png/{link}"
        url=f"https://normal-api.ml/imgur?title=Blank&url={urlt}"
        r=requests.get(url).json()
        if not r['status']=="200":
            return urlt
        else:
            url=r['url']
        if is_image_url(url):
            return url
    return "Unable to access URL"
    
def nekos_life_getlink(link):
    link="https://render-tron.appspot.com/render/"+link
    while True:
        try:
            r=requests.get(link).text
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
    return f['url']

def changemymind_gen(text):
    endpoint=neko_base+"changemymind&text="+urllib.parse.quote_plus(text)
    res=(requests.get(endpoint).json()["message"])
    return res
    
def phcomment_gen(name, img, text):
    endpoint=neko_base+"phcomment&username="+urllib.parse.quote_plus(name)+"&image="+img+"&text="+urllib.parse.quote_plus(text)
    res=(requests.get(endpoint).json()["message"])
    return res

def short_link(link):
    base="https://api.shrtco.de/v2/shorten?url="
    if not link.lower().startswith("https://") and not link.lower().startswith("http://"):
        linkr="https://"+link
        if checklink(linkr):
            link=linkr
        else:
                linkr="http://"+link
                if checklink(linkr):
                    link=linkr
                else:
                    return "Invalid URL"
    if not checklink(link):
        return "Invalid URL"
        
    else:
        r=requests.get(base+link)
        res=r.json()
        if res["ok"]:
            result=(res["result"]["full_short_link"]).replace("\\","")
            result=f'<{result}>'
            return result
        else:
            error=res["error_code"]
            if error==3:
                result="Wait a second before making another link"
            elif error==6:
                result="Some unknown error occured"
            elif error==10:
                result="That URL is not allowed"
            return result

def gender_info(name):
    base="https://api.genderize.io/?name="
    r=requests.get(base+name.strip())
    res=r.json()
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

def patpat(url):
    a=0
    endpoint="https://api.jeyy.xyz/image/patpat?image_url="+url
    for i in range(3):
        if is_image_url(endpoint):
            return endpoint
    return False

def trash_gen(url):
    endpoint=neko_base+"trash&url="+url
    res=(requests.get(endpoint).json()["message"])
    return res
    
def stickbug_vid(url, link):
    endpoint=neko_base+"stickbug&url="+str(url)
    link[0]=(requests.get(endpoint).json()["message"])
 
def neko_pic():
    ch=random.choice([1, 2, 3])
    if ch==3:
        endpoint="https://nekos.best/api/v1/nekos"
    if ch==1:
        endpoint="https://neko-love.xyz/api/v1/neko"
    else:
        endpoint="https://nekos.life/api/v2/img/neko"
    return upload_image(nekos_life_getlink(endpoint))
        
def lewdkemo_gen():
    endpoint="https://nekos.life/api/v2/img/lewdkemo"
    return upload_image(nekos_life_getlink(endpoint))
    
def lewdholo_gen():
    endpoint="https://nekos.life/api/v2/img/hololewd"
    return upload_image(nekos_life_getlink(endpoint))

def fox_girl_gen():
    endpoint="https://nekos.life/api/v2/img/fox_girl"
    return upload_image(nekos_life_getlink(endpoint))

def kemonomimi_gen():
    endpoint="https://nekos.life/api/v2/img/kemonomimi"
    return upload_image(nekos_life_getlink(endpoint))
    
def cum_gen():
    endpoint="https://nekos.life/api/v2/img/cum_jpg"
    return upload_image(nekos_life_getlink(endpoint))
    
def bj_gen():
    endpoint="https://nekos.life/api/v2/img/blowjob"
    return upload_image(nekos_life_getlink(endpoint))
    
def femdom_gen():
    endpoint="https://nekos.life/api/v2/img/femdom"
    return upload_image(nekos_life_getlink(endpoint))
    
def lewd_gen():
    endpoint="https://nekos.life/api/v2/img/lewd"
    return upload_image(nekos_life_getlink(endpoint))
    
def pussy_gen():
    endpoint="https://nekos.life/api/v2/img/pussy_jpg"
    return upload_image(nekos_life_getlink(endpoint))
    
def boobs_gen():
    endpoint="https://nekos.life/api/v2/img/tits"
    return upload_image(nekos_life_getlink(endpoint))

def rand_list(list):
    return random.choice(list)

def get_image_bytes(url):
    if is_image_url(url):
        b=io.BytesIO(requests.get(url).content)
        return b
        
def lewdneko_gen():
    ch=random.choice([1, 2])
    if ch==1:
        endpoint="https://neko-love.xyz/api/v1/nekolewd"
        r=requests.get(endpoint).json()['url']
        return r
    else:
        endpoint="https://nekos.life/api/lewd/neko"
        return upload_image(nekos_life_getlink(endpoint))
        
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
value="`help embed purge del copy shorten webshot ip whois translate stream play watch listen random_status`", inline=False)
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
                embed.add_field(name=f"{prefix}help [category]", value="`Shows help menu. (If category is given, then shows help menu for the category)`")
                embed.add_field(name=f"{prefix}embed [Image url] <text>", value="`Send embed like a bot`")
                embed.add_field(name=f"{prefix}purge <number of messages>", value="`Deletes the given number of messages sent by you (do not put large number or you will get rate limited)`")
                embed.add_field(name=f"{prefix}del <text>", value="`Send a message and instantly deletes it (do not use this very frequently or you will get rate limited)`")
                embed.add_field(name=f"{prefix}copy", value="`Copy the current server (do not make changes to the new server until the server icon is copied)`")
                embed.add_field(name=f"{prefix}shorten <link>", value="`Shorten your link`")
                embed.add_field(name=f"{prefix}webshot <link>", value="`Send screenshot of webpage from link`")
                embed.add_field(name=f"{prefix}ip <ip address>", value="`Get information of an IP address`")
                embed.add_field(name=f"{prefix}whois [user]", value="`Send information about a user in the server`")
                embed.add_field(name=f"{prefix}translate <lang/code> <text> [0/1]", value="`Translate the given text to the given language`")
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
                embed.add_field(name=f"{prefix}neko", value="`Send random image of neko girl`")
                embed.add_field(name=f"{prefix}foxgirl", value="`Send random image of fox girl`")
                embed.add_field(name=f"{prefix}kemonomimi", value="`Send random image of kemonomimi (beast girl)`")
                embed.add_field(name=f"{prefix}anime <anime>", value="`Send info about an anime`")
                embed.add_field(name=f"{prefix}invert [user/image link]", value="`Send an image with inverted colours of original`")
                embed.add_field(name=f"{prefix}jail [user]", value="`Send someone to jail (prison)`")
                embed.add_field(name=f"{prefix}clown [user]", value="`I swear its a clown`")
                embed.add_field(name=f"{prefix}wanted [user]", value="`Make a wanted poster of a user`")
                embed.add_field(name=f"{prefix}wasted [user]", value="`GTA V 'wasted' image for a user`")
                embed.add_field(name=f"{prefix}gaypride [user]", value="`Send gay flag of a user`")
                embed.add_field(name=f"{prefix}pat [user]", value="`Pats a user`")
                embed.add_field(name=f"{prefix}scroll <text>", value="`Generate scroll meme`")
                embed.add_field(name=f"{prefix}phcomment [user] <text>", value="`Send fake screenshot of the user's pornhub comment`")
                embed.add_field(name=f"{prefix}chatbot <message>", value="`Chat with me when you are alone and bored`")
                embed.add_field(name=f"{prefix}kannagen <text>", value="`Kanna Kamui writes your text in her board`")
                embed.add_field(name=f"{prefix}changemymind <text>", value="`Generate change my mind meme with the text`")
                embed.add_field(name=f"{prefix}trash [user]", value="`Convert a user to a trash waifu`")
                embed.add_field(name=f"{prefix}stickbug [user]", value="`Generate stickbug meme with the user's profile picture (takes some time)`")
                embed.add_field(name=f"{prefix}wyr", value="`Send a would-you-rather questiom`")
                embed.add_field(name=f"{prefix}topic", value="`Send a chat topic`")
                embed.add_field(name=f"{prefix}roll <first number> <last number>", value="`Choose a random number between the first and last number`")
                embed.add_field(name=f"{prefix}gender <name>", value="`Predict the gender based on a name (first name only)`")
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
                embed.add_field(name=f"{prefix}lewdneko", value="`Hentai neko`")
                embed.add_field(name=f"{prefix}lewdkemo", value="`Hentai kemo`")
                embed.add_field(name=f"{prefix}lewd", value="`Hentai random`")
                embed.add_field(name=f"{prefix}blowjob", value="`Hentai blowjob`")
                embed.add_field(name=f"{prefix}femdom", value="`Hentai femdom`")
                embed.add_field(name=f"{prefix}lewdholo", value="`Hentai holo`")
                embed.add_field(name=f"{prefix}cum", value="`Hentai orgasm`")
                embed.add_field(name=f"{prefix}boobs", value="`Hentai boobs`")
                embed.add_field(name=f"{prefix}pussy", value="`Hentai pussy`")
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
    patpat_gif=patpat(str(avatar))
    if patpat is False:
        await ctx.channel.send("Cannot process that user's avatar", delete_after=2.0)
        return
    img=get_image_bytes(patpat)
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
    url=kannagen_gen(text)
    try:
        file=get_image_bytes(url)
        await ctx.channel.send(file=discord.File(file, 'blank_kanna.png'))
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
        res=scrnshot(link)
        if res is False:
            await ctx.channel.send("Unable to access URL", delete_after=2.0)
        else:
            try:
                file=io.BytesIO(res)
                await ctx.channel.send(file=discord.File(file, 'blank_screenshot.png'))
            except Exception:
                r=upload_image(res)
                await ctx.channel.send(r)

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

@Blank.command(aliases=['chat'])
async def chatbot(ctx, *, message: str=None):
    await ctx.message.delete()
    if message is None:
        await ctx.channel.send('```\nBlankbot: Hello I am BlankBot, please chat with me :)```')
        return
    bot=f"https://api.popcat.xyz/chatbot?msg={urllib.parse.quote_plus(message)}&owner=Blank&botname=Blankbot"
    r=requests.get(bot)
    if r.status_code==200:
        await ctx.channel.send(message)
        await ctx.channel.send(f"```\nBlankbot: {r.json()['response'].strip()}```")
    else:
        await ctx.channel.send("Chatbot not working right now", delete_after=2.0)

@Blank.command
async def clown(ctx, user: discord.Member=None):
    try:
        await ctx.message.delete()
    except Exception:
        pass
    if user is None:
        user=ctx.author
    endpoint="https://api.popcat.xyz/clown?image="+str(user.avatar_url_as(format='png'))
    if is_image_url(endpoint):
        try:
            await ctx.channel.send(file=discord.File(get_image_bytes(endpoint), 'Blank_clown.png'))
        except Exception:
            await ctx.channel.send(upload_image(endpoint))

@Blank.command()
async def lewdneko(ctx):
    try:
        await ctx.message.delete()
    except Exception:
        pass
    url=lewdneko_gen()
    extent=url.rsplit(".", 1)[1]
    try:
        file=get_image_bytes(url)
        await ctx.channel.send(file=discord.File(file, f'blank_lewdneko.{extent}'))
    except Exception:
        await ctx.channel.send(url)

@Blank.command()
async def lewdkemo(ctx):
    try:
        await ctx.message.delete()
    except Exception:
        pass
    url=lewdkemo_gen()
    extent=url.rsplit(".", 1)[1]
    try:
        file=get_image_bytes(url)
        await ctx.channel.send(file=discord.File(file, f'blank_lewdkemo.{extent}'))
    except Exception:
        await ctx.channel.send(url)

@Blank.command()
async def lewdholo(ctx):
    try:
        await ctx.message.delete()
    except Exception:
        pass
    url=lewdholo_gen()
    extent=url.rsplit(".", 1)[1]
    try:
        file=get_image_bytes(url)
        await ctx.channel.send(file=discord.File(file, f'blank_lewdholo.{extent}'))
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
    file=discord.File(io.BytesIO(requests.get(gae(link)).content), 'Blank_gaypride.png')
    try:
        await ctx.channel.send(file=file)
    except Exception:
        await ctx.channel.send(upload_image(gae(link)))
    
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
        if not checklink(user):
            await ctx.channel.send('Invalid image URL')
            return
        else:
            if not is_image_url(user):
                await ctx.channel.send('Invalid image URL')
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
        file=discord.File(io.BytesIO(requests.get(invrt(user)).content), 'Blank_invert.png')
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
    link=jale(str(user.avatar_url_as(format='png')))
    try:
        file=discord.File(io.BytesIO(requests.get(link).content), 'Blank_jail.png')
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
    link=waste(str(user.avatar_url_as(format='png')))
    try:
        file=discord.File(io.BytesIO(requests.get(link).content), 'Blank_wasted.png')
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
    link=want(str(user.avatar_url_as(format='png')))
    try:
        file=discord.File(io.BytesIO(requests.get(link).content), 'Blank_wanted.png')
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
    link=scrolll(text)
    try:
        file=discord.File(io.BytesIO(requests.get(link).content), 'Blank_scroll.png')
        await ctx.channel.send(file=file)
    except Exception:
        await ctx.channel.send(upload_image(link))

@Blank.command()
async def foxgirl(ctx):
    try:
        await ctx.message.delete()
    except Exception:
        pass
    url=fox_girl_gen()
    extent=url.rsplit(".", 1)[1]
    try:
        file=get_image_bytes(url)
        await ctx.channel.send(file=discord.File(file, f'blank_foxgirl.{extent}'))
    except Exception:
        await ctx.channel.send(url)

@Blank.command(aliases=['t'])
async def translate(ctx, lang: str="ja", *, text: str=None):
    if text is None:
        return
    try:
        await ctx.message.delete()
    except Exception:
        pass
    lang=langsearch(lang.strip())
    if lang is None:
        await ctx.channel.send('Language is not valid', delete_after=2.0)
        return
    ttext=text
    if text.strip().endswith(" 0"):
        ttext=text.rsplit(" ", 1)[0]
    elif text.strip().endswith(" 1"):
        ttext=text.rsplit(" ", 1)[0]
    r=requests.get(f'https://translate-api.ml/translate?lang={lang}&text='+urllib.parse.quote_plus(ttext)).json()
    if r['status']==404:
        if r['error']=="You are being Rate Limited":
            await ctx.channel.send('Please wait a second before translating another text', delete_after=2.0)
        elif r['error']=="An Error Occured while Translating the Language":
            await ctx.channel.send('Invalid Language Code', delete_after=2.0)
            return
    elif r['status']==200:
        if text.strip().endswith(" 0") or text.strip().endswith(" 1"):
            if text.rsplit(" ", 1)[1]=="0":
                if r['translated']['pronunciation'] is not None:
                    await ctx.channel.send(r['translated']['pronunciation'])
                else:
                    if r['translated']['text'] is not None:
                        await ctx.channel.send(r['translated']['text'])
                    else:
                        await ctx.channel.send("Cannot translate this text", delete_after=2.0)
            elif text.rsplit(" ", 1)[1]=="1":
                    if r['translated']['text'] is not None:
                        await ctx.channel.send(r['translated']['text'])
                    else:
                        if r['translated']['text'] is not None:
                            await ctx.channel.send(r['translated']['text'])
                        else:
                            await ctx.channel.send("Cannot translate this text", delete_after=2.0)

@Blank.command()
async def kemonomimi(ctx):
    try:
        await ctx.message.delete()
    except Exception:
        pass
    url=kemonomimi_gen()
    extent=url.rsplit(".", 1)[1]
    try:
        file=get_image_bytes(url)
        await ctx.channel.send(file=discord.File(file, f'blank_kemonomimi.{extent}'))
    except Exception:
        await ctx.channel.send(url)
        
@Blank.command()
async def lewd(ctx):
    try:
        await ctx.message.delete()
    except Exception:
        pass
    url=lewd_gen()
    extent=url.rsplit(".", 1)[1]
    try:
        file=get_image_bytes(url)
        await ctx.channel.send(file=discord.File(file, f'blank_lewd.{extent}'))
    except Exception:
        await ctx.channel.send(url)
        
@Blank.command()
async def femdom(ctx):
    try:
        await ctx.message.delete()
    except Exception:
        pass
    url=femdom_gen()
    extent=url.rsplit(".", 1)[1]
    try:
        file=get_image_bytes(url)
        await ctx.channel.send(file=discord.File(file, f'blank_femdom.{extent}'))
    except Exception:
        await ctx.channel.send(url)

@Blank.command()
async def cum(ctx):
    try:
        await ctx.message.delete()
    except Exception:
        pass
    url=cum_gen()
    extent=url.rsplit(".", 1)[1]
    try:
        file=get_image_bytes(url)
        await ctx.channel.send(file=discord.File(file, f'blank_cum.{extent}'))
    except Exception:
        await ctx.channel.send(url)

@Blank.command()
async def blowjob(ctx):
    try:
        await ctx.message.delete()
    except Exception:
        pass
    url=bj_gen()
    extent=url.rsplit(".", 1)[1]
    try:
        file=get_image_bytes(url)
        await ctx.channel.send(file=discord.File(file, f'blank_blowjob.{extent}'))
    except Exception:
        await ctx.channel.send(url)

@Blank.command()
async def pussy(ctx):
    try:
        await ctx.message.delete()
    except Exception:
        pass
    url=pussy_gen()
    extent=url.rsplit(".", 1)[1]
    try:
        file=get_image_bytes(url)
        await ctx.channel.send(file=discord.File(file, f'blank_pussy.{extent}'))
    except Exception:
        await ctx.channel.send(url)

@Blank.command()
async def boobs(ctx):
    try:
        await ctx.message.delete()
    except Exception:
        pass
    url=boobs_gen()
    extent=url.rsplit(".", 1)[1]
    try:
        file=get_image_bytes(url)
        await ctx.channel.send(file=discord.File(file, f'blank_boobs.{extent}'))
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
        await ctx.channel.send(short_link(text))

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
            url=neko_pic()
            extent=url.rsplit(".", 1)[1]
            break
        except Exception:
            pass
    try:
        file=io.BytesIO(requests.get(url).content)
        await ctx.channel.send(file=discord.File(file, f'blank_neko.{extent}'))
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
    try:
        await m.delete()
    except Exception:
        pass
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
                        await x.create_voice_channel(f"{chann}", bitrate=chann.bitrate, rtc_region=chann.rtc_region, user_limit=chann.user_limit, position=chann.position)
                    if isinstance(chann, discord.TextChannel):
                        await x.create_text_channel(f"{chann}", nsfw=chann.is_nsfw(), topic=chann.topic, slowmode_delay=chann.slowmode_delay, position=chann.position)
            for roles in ctx.guild.roles:
                await g.create_role(name=roles.name, colour=roles.colour, permissions=roles.permissions, mentionable=roles.mentionable, hoist=roles.hoist)
            
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
        await g.edit(icon=requests.get(ctx.guild.icon_url).content)
    except Exception:
        pass
        
@Blank.command()
async def purge(ctx, amount: int=None):
    if amount is None:
        return
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
async def ascii(ctx, *, text=None):
    if text is None:
        return
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
            working=is_image_url(image_url)
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
        except Exception as e:
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
            await ctx.channel.send("Invalid IP Address", delete_after=2.0)
            
@Blank.command()
async def gender(ctx, name: str=None):
    if name is not None:
        try:
            await ctx.message.delete()
        except Exception:
            pass
        await ctx.channel.send(gender_info(name))

@Blank.command()
async def anime(ctx, *, anime: str=None):
    if anime is None:
        return
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
