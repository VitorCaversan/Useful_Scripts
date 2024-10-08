"""
workTimeCalc.py
João Vitor Caversan
Given a .pdf work time sheet, it sums the positive worked hours and subtracts the negative ones.
All the data is printed in the process.

Replace positiveIdentifier and negativeIdentifier with the respective strings that identify your
positive and negative balances.
"""

"""
Libraries to import:
pip install pdfplumber
OR
python3 -m pip install pdfplumber
"""

import sys
import pdfplumber

def read_pdf(file_path):
   with pdfplumber.open(file_path) as pdf:
      text = ""
      for page in pdf.pages:
         text += page.extract_text()
      return text

try:
   scriptname, source = sys.argv
except:
   print( """Invalid arguments passed. Usage:\npython3 scriptname.py file\path\without\white\spaces""")
   sys.exit()

fileContent = read_pdf(source)

positiveIdentifier = "Lancto Positivo Ban"
negativeIdentifier = "Lancto Negativo Ban"

positiveMins = 0
negativeMins = 0
totalMinutes = 0

for line in fileContent.split('\n'):
   if (line.find(positiveIdentifier) != -1):
      splitedLine = line.split(' ')
      for key, word in enumerate(splitedLine):
         if (word.find('Lancto') != -1):
            print(f"{splitedLine[key]} {splitedLine[key + 1]} {splitedLine[key - 1]}")
            time = splitedLine[key - 1]
            hours, minutes = map(int, time.split(':'))
            totalMinutes += hours * 60 + minutes
            positiveMins += hours * 60 + minutes
   elif (line.find(negativeIdentifier) != -1):
      splitedLine = line.split(' ')
      for key, word in enumerate(splitedLine):
         if (word.find('Lancto') != -1):
            print(f"{splitedLine[key]} {splitedLine[key + 1]} {splitedLine[key - 1]}")
            time = splitedLine[key - 1]
            hours, minutes = map(int, time.split(':'))
            totalMinutes -= hours * 60 + minutes
            negativeMins += hours * 60 + minutes

totalHours = totalMinutes // 60
remainingMins = totalMinutes % 60

positiveHours = positiveMins // 60
remainingPositiveMins = positiveMins % 60

negativeHours = negativeMins // 60
remainingNegativeMins = negativeMins % 60

print(f"\n\nPositive worked hours: {positiveHours:02}:{remainingPositiveMins:02}")
print(f"Negative worked hours: {negativeHours:02}:{remainingNegativeMins:02}")
print(f"Sum of worked hours: {totalHours:02}:{remainingMins:02}")
