# -*- coding: utf-8 -*-
"""Wordle.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Hb5dFxgcP-5lcAox1gxS9Afb8yHKzN24
"""

def GetWordList(universe):
  wordlist = []
  for x in universe:
    wordlist.append([i for i in x])
  return wordlist

def GetFrequency(wordlist):
  frequency = {}
  NumOfWords = len(wordlist)
  for x in wordlist:
    y = list(dict.fromkeys(x))
    for i in y:
      if i in frequency.keys():
        frequency[i] = frequency[i]+1
      else:
        frequency[i] = 1
  for i in frequency.keys():
    frequency[i] = frequency[i]/NumOfWords
  return frequency

def GetProbability(universe, wordlist, frequency):
  count = 0
  probab = {}
  for x in wordlist:
    y = list(dict.fromkeys(x))
    temp = 0
    for i in y:
      temp = temp+frequency[i]
    probab[universe[count]] = temp
    count = count+1
  return probab

def UpdateGreen(tracker, letter, pos):
  #print(letter, pos, "green")
  keylist = tracker.keys()
  for word in list(tracker):
    if(word[pos]!=letter):
      del tracker[word]
  return tracker

def UpdateYellow(tracker, letter, pos):
  #print(letter, pos, "yellow")
  keylist = tracker.keys()
  for word in list(tracker):
    if(word[pos]==letter):
      del tracker[word]
    elif(letter not in word):
      del tracker[word]
  return tracker  

def UpdateGrey(tracker, letter):
  #print(letter, 'grey')
  keylist = tracker.keys()
  for word in list(tracker):
    if(letter in word):
      del tracker[word]
  return tracker
  
def UpdateUniverse(universe, word, response):
  word = [x for x in word]
  tracker = {}
  for x in universe:
    tracker[x]=1
  for position in [0,1,2,3,4]:
    if(response[position]=='g'):
      tracker = UpdateGreen(tracker, word[position], position)
    elif(response[position]=='y'):
      tracker = UpdateYellow(tracker, word[position], position)
    else:
      tracker = UpdateGrey(tracker, word[position])
  universe = list(tracker.keys())
  return universe

universe = open("Universe.txt", "r")
universe = universe.read()
universe = universe.splitlines()
play = "yes"
attempt = 1
while(play=="yes"):
  wordlist = GetWordList(universe)
  freq = GetFrequency(wordlist)
  probab = GetProbability(universe, wordlist, freq)
  print("starting attempt ",attempt)
  probab = sorted(probab.items(), key=lambda x: x[1], reverse=True)
  print(probab)
  word = input("Input guess : ")
  result = input("Input result y/g/z : ")
  play = input("Do you want to continue yes/no :")
  attempt = attempt+1
  universe = UpdateUniverse(universe, word, result)
  print("end")