# -*- coding: utf-8 -*-
from configparser import ConfigParser

import numpy as np
import telebot
import telegram
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot import types

import config
from bot import tests

TELEGRAM_TOKEN = '1743070206:AAEFKsDl0kNfo6zZhoknJSzyZ2VDKBZqhK8'

bot = telebot.TeleBot(TELEGRAM_TOKEN)
lst = np.zeros(30)
arr = config.test
arr_ans = config.questions
test = tests.test
lst1 = np.zeros(15)

@bot.message_handler(commands=['start'])
def start_test(message):
    bot.send_message(message.chat.id, text=config.rus_start, reply_markup=trans_markup('star_'))

@bot.message_handler(commands=['info'])
def start_test(message):
    bot.send_message(message.chat.id, text=config.rus_info, reply_markup=trans_markup('info_'))

@bot.message_handler(commands=['help'])
def start_test(message):
    bot.send_message(message.chat.id, text=config.rus_help, reply_markup=trans_markup("help_"))

@bot.message_handler(commands=['tests'])
def start_test(message):
    bot.send_message(message.chat.id, text=tests.rus_test, reply_markup=trans_markup("test_"))

def trans_markup(st):
    markup = types.InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text="Перевести на русский", callback_data=st + 'r'))
    markup.add(InlineKeyboardButton(text="Translate in English", callback_data=st + 'e'))
    if st == 'star_':
        markup.add(InlineKeyboardButton(text="Start test", callback_data='start_'))
    if st == 'test_':
        markup.add(InlineKeyboardButton(text="Start test", callback_data='it'))
    return markup




@bot.message_handler(content_types=["text"])
def message_handler(message):
    bot.send_message(message.chat.id, text=config.rus_help, reply_markup=trans_markup("help_"))

def gen_markup(i):
    markup = InlineKeyboardMarkup()

    if i < 10:
        for j in range(4):
            st = arr[i][j+1]
            markup.add(InlineKeyboardButton(st, callback_data="ans0{}{}".format(i, j)))
    else:
        for j in range(4):
            st = arr[i][j+1]
            markup.add(InlineKeyboardButton(st, callback_data="ans{}{}".format(i, j)))
    return markup

def gen_true_markup(i, c):
    markup = types.InlineKeyboardMarkup()
    if c == arr[i][5]:
        em = ' ✅'
        lst[i] = 1
    else:
        em = ' ❌'
        lst[i] = 0
    for j in range(4):
        st = arr[i][j + 1]
        if j == c:
            markup.add(InlineKeyboardButton(text=st+em, callback_data="a{}".format(i)))
        else:
            markup.add(InlineKeyboardButton(text=st, callback_data="a{}".format(i)))
    return markup
def gen_q(i):
    m = i
    stri = arr[m]
    return stri

def get_rez():
    strin = "aaa"
    arr = lst
    rez = np.sum(arr)/len(arr) * 100
    if rez <= 16:
        strin = config.A1
    elif 17 <= rez <= 32:
        strin = config.A2
    elif 33 <= rez <= 50:
        strin = config.B1
    elif 51 <= rez <= 67:
        strin = config.B2
    elif 68 <= rez <= 84:
        strin = config.C1
    elif 85 <= rez <= 100:
        strin = config.C2
    return strin

def get_eng_rez():
    strin = "aaa"
    arr = lst
    rez = np.sum(arr) / len(arr) * 100
    if rez <= 16:
        strin = config.A1_E
    elif 17 <= rez <= 32:
        strin = config.A2_E
    elif 33 <= rez <= 50:
        strin = config.B1_E
    elif 51 <= rez <= 67:
        strin = config.B2_E
    elif 68 <= rez <= 84:
        strin = config.C1_E
    elif 85 <= rez <= 100:
        strin = config.C2_E
    return strin

def gen_test(i):
    m = i
    stri = test[m]
    return stri

def gen_markup_t(i):
    markup = InlineKeyboardMarkup()
    markup.row_width = 4
    if i < 10:
        for j in range(4):
            st = test[i][j+1]
            markup.add(InlineKeyboardButton(st, callback_data="tns0{}{}".format(i, j)))
    else:
        for j in range(4):
            st = test[i][j+1]
            markup.add(InlineKeyboardButton(st, callback_data="tns{}{}".format(i, j)))
    return markup


def gen_true_markup_t(i, c):
    markup = types.InlineKeyboardMarkup()
    if c == test[i][5]:
        em = ' ✅'
        lst1[i] = 1
    else:
        em = ' ❌'
        lst1[i] = 0
    for j in range(4):
        st = test[i][j + 1]
        if j == c:
            markup.add(InlineKeyboardButton(text=st+em, callback_data="a{}".format(i)))
        else:
            markup.add(InlineKeyboardButton(text=st, callback_data="a{}".format(i)))
    return markup

def get_rez_t():
    strin = "aaa"
    arr = lst1
    rez = np.sum(arr) / len(arr) * 100
    if rez <= 33:
        strin = tests.rez_33_rus
    elif 34 <= rez <= 66:
        strin = tests.rez_66_rus
    elif 67 <= rez <= 100:
        strin = tests.rez_100_rus
    return strin

def get_rez_t_eng():
    strin = "aaa"
    arr = lst1
    rez = np.sum(arr) / len(arr) * 100
    if rez <= 33:
        strin = tests.rez_33_eng
    elif 34 <= rez <= 66:
        strin = tests.rez_66_eng
    elif 67 <= rez <= 100:
        strin = tests.rez_100_eng
    return strin


qu = tests.qu

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            chat_id = call.message.chat.id
            message_id = call.message.message_id
            if 'start' in call.data:
                bot.send_message(call.message.chat.id, text=gen_q(0), reply_markup=gen_markup(0))

            if 'it' in call.data:
                bot.send_message(call.message.chat.id, text=gen_test(0), reply_markup=gen_markup_t(0))
            if 'tns' in call.data:
                st = call.data
                if int(st[3]) == 0:
                    num = int(st[4])
                else:
                    num = int(st[3]) * 10 + int(st[4])
                bot.edit_message_text(
                        chat_id=chat_id,
                        message_id=message_id,
                        text=qu[num],
                        reply_markup=gen_true_markup_t(num, int(st[5])),
                        parse_mode=telegram.ParseMode.HTML)
                if num == 14:
                    rez = "Your result: {}/{} - {:.2f}%\n\n".format(int(np.sum(lst1)),len(lst1),np.sum(lst1)/len(lst1)*100)
                    bot.send_message(call.message.chat.id, text=rez)
                    bot.send_message(call.message.chat.id, text=get_rez_t(), reply_markup=trans_markup('rest_'),
                                     parse_mode=telegram.ParseMode.HTML)
                else:
                    bot.send_message(call.message.chat.id, text=gen_test(num+1), reply_markup=gen_markup_t(num+1))
            if 'ans' in call.data:
                st = call.data
                if int(st[3]) == 0:
                    num = int(st[4])
                else:
                    num = int(st[3]) * 10 + int(st[4])
                bot.edit_message_text(
                        chat_id=chat_id,
                        message_id=message_id,
                        text=arr_ans[num],
                        reply_markup=gen_true_markup(num, int(st[5])),
                        parse_mode=telegram.ParseMode.HTML)
                if num == 29:
                    rez = "Your result: {}/{} - {:.2f}%\n\n".format(int(np.sum(lst)),len(lst),np.sum(lst)/len(lst)*100)
                    bot.send_message(call.message.chat.id, text=rez)
                    bot.send_message(call.message.chat.id, text=get_rez(), reply_markup=trans_markup('resu_'),
                                     parse_mode=telegram.ParseMode.HTML)
                else:
                    bot.send_message(call.message.chat.id, text=gen_q(num+1), reply_markup=gen_markup(num+1))
            if 'help' or 'star' or 'info' or 'resu' or 'rest' in call.data:
                st = ""
                mes = ""
                if 'help' in call.data:
                    if call.data[5] == 'e':
                        mes = config.eng_help
                    elif call.data[5] == 'r':
                        mes = config.rus_help
                    st = 'help_'
                elif 'star' in call.data:
                    if call.data[5] == 'e':
                        mes = config.eng_start
                    elif call.data[5] == 'r':
                        mes = config.rus_start
                    st = 'star_'
                elif 'info' in call.data:
                    if call.data[5] == 'e':
                        mes = config.eng_info
                    elif call.data[5] == 'r':
                        mes = config.rus_info
                    st = 'info_'
                elif 'test' in call.data:
                    if call.data[5] == 'e':
                        mes = tests.eng_test
                    elif call.data[5] == 'r':
                        mes = tests.rus_test
                    st = 'test_'
                elif 'resu' in call.data:
                    if call.data[5] == 'e':
                        mes = get_eng_rez()
                    elif call.data[5] == 'r':
                        mes = get_rez()
                    st = 'resu_'
                elif 'rest' in call.data:
                    if call.data[5] == 'e':
                        mes = get_rez_t_eng()
                    elif call.data[5] == 'r':
                        mes = get_rez_t()
                    st = 'rest_'

                bot.edit_message_text(
                        chat_id=chat_id,
                        message_id=message_id,
                        text=mes,
                        reply_markup=trans_markup(st),
                        parse_mode=telegram.ParseMode.HTML)

    except Exception as e:
        print(repr(e))

bot.polling(none_stop=True)