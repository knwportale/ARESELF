import os
os.system("cls && title Checking.... && color b")
active = False
print("Welcome! Checking...")
if os.path.exists('insert_token.txt') == False:
  print("Insert the token to the file INSERT_TOKEN.txt\nAnd restart the programm")
  open('insert_token.txt', 'w')
  while True:
    a = 0
    a + 1
import random
import asyncio
import discord
import requests
from discord.ext import commands
client = commands.Bot(command_prefix = ";", help_command=None, self_bot = True)
guild  = client.get_guild(id)
my_array = ["еблан, ", "у твоей матери ребенок", "насколько же ты", "ты униженный и попущеный", "слышь ты блядь, уебан.", "слитое уродское создание", "cын еблана отзовись.", "ау блядь уебище.", "блядское создание ", "ущербный настолько что твое призвание", "мамонт ебаный", "проведи себе вскрытие нахуй, ты", "ты смешной, долбоящер", "Что ты несешь долбаебище ", "Ау блядь, ", "Дочка прошмандовки, "]
osk2 = [" шлюха,", " хуисосище ебанное", " пидорасня", " животное", " мальчик без хуя", " спидозная залупа", " ущербное создание", " хуежуйка ебаная", " отмороженный ", " подзалупный творожочек", " долбаебическая свинья", " сын шлюхи", " ребенок двух пидорасов", " терпилоид чисто", " сын детственника", " сын овцы", " дилдосос", " порноактер из категории гей порно", " обсос", " подсос своего бати", " жертва аутизма", " абортышь", "  даун чисто", " недоразвитое создание", " ебучая ошибка природы", " дитя ебаное", " долбаеб", " оффни свой ебасос", " подсос всех кто мужского пола ебать", " чисто уебище ебаное блядь", " дырявый отморозок", " у тебя четыре хуя в жопе, хватит", " самоунижается чисто", "чисто ребенок гноя блядь", " какого хуи сосать уеба", " гнойная хуйня", " ущербный подсос ебать ахахаа", " порвало тебя да,"]
osk3 = [" гандопляс ебаный", " сын джастнаникса и дочь итскекофа ", " безмамное чудище", " слитое уродское создание", " переебанный отцами", " бомж", ", позови мать проститутку уебище", " про тебя принято называть животным, потому-что ты отсталый долбаеб нахуй,", " хуйло ебанное", " у тебя очко растянуто настолько, что туда влезает ебанный вентилятор нахуй", " шалашовка пиздочесанная", " ебучий хуебес", ",  разьебали бедного нахуй.", " уркодроченый пидорас озабоченых пенсионеров блядь. ", " блядота", " клиторосос ебучий",  " пидораст конченый", " сын залупы", " чисто мальчик гей нахуй", " выебистый пёс", " иди матери поплачь", " спермаглот ебаный", " подсос больших хуев", " иди матери пожалуйся чтоле", " сын куколда и проститутки", " у тебя в очке уже вазелиновые железы образовались, уебище,",  " ты при виде плетки сразу раком встаешь", " хватит высирать свою хуйню,", " дитя чернобыля", " хватит пастить уебок", " хватит выебываться, раб, без еды останешься, гандон", " ты при виде омего члена подставляешь свой рот, омежка ебаная", " твою мать выебали свиньи, видишь результат, хуйлушка"]
osk4 = [". Вообще нахуя ты так с отцом разговариваешь", ', че замолк сын чудовища', ". Я бы тебя отпиздил, хуесос", ", че молчим", ", давай, метни стрелочку, лучница ебаная", " попизди на меня еще, хуесоска :)", " :heart:", " сразу рот прирыл", " с хуями во рту говорить не можешь? Псина", ", что молчишь, жертва двух озабоченых подростков и бутылки водки", ". И вообще ты жертва аборта", ". Давай, голос, пёс.", ". Че блядь, погавкал и все?", "мы тебя по кругу пускали, чорт", ", я тебя палкой хуярил", ", мать твоя видя мой огромный член течет, уебище", ". Твоя мать под моим столом кстати", ". Я тебя елдаком по голове уебашил", ". Ты - одноклеточное существо.", ". Кринжовый хуеплет", ". Запомни нахуй, я - твой хозяин, а ты секс-рабыня", " хули ты мне сосать перестал, я не разрешал нахуй", ", кстати я тебе команду голос не давал, хули пиздишь уеба", ". Я слышал твоя мать элитная шлюха, попроси ее заскочить ко мне, давно не ебались", ", я твоему бате шуруп в голову закрутил", ", я из волос твоей жирной мамаши самокрутку сделал", ", дочка двух инвалидов ору"]
ban_answers = ["Да", "Нет", "Хо-хо-хо"]
ball_answers = ["Незнаю", "Возможно", "Да", "Скорее всего да, чем нет", "Скорее всего нет", "Спроси еще разок"]
@client.event
async def on_ready():
    print("Loading...")
    os.system("cls && color c")
    await asyncio.sleep(0.2)
    os.system("title A\ ")
    await asyncio.sleep(0.3)
    os.system("title Ar\ ")
    await asyncio.sleep(0.2)
    os.system("title Are\ ")
    await asyncio.sleep(0.2)
    os.system("title Ares\ ")
    await asyncio.sleep(0.3)
    os.system("title Arese\ ")
    await asyncio.sleep(0.2)
    os.system("title Aresel\ ")
    await asyncio.sleep(0.2)
    os.system("title Areself\ ")
    await asyncio.sleep(0.2)
    os.system("title Areself \ ")
    await asyncio.sleep(0.2)
    os.system("title Areself / v0.2 \ SelfBot")
    os.system("color c")
    print("""
                              ___    ____  ___________ ________    ______
                             /   |  / __ \/ ____/ ___// ____/ /   / ____/     Developed by Know
                            / /| | / /_/ / __/  \__ \/ __/ / /   / /_         with love <3
                           / ___ |/ _, _/ /___ ___/ / /___/ /___/ __/    
                          /_/  |_/_/ |_/_____//____/_____/_____/_/            areself.ml
                                      **  Version : 1.0  **
                                        """)
################ S  E  T  T  I  N  G S #######################
token = open('insert_token.txt', 'r').readline()
################ B  U  L  L  I  N  G  ########################
active = True
@client.command()
async def bull_start(ctx):
    await ctx.message.delete()
    for active in False:
        await ctx.send(random.choice(my_array) + random.choice(osk2) + random.choice(osk3) + random.choice(osk3) + random.choice(osk4))
        print("LOG: Bullying sended!")
        asyncio.sleep(2)

@client.command()
async def bull_off(ctx):
    await ctx.message.delete()
    print("LOG: Bulling stopped")
    active = False
################ F  U  N  ########################
@client.command()
async def ben(ctx, *, question):
    await ctx.message.delete()
    ban_answer = random.choice(ban_answers)
    await ctx.send(f"""
```ansi
[2;37mВы задали вопрос бэну:[0m
[2;34m{question}

[2;37mОтвет Бэна:[0m[2;34m
{ban_answer}
[0m
```
""")
@client.command()
async def ball(ctx, *, question):
    await ctx.message.delete()
    ball_answer = random.choice(ball_answers)
    await ctx.send(f"""
```ansi
[2;37mВы задали вопрос и потрясли шар:[0m
[2;34m{question}

[2;37mНа шаре написано:[0m[2;34m
{ball_answer}
[0m
```
""")
@client.command()
async def say(ctx, settings, *, message):
    await ctx.message.delete()
    if settings != "random" or "not":
      print("READ: Say has 2 types. 1 - random (;say random example > example [99999]) or not (just message).")
    if settings == "random":
      await ctx.send(message + " [" + str(random.randint(9999,99999)) + "]")
    if settings == "not":
      await ctx.send(message)
################ A  B  U  S  E  ########################
@client.command()
async def delchannels(ctx):
   print("LOG: Deleting all channels on server")
   await ctx.message.delete()
   for channel in ctx.guild.channels: # iterating through each guild channel
      await channel.delete()
      print("LOG: Deleted Channel.\n" + "     Channel Name: " + str(channel))
@client.command()
async def spam(ctx, number, *, text):
   await ctx.message.delete()
   print("LOG: Started spaming...")
   for channel in ctx.guild.channels: # iterating through each guild channel
     for i in range(int(number)):
       await ctx.send(str(text) + " [" + str(random.randint(1000,9999)) + "]")
       print("LOG: Spam sended")
       asyncio.sleep(1)
##################  H  E  L  P ###################
@client.command()
async def help(ctx):
  await ctx.message.delete()
  await ctx.send("""```ansi
[2;33m╭😈╮[0m  [2;31m𝙰  𝚁  𝙴  𝚂  𝙴  𝙻  𝙵[0m
[2;31m╰👿╯[0m [2;33m 𝙿  𝚁  𝙴  𝙼  𝙸  𝚄  𝙼
[0m
[2;30m    -  Prefix:[0m [1;2m[1;31m;
[0m[0m[2;30m    -  Developed by:[0m [1;2m[1;31mKnow#4463[0m[0m

[2;31m[ 🤬 ][0m    [2;31m 𝙱  𝚄  𝙻  𝙻  𝙸  𝙽  𝙶[0m
[2;30m[  +  ][0m      [2;34m< bull_start >[0m | [2;32mStart bulling[0m
[2;30m[  +  ] [0m     [2;34m< bull_off >[0m | [2;31mOff bulling

[  ❗  ]      𝙰  𝙱  𝚄  𝚂  𝙴
[2;30m[  +  ] [0m[2;31m     [0m[2;34m< spam [2;42m[2;41m[2;40m[2;36m<x>[0m[2;34m[2;40m[0m[2;34m[2;41m[0m[2;34m[2;42m[0m[2;34m [2;40m[2;30m[0m[2;34m[2;40m[0m[2;34m[2;36m[2;40m<text>[0m[2;36m [0m[2;34m>[0m | [2;31mSpam [2;33mx[0m[2;31m messages
[0m[2;30m[  +  ] [0m     [2;34m< delchannels >[0m | [2;31mDelete [2;34mall channels[0m[2;31m on the server
[0m[2;30m[  +  ] [0m     [2;34m< nuke >[0m | [2;31mCrash discord server
[0m[2;30m[  +  ] [0m     [2;34m< token_nuke >[0m | [2;31m!!![0m [2;31mKill this account !!!
[0m
[2;31m[  ❗  ]      𝙵  𝚄  𝙽
[0m[2;30m[  +  ] [0m     [2;34m< ben [2;40m[2;36m<text>[0m[2;34m[2;40m[0m[2;34m >[0m | [2;31mCall to ban
[0m[2;30m[  +  ] [0m     [2;34m< ball [2;40m[2;36m<text[0m[2;34m[2;40m[0m[2;34m[2;40m>[0m[2;34m[0m [2;34m>[0m | [2;31m8ball[0m
[0m[2;30m[  +  ] [0m     [2;34m< say [2;40m[2;36m<random/not> [2;40m[2;36m<text>[0m[2;34m[2;40m[0m[2;34m >[0m | [2;31mSay

```""")
##error fix##
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound ):
        print("LOG: Command not exist!")
        await ctx.message.delete()


client.run(token, bot = False) #mammoth's token
