chars = input("Enter characters separated by a space: ").split()
lucky = int(input("Enter lucky number: "))
length = int(input("Enter string length: "))
charval = {}

for x in chars:
    if(x.islower()):
        charval[x]=ord(x)-96
    else:
        charval[x]=ord(x)-64

comb = []

def combinations(chars, str, n, k):
    if (k==0) :
        comb.append(str)
        return

    for i in range(n):
        if(chars[i] in str):
            continue
        newstr = str + chars[i]
        combinations(chars, newstr, n, k - 1)

combinations(chars, "", len(chars), length) 

for y in comb:
    alpha = True
    val = 0
    for i in range(length-1):
        if(y[i]>y[i+1]):
            alpha = False
    for z in y:
        val+=charval[z]
    if(val==lucky and alpha):
        print(y)