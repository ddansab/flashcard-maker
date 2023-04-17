#!/usr/bin/env python

from googletrans import Translator
import os
import random

translator = Translator()


def introStuff(fileName, categoryName):
    PATH = "new_files"
    if not os.path.exists(PATH):
        os.makedirs(PATH)
    num = random.randrange(1, 100)
    if not categoryName:
        w = open('new_files/{}_pleco.txt'.format(fileName), 'w')
        w.write("//Lazy Category Namer {}\n".format(num))
    else:
        w = open('new_files/{}_pleco.txt'.format(fileName), 'w')
        w.write("//{}\n".format(categoryName))


def zhengLongShuo(werdz):
    split = werdz.split(',')
    return split


def newLineSplit(werdz):
    split = werdz.split('\n')
    return split


def getTheWerdz(werdz, fName):
    for werd in werdz:
        transSF = werd.strip()
        transEN = translator.translate(transSF, dest='en')
        transLF = translator.translate(transSF, dest='zh-tw')
        transPY = translator.translate(transSF, dest='zh-cn')

        f = open('new_files/{}_pleco.txt'.format(fName), 'a')
        f.write("{}[{}]\t{}\t{}\n".format(
            transSF, transLF.text, transPY.pronunciation, transEN.text))
