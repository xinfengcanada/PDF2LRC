from PyPDF2 import PdfReader
from tkinter.filedialog import *
import os

# Extract text from pdf，ignoring header and footer
# book = askopenfilename()
book = open('/home/dd/Documents/Library/How to be better at almost everything learn anything quickly, stack your skills, dominate (Flynn, Pat) (z-lib.org).pdf','rb')
reader = PdfReader(book)
print(reader.numPages)
full_text =""
# outbook = asksaveasfilename()
# print(outbook)
# textf = open(outbook,'w',encoding='utf-8')
textf = open('/home/dd/Desktop/test_project/PDF2LRC/text.txt','r+',encoding='utf-8')
for num in range(9,138):
    page = reader.pages[num]    
    text_body = page.extract_text()
    text_body = " ".join(text_body.splitlines())
    # 独句成行
    text_body = text_body.replace("?”","?”\n")
    text_body = text_body.replace("? ","?\n")
    text_body = text_body.replace(".”",".”\n")
    text_body = text_body.replace(". ",".\n")
    text_body = text_body.replace("; ",";\n")
    # 去除多余空格
    text_body = text_body.replace("’ ","’")
    text_body = text_body.replace(" ’","’")
    text_body = text_body.replace(" .",".")
    text_body = text_body.replace(" ,",",")
    text_body = text_body.replace("  "," ")
    full_text += text_body
textf.write(full_text)
for line in textf:
    print(line)
textf.close()
print("Done")
