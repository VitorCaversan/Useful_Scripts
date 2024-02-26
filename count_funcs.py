#!/usr/bin/env python2
import os
import re
import sys

def getExternFunctions(headerFile: str) -> list:
   funcList = []
   for line in headerFile.split('\n'):
      if (line.find("extern") != -1):
         funcLine = line.split(' ')
         for word in funcLine:
            if (word.find('_') != -1):
               word = word.split("(")
               word = word[0]
               funcList.append(word)
               break

   return funcList

try:
   scriptname, source, base_file = sys.argv
except:
   print( """Invalid arguments passed. Usage:\n scriptname.py source-path base_file.h""")
   sys.exit()

externFuncs = []
codefiles = []
for root, dirnames, filenames in os.walk(source):
   for filename in filter(lambda s: (s.endswith(".c") or s.endswith(".h")) and
                                    not(s.endswith("MemoriaLegado.c") or s.endswith("MemoriaLegado.h")), filenames):
      if (filename.endswith(base_file)):
         filePath = os.path.join(root, filename)
         externFuncs = getExternFunctions(open(filePath).read())
      
      codefiles.append(os.path.join(root, filename))

occurrencesOfFuncs = [0] * len(externFuncs)
for file in codefiles:
   try:
      fileContent = open(file).read()
   except:
      fileContent = open(file, encoding='utf-8').read()
   for itr in range(len(externFuncs)):
      counter = fileContent.count(externFuncs[itr])
      if counter != 0:
         occurrencesOfFuncs[itr] += counter

print("\n\n Functions with only 1 or 2 occurrences:\n")
for itr in range(len(occurrencesOfFuncs)):
   if occurrencesOfFuncs[itr] < 3:
      print(externFuncs[itr] + "  :  " + str(occurrencesOfFuncs[itr]) + '\n')