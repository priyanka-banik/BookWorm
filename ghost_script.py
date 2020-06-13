from wand.image import Image as wi
import pytesseract
from gtts import gTTS

pdf = wi(filename="CS_Computer-Science-and-Information-Technology.pdf", resolution=300)
pdfimage = pdf.convert("jpeg")
i = 1
for img in pdfimage.sequence:
    page = wi(image=img)
    page.save(filename=str(i)+".jpg")
    i += 1


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
j = 1
dir_name = "C:\\Users\\Admin\\Documents\\"
mytext =""

while j < i:
    file_name = str(j) + ".jpg"
    mytext += pytesseract.image_to_string(dir_name+file_name)
    j=j+1

tts = gTTS(text=mytext, lang='en')
tts.save("syllabus.mp3")