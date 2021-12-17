# importing the library
import pyperclip as pc
import random
import string
import time

char_set = string.digits

def randomEmail(email):
    randomMail =email+ "+"+ ''.join(random.sample(char_set*6, 10)) +"@gmail.com"
    print(randomMail)
    return randomMail

def PermutateEmail4Ever(email,time):
    while(True):
        pc.copy(randomEmail(email))
        time.sleep(time)
