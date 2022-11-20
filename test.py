import sqlite3
from identification import *
import sys

conn = sqlite3.connect('my_DB.db')
cur = conn.cursor()
id = 2
cur.execute("""SELECT CB,code_pin FROM utilisateurs WHERE id=?""", (id,))
response = cur.fetchone()
response1 = list(response)
print(response1)

def compare(a,b):
    print(a)
    print(b)
    if a==b:
        print("toto")
    else:
        sys.exit()
        
d = callbackFunc()
print(d)
question = list(d)
print(question)
#compare(question,response1)