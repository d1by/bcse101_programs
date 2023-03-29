inp_list = eval(input("Enter list: "))

#fixing age:name
for member in inp_list:
    for key in member:
        if(type(key)==int):
            inp_list.append({member[key]:key})
            inp_list.remove(member)

#same age
for member in inp_list:
    for key in member:
        age = member[key]

        for member2 in inp_list:
            if(member2==member):
                continue

            for key2 in member2:
                age2 = member2[key2]
                if(age2==age):
                    newstr = key+key2
                    temp=[]
                    temp.append({newstr:round(age**(1/3))})
                    inp_list.remove(member)
                    inp_list.remove(member2)
                    for k in inp_list:
                        temp.append(k)
                    inp_list=[]
                    for k in temp:
                        inp_list.append(k)

#same name
for member in inp_list:
    for key in member:

        for member2 in inp_list:
            if(member2==member):
                continue

            for key2 in member2:
                if(key2==key):
                    temp=[]
                    temp.append({key:(str(member[key])+str(member2[key2]))})
                    inp_list.remove(member)
                    inp_list.remove(member2)
                    for k in inp_list:
                        temp.append(k)
                    inp_list=[]
                    for k in temp:
                        inp_list.append(k)                    

print(inp_list)