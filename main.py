import pyttsx3
import PyPDF2
import sys

if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")

bot = pyttsx3.init()
book = open("Data Structures and Algorithms Using Python.pdf", "rb")
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)

'''Rate'''
rate = bot.getProperty("rate")
print(rate)
bot.setProperty("rate", 125)

'''Voice'''
voices = bot.getProperty("voices")
print(voices)
bot.setProperty("voice", voices[1].id)

for i in range(20, pages):
    page = pdfReader.getPage(20)
    text = page.extractText()
    bot.say(text)
    bot.runAndWait()





