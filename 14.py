import os

n = int(input("Enter number of customers: "))
bill_list = []

for i in range(n):
    custid = input("Enter customer ID: ")
    m = int(input("Enter number of products: "))
    for j in range(m):
        prod = input("Enter product: ")
        quan = int(input("Enter quantity: "))
        price = int(input("Enter price: "))
        total = quan*price
        bill_list.append([custid, prod, quan, price, total])

def totalamt(custid, inplist):
    for x in inplist:
        if(x[0]==custid):
            return x[4]
    return 0

def maxmin():
    maxprod = bill_list[0][1]
    maxprodnum = bill_list[0][2]
    minprod = bill_list[0][1]
    minprodnum = bill_list[0][2]
    
    for x in bill_list:
        if(x[2]>maxprodnum):
            maxprodnum = x[2]
            maxprod = x[1]
        if(x[2]<minprodnum):
            minprodnum=x[2]
            minprod = x[1]
    
    print(maxprod)
    print(minprod)

def maxord():
    maxcount=0
    mincount=0
    maxcust=''
    mincust=''
    for x in bill_list:
        count=0
        for y in bill_list:
            if(x[0]==y[0]):
                count+=1
        if(count>maxcount):
            maxcount=count
            maxcust=x[0]
        if(count<mincount):
            mincount=count
            mincust=x[0]
    
    print(maxcust)
    print(mincust)

print("\n")

totsum=0
new_bill_list=[]
for j in bill_list:
    new_bill_list.append(j)

for k in range(len(new_bill_list)):
    i=new_bill_list[0]
    totsum+=totalamt(i[0], new_bill_list)
    print(i[0], totalamt(i[0], new_bill_list))
    new_bill_list.remove(i)

print("\n")
maxmin()
print("\n")
maxord()

file1 = open('bill.txt', 'w')
for order in bill_list:
    file1.writelines(str(order)+"\n")
file1.writelines("Total amount: Rs" + str(totsum))

file1.close()