#!/usr/bin/python3
import random
import string
i = 0
print("<========= PASSGEN =========>")
num = int(input("Number of characters : "))
res = ""
ans1 = input("Numbers ? (y/n)")
while ans1 != 'y' and ans1 != 'n' :
    ans1 = input("Sorry, try again.\nNumbers ? (y/n)")
ans2 = input("Special characters ? (y/n)")
while ans2 != 'y' and ans2 != 'n' :
    ans2 = input("Sorry, try again.\nSpecial characters ? (y/n)")
range = string.ascii_letters
if ans1 == 'y' :
    range += string.digits
if ans2 == 'y' :
    range += string.punctuation
while i < num :
    res += random.choice(range)
    i += 1
print("Generated the following string :\n" + res)
