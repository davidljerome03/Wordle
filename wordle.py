import os
import time
import sys
import datetime

print("Welcome to Wordle")
workfile = open(f'guess.txt', 'w')
workfile.close()
workfile = open(f'square.txt', 'w')
workfile.close()



x = 0
guess = 0
file = open('wordoftheday.txt', 'r')
content = file.readlines()
startdate = '09/30/2025'
startday = datetime.datetime.strptime(startdate, "%m/%d/%Y").date()
todaydate = datetime.date.today()

delta = todaydate - startday
if todaydate > startday:
  x = delta.days
else:
  pass
  
# wordofthedayaw = 'robot'
wordofthedayaw = content[x]

wordofthedayaw = wordofthedayaw.strip('\n')

def wordle():
  if guess == 6:
    lost()
  writeFile = open(f'guess.txt', 'r')
  workFileContents = writeFile.read()
  print(workFileContents)
  writeFile.close()
  file = open("wordacceptablewords.txt")
  global search_word
  search_word = input("\033[0;37;48mEnter a five letter word: ").lower()
  if len(search_word) == 5:
    print("Answer accepted")
    if(search_word in file. read()):
        wordcheck()
    else:
      print("Word not acceptable")
      time.sleep(2)
      os.system('clear')
      wordle()
  else:
    print("Wrong, that has", len(search_word), "letters!")
    time.sleep(2)
    os.system('clear')
    wordle()


def wordcheck():
  global wordofthedayaw
  wordofthedayaw = content[x]
  word = search_word
  emptyword = ['','','','','']
  emptysquare = ['','','','','']



  print()
  print("You entered:")
  print(word)
  print()

  # yellowfile = open("yellow.txt", "r")
  # greenfile = open("green.txt", "r")
  # grayfile = open("gray.txt", "r")

  # print("The character(s) listed are in the word: ")
  # print(list(set(word).intersection(set(wordofthedayaw))))
  #print(f"wordofthedayaw: {wordofthedayaw}")
  answer = content[x].strip('\n')
  if word == str(answer):
    for i in range(5):
      if word[i] == wordofthedayaw[i]:
        emptysquare[i] = '\U0001F7E9'
      else:
        pass
    def listToString2(s): 
  
      # initialize an empty string
      str1 = "" 
      
      # traverse in the string  
      for ele in emptysquare: 
          str1 += ele
      
      # return string  
      return str1
      
    writeFile = open(f'square.txt', 'a')
    emptysquare = listToString2(emptysquare)
    writeFile.write(emptysquare)
    writeFile.write('\n')
    writeFile.close()
    for i in range(5):
      if word[i] == wordofthedayaw[i]:
        position = i
        new_character = '_'
        temp = list(wordofthedayaw)
        temp[position] = new_character
        wordofthedayaw = ''.join(temp)
        emptyword[i] = f'\033[1;32;40m {word[i]}'
      else:
        pass
        
    def listToString(s): 
    
      # initialize an empty string
      str1 = "" 
      
      # traverse in the string  
      for ele in emptyword: 
          str1 += ele
      
      # return string  
      return str1

    writeFile = open(f'guess.txt', 'a')
    emptyword = listToString(emptyword)
    writeFile.write(emptyword)   
    writeFile.write('\n')
    writeFile.close()
      
    won()
  else:
    writeFile = open(f'guess.txt', 'a')
  
    #green loop
    for i in range(5):
      if word[i] == wordofthedayaw[i]:
        position = i
        new_character = '_'
        temp = list(wordofthedayaw)
        temp[position] = new_character
        wordofthedayaw = ''.join(temp)
        emptyword[i] = f'\033[1;32;40m {word[i]}'
        position = i
        new_character = '-'
        temp = list(word)
        temp[position] = new_character
        word = ''.join(temp)
        emptysquare[i] = '\U0001F7E9'
      else:
        pass

    #yellow loop
    for i in range(5):
      new_wordofthedayaw = wordofthedayaw
      if word[i] in new_wordofthedayaw:
        emptyword[i] = f'\033[1;33;40m {word[i]}'
        emptysquare[i] = '\U0001F7E8'
      else:
        pass

    #gray loop
    for i in range(5):
      if word[i] == '-':
        pass
      else:
        if word[i] not in new_wordofthedayaw:
          emptyword[i] = f'\033[0;37;40m {word[i]}'
          emptysquare[i] = '\U00002B1B'
        else:
          pass

    def listToString(s): 
    
      # initialize an empty string
      str1 = "" 
      
      # traverse in the string  
      for ele in emptyword: 
          str1 += ele
      
      # return string  
      return str1

    def listToString2(s): 
  
      # initialize an empty string
      str1 = "" 
      
      # traverse in the string  
      for ele in emptysquare: 
          str1 += ele
      
      # return string  
      return str1
          
  emptyword = listToString(emptyword)
  writeFile.write(emptyword)   
  writeFile.write('\n')
  writeFile.close()

  writeFile = open(f'square.txt', 'a')
  emptysquare = listToString2(emptysquare)
  writeFile.write(emptysquare)
  writeFile.write('\n')
  writeFile.close()

  writeFile = open(f'guess.txt', 'r')
  workFileContents = writeFile.read()
  print(workFileContents)
  writeFile.close()
  
  option = 0
  while option != 'Y':
    option = input("\033[0;37;48m Are you ready for you next guess? Please put Y when ready:  ").capitalize()
  if option == 'Y':
    os.system('clear')
    global guess
    guess += 1
    wordle()

def won():
  x = 0
  startdate = '03/03/2022'
  startday = datetime.datetime.strptime(startdate, "%m/%d/%Y").date()
  todaydate = datetime.date.today()
  
  delta = todaydate - startday
  if todaydate > startday:
    x = delta.days
  else:
    pass
  print("You got the word.")
  print("You won!!")
  print()
  writeFile = open(f'square.txt', 'r')
  workFileContents = writeFile.read()
  with open("guess.txt", 'r') as fp:
    guess2 = len(fp.readlines())
  print(f"Wordle #{x} {guess2}/6")
  print(workFileContents)
  writeFile.close()
  sys.exit()

def lost():
  x = 0
  file = open('wordoftheday.txt', 'r')
  content = file.readlines()
  startdate = '03/03/2022'
  startday = datetime.datetime.strptime(startdate, "%m/%d/%Y").date()
  todaydate = datetime.date.today()
  
  delta = todaydate - startday
  if todaydate > startday:
    x = delta.days
  else:
    pass
  file = open('wordoftheday.txt')
  content = file.readlines()
  print('Sorry you ran out of attempts')
  print(f"The word was {content[x]}")
  writeFile = open(f'square.txt', 'r')
  workFileContents = writeFile.read()
  step = 2
  guess2 = 0
  with open("guess.txt") as handle:
    for lineno, line in enumerate(handle):
        if lineno % step == 0:
            guess2 += 1
  print(f"Wordle #{x} X/6")
  print(workFileContents)
  writeFile.close()
  sys.exit()

wordle()