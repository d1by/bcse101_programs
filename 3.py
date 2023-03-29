illegal = False
inp_list = eval(input("Enter list (Max of 2 strings, complex types, integer types): "))
#counting types
cstr=0; ccmplx=0; cint=0;
for x in inp_list:
    if(type(x)==str):
        cstr+=1
    elif(type(x)==int):
        cint+=1
    elif(type(x)==complex):
        ccmplx+=1
    else:
        print(x, " isn't string, complex, or integer type. ")
        illegal = True
        break

if(cstr>2 or cint>2 or ccmplx>2 or illegal or cstr==0 or cint==0 or ccmplx==0):    
    print("Invalid data. ")
    exit()

#useful functions
def checkPrime(n):
    if(n<=0):
        return False
    
    prime=True
    for i in range(n):
        if(i==0 or i==1):
            continue
        if(n%i==0):
            prime=False
            break

    return prime

def checkPalindrome(n):
    n = n.lower()
    return n==n[::-1]

con1=False; con2=False;
for i in range(len(inp_list)):
    if(type(inp_list[i])==int):
        if checkPrime(inp_list[i]):
            con1 = True
    elif(type(inp_list[i])==str):
            if checkPalindrome(inp_list[i]):
                con2 = True

if(con1 and not con2):
    for i in range(len(inp_list)):
        if(type(inp_list[i])==str):
            inp_list[i] = inp_list[i][::-1]
        elif(type(inp_list[i])==complex):
            inp_list[i] = complex(inp_list[i].imag, inp_list[i].real)
    
    print(inp_list)

elif(con2 and not con1):
    for i in range(len(inp_list)):
        if(type(inp_list[i])==complex):
            inp_list[i] = complex(inp_list[i].real, -1*inp_list[i].imag)
        elif(type(inp_list[i])==int):
            inp_list[i] = -1 * inp_list[i]
    
    print(inp_list)

elif(con1 and con2):
    mid = int(len(inp_list)/2)

    if(len(inp_list)%2==0):
        print(inp_list[mid-1], inp_list[mid])
    else:
        print(inp_list[mid])        


else:
    new_list=[]
    for i in range(len(inp_list)):
        if(type(inp_list[i])==str):
            for j in list(inp_list[i]):
                new_list.append(j)
        else:
            new_list.append(inp_list[i])

    print(new_list)