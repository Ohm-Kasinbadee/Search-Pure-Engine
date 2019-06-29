from pythainlp import word_tokenize

text = "ทดสอบการตัดตำภาษาไทย"
proc = word_tokenize(text, engine='newmm')
print(proc)