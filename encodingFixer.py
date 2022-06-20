from ctypes import sizeof
import re
import os

# Finds and replaces all special characters in a // comment
def replace_2bars_SpecialChars(raw_text : str):
   return_text = str()
   firstLine = True

   for line in raw_text.split('\n'):
      if line.find('//') != -1:
         line = line.replace('á', 'a').replace('à', 'a').replace('ã', 'a').replace('â', 'a').replace('Á', 'A').replace('À', 'A').replace('Ã', 'A').replace('Â', 'A')
         line = line.replace('é', 'e').replace('ê', 'e').replace('É', 'E').replace('Ê', 'E')
         line = line.replace('í', 'i').replace('Í', 'I')
         line = line.replace('ó', 'o').replace('ô', 'o').replace('õ', 'o').replace('Ó', 'O').replace('Ô', 'O').replace('Õ', 'O')
         line = line.replace('ú', 'u').replace('Ú', 'U')
         line = line.replace('ç', 'c').replace('Ç', 'C')
         line = line.replace('°', 'graus')
         line = line.replace('±', '+ou-')
         line = line.replace('Ã§Ãµ', 'co')
         line = line.replace('A¡', 'a').replace('A£', 'a').replace('A¢', 'a').replace('Aƒ', 'A')
         line = line.replace('Aª', 'e').replace('A©', 'e')
         line = line.replace('tA­t', 'tit').replace('rA­m', 'rim').replace('nA­c', 'nic')
         line = line.replace('A³', 'o').replace('Aµ', 'o').replace('A”', 'O')
         line = line.replace('A§', 'c').replace('ח', 'c').replace('A‡', 'C')
         line = line.replace('חד', 'ca')
         line = line.replace('ב', 'a').replace('ד', 'a').replace('ג', 'a')
         line = line.replace('ם', 'i')
         line = line.replace('ף', 'o').replace('ץ', 'o')

      if firstLine == True:
         return_text += line
         firstLine = False
      else:
         return_text += '\n' + line   

   return return_text


# Finds and replaces all special characters within a /**/ comment
def replace_bars_star_SpecialChars(raw_text : str):
   return_text = ''
   found_start = False
   found_end = False
   firstLine = True

   for line in raw_text.split('\n'):
      work_line = line
      work_line = work_line.strip()

      if work_line[:5].find('/*') != -1:
         found_start = True
      
      if work_line.find('*/') != -1:
         found_end = True
      
      
      if found_start == True or found_end == True:
         line = line.replace('á', 'a').replace('à', 'a').replace('ã', 'a').replace('â', 'a').replace('Á', 'A').replace('À', 'A').replace('Ã', 'A').replace('Â', 'A')
         line = line.replace('é', 'e').replace('ê', 'e').replace('É', 'E').replace('Ê', 'E')
         line = line.replace('í', 'i').replace('Í', 'I')
         line = line.replace('ó', 'o').replace('ô', 'o').replace('õ', 'o').replace('Ó', 'O').replace('Ô', 'O').replace('Õ', 'O')
         line = line.replace('ú', 'u').replace('Ú', 'U')
         line = line.replace('ç', 'c').replace('Ç', 'C')
         line = line.replace('°', 'graus')
         line = line.replace('±', '+ou-')
         line = line.replace('Ã§Ãµ', 'co')
         line = line.replace('A¡', 'a').replace('A£', 'a').replace('A¢', 'a').replace('Aƒ', 'A')
         line = line.replace('Aª', 'e').replace('A©', 'e')
         line = line.replace('tA­t', 'tit').replace('rA­m', 'rim').replace('nA­c', 'nic')
         line = line.replace('A³', 'o').replace('Aµ', 'o').replace('A”', 'O')
         line = line.replace('A§', 'c').replace('ח', 'c').replace('A‡', 'C')
         line = line.replace('חד', 'ca')
         line = line.replace('ב', 'a').replace('ד', 'a').replace('ג', 'a')
         line = line.replace('ם', 'i')
         line = line.replace('ף', 'o').replace('ץ', 'o')

      if found_start == True and found_end == True:
         found_start = False
         found_end = False

      if firstLine == True:
         return_text += line
         firstLine = False
      else:
         return_text += '\n' + line  
   
   return return_text

def is_upper_case(letter : str):
   if 'Z' >= letter >= 'A':
      return True
   else:
      return False

def is_a_define(text : str):
   index = 0

   for letter in text:
      if (len(text) - 1) == index: break

      if is_upper_case(letter) and is_upper_case(text[index+1]):
         return True
      
      index += 1

   return False

def find_by_list(text : str ,tags: list):
   for tag in tags:
      if text.find(tag) != -1:
         return text.find(tag)

   return -1


# Where all the directory running, and file picking, happens
# Files Idiomas.h and Idiomas.c must be opened with windows 1252 encoding and then saved with utf-8 encoding
for root, direcs, files in os.walk(os.path.dirname(__file__)):
   for dir in direcs:
      currentDir = root + os.sep + dir
      #print(currentDir)
      for filename in os.listdir(currentDir):
         filePath = os.path.join(currentDir, filename)
         #print(filePath)
         if filePath.endswith(('Teclado.c', 'NavegacaoTela.c', 'TemplatesDesenho.c', 'ConfiguracoesPiloto.c')) == False:  
            if filePath.endswith(".h") or filePath.endswith(".c"):
               try:
                  if filePath.endswith(('DashboardComunicacao.c', 'MotorEletronico.c', 'ConfiguracoesAdubacao.c', 'ConfiguracoesMemoriaTela.c', 'ConfiguracoesPiloto.h', 'ConfiguracoesPulverizacao.c', 'ConfiguracoesPulverizacao.h', 'HorimetrosEquipTela.c', 'BalancaAD.c')):
                     fileContent = open(filePath, encoding='utf-8').read()
                  elif filePath.endswith(('Idiomas.c', 'Idiomas.h')):
                     fileContent = open(filePath, encoding='cp1252').read()
                  else:
                     fileContent = open(filePath).read()

                  fileContent = replace_bars_star_SpecialChars(fileContent)
                  fileContent = replace_2bars_SpecialChars(fileContent)

                  open(filePath, mode='w', encoding='utf-8').write(fileContent)
               except:
                  print('-----------------------' + filename)