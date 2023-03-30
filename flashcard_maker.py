#!/usr/bin/env python

from googletrans import Translator
from pathlib import Path
import random

while True:
    fName = input("Choose a new filename (no special characters): ").replace(" ", "_")
    if fName: break

catName = input("Choose a category name for your new flashcards: ")
translator = Translator()


def introStuff(fileName, categoryName):
    num = random.randrange(1, 100)
    if not categoryName:
        w = open('{}_pleco.txt'.format(fileName), 'w')
        w.write("//{} Monkey Butts\n".format(num))
    else:
        w = open('{}_pleco.txt'.format(fileName), 'w')
        w.write("//{}\n".format(categoryName))

def zhengLongShuo():
   with open(r'starter_file.txt', 'r') as werdz:
      data = werdz.read()
      data = data.replace(", ", "\n")

   with open(r'starter_file.txt', 'w') as werdz:
      werdz.write(data)


zhengLongShuo()

# get the characters from file
with open('starter_file.txt') as werdz:
    lines = werdz.readlines()

# loop through the file
def getTheWerdz():
    wait = '.'

    for line in lines:
	# pull character
        transSF = line.strip()
        transEN = translator.translate(transSF, dest='en')
        transLF = translator.translate(transSF, dest='zh-tw')
        transPY = translator.translate(line, dest='zh-cn')
    
        f = open('{}_pleco.txt'.format(fName), 'a')
        f.write("{}[{}]\t{}\t{}\n".format(transSF, transLF.text, transPY.pronunciation, transEN.text))
    
       	print(wait)
        wait += '.'

def doTheThing():
    introStuff(fName, catName)
    getTheWerdz()

doTheThing()
print("==========================")
print("All done! You can find `{}_pleco.txt` inside your {} folder.".format(fName, Path.cwd()))
print("Just Teams or email it to yourself, and upload it into Pleco.")
print("=========================")
