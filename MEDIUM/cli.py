from PIL import Image
availableitems=['asus zenfone','honor 7a','samsung galaxy s9','oppo f9','vivo v11']
price=['10000','11000','9000','50000','15000']
price=list(map(int,price))
print("the cost of each items are listed below respectively")
print(availableitems)
print(price)
n=int(input("how many products do you want to buy? "))
c=[]
while (len(c)!=n):
      citems=input("enter product ")
      c.append(citems)
s=0
for i in range(0,n):
    if (c[i]==availableitems[0]):
        s=s+price[0]
    elif (c[i]==availableitems[1]):
        s=s+price[1]
    elif (c[i]==availableitems[2]):
        s=s+price[2]
    elif (c[i]==availableitems[3]):
        s=s+price[3]
    elif (c[i]==availableitems[4]):
        s=s+price[4]
print("proceeding to checkout...")
print("the total amount payable is "+str(s))
x=input("do you have any coupon? ")
if x=="yes":
    s=s-(s*0.04)
    print("the total amount payable after discount is "+str(s))
else:
    print("the total amount payable after discount is "+str(s))
print("Choose a payment option:\n1)credit card\n2)debit card\n3)net banking")
img=Image.open("1.jpg")
img.show()
img.close()
