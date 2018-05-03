#!/usr/bin/python
# coding: utf-8
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import xlrd
chatterbot = ChatBot(
    'Norman',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database='./database.sqlite3')
chatterbot.set_trainer(ListTrainer)
book = xlrd.open_workbook("greeting.xlsx")
sh = book.sheet_by_index(0)
conversation=[]
for rx in range(sh.nrows):
    if not sh.cell_value(rowx=rx, colx=0).split()=="":
        conversation.append(sh.cell_value(rowx=rx, colx=0))
        print(sh.cell_value(rowx=rx, colx=0))
chatterbot.train(conversation)


def chat(inpt):
    a =chatterbot.get_response(inpt)
    return a
