anskey = ['A', 'B', 'B', 'A', 'C']

num = int(input("Enter number of students: "))
allans = []

for i in range(1,num+1):
    ans=input("Enter answers for candidate %d separated by a space: "%i).split()
    allans.append(ans)

allmarks=[]
for x in allans:
    marks=0
    for j in range(len(x)):
        if(x[j]==anskey[j]):
            marks+=2
        elif(x[j]=="X"):
            continue
        else:
            marks-=0.25
    allmarks.append(marks)

allmarks2=[]
for z in allmarks:
    allmarks2.append(z)

print("Rank\tCandidate(s)\tTotal")
for m in range(len(allmarks2)):
    if(allmarks==[]):
        break
    m+=1
    maxval = max(allmarks)
    maxcan = "C" + str(allmarks2.index(maxval)+1)
    for n in range(len(allmarks2)):
        if(allmarks2[n]==maxval):
            if(n!=allmarks2.index(maxval)):
                maxcan+=",C" + str(n+1)
                allmarks.remove(maxval)
    print(m, "\t", maxcan, "\t\t", maxval)
    allmarks.remove(maxval)