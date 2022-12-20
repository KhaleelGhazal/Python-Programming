import PyPDF2, pyttsx3
link = input("Enter the url for your PDF: ")
def read_file(link):
  filepath = open(link, "rb")
  file_reader = PyPDF2.PdfFileReader(filepath)
  sorosoke = pyttsx3.init()
  for pages in range(file_reader.numPages):
      text = file_reader.getPage(pages).extractText()
      sorosoke.say(text)
      sorosoke.runAndWait()
  sorosoke.stop()
