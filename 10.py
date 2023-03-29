import re

inp = input("Enter string: ")
pal = ""
maxlen = 1

if(re.findall("^[a-zA-Z]*$", inp)):

    for i in range(len(inp)):
        str=inp[i]
        for j in range(i+1, len(inp)):
            str+=inp[j]
            if(str==str[::-1] and len(str)>maxlen):
                pal = str
                maxlen = len(pal)

    if(pal!=""):
        print(pal)
        print(maxlen)

else:
    print("Invalid input")