from tkinter import E
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
 
from pyrogram.types import ChatPermissions
 
import time
from time import sleep
import random
 
app = Client("my_account",
            api_id='10049060',
            api_hash='1483f2213eb453df4587a8bd9d37e95a'
)
 
 
# Команда type
@app.on_message(filters.command("t", prefixes=".") & filters.me)
def type1(_, msg):
    orig_text = msg.text.split(".t ", maxsplit=1)[1]

    text = orig_text
    tbp = "" # to be printed
    typing_symbol = "✍️"
 
    while(tbp != orig_text):
        try:
            msg.edit(tbp + typing_symbol)
            sleep(0.05) # 50 ms
 
            tbp = tbp + text[0]
            text = text[1:]
 
            msg.edit(tbp)
            sleep(0.02)
 
        except FloodWait as e:
            sleep(e.x)


veter = ['Затянулось', 'небо🥀', 'одеялом💔', 'да', 'День', 'чернее', 'ночи', 'солнца🌕', 'стало', 'мало🌒', 'нам👩‍❤️‍👨', 'Ветер😻', 'завывает', 'диким', 'воем',
        'облака', 'Сердце💔', 'тихо', 'плачет💔🥀', 'и', 'болит❤️‍🩹', 'но', 'как', 'Но', 'как', 'нам', 'не', 'хватало💔', 'на', 'двоих👫', 'одной', 'любви❤️',
        'Как', 'же', 'было', 'мало🥀', 'разжигать', 'огонь🔥', 'внутри❤️‍🔥',
        'Девочка', 'Джованна💔🥀', 'в', 'мире🌏', 'пустоты', 'и', 'лжи',
        'Она', 'Инь-Янь', 'искала', 'но', 'нашла', 'лишь', 'черный🖤', 'Инь'
        ]

@app.on_message(filters.command('v', prefixes='.') & filters.me)
def type(_,msg):
    for i in veter:
        try:
            msg.edit(i)
            sleep(0.7)

        except FloodWait as e:
            sleep(e.x)
    msg.edit("Creator: Ozodbek")


@app.on_message(filters.command("vzl", prefixes=".") & filters.me)
def hack(_,msg):
    x = 0 

    while x < 100:
        try:
            text = " Telegram accountni buzish ishlari boshladni..." + str(x) + "%"
            msg.edit(text)
            
            x += random.randint(1,3)
            sleep(0.01)

        except FloodWait as e:
            sleep(e.x)

    msg.edit('Telegram account buzildi✅')

javob = True
@app.on_message(filters.command('s', prefixes='.') & filters.me)
def spam(_,msg):    
    app.send_message("ssssss")

        



app.run()
