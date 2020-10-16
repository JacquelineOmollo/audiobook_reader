import pyttsx3
import PyPDF2

book = open("Data Structures and Algorithms Using Python.pdf", "rb")
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
bot = pyttsx3.init()
for i in range(20, pages):
    page = pdfReader.getPage(20)
    text = page.extractText()
    bot.say(text)
    bot.runAndWait()