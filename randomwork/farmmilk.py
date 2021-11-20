nofrm = int(input("enter number of farms "))
i = 0
litsum = 0
mlsum = 0
while i < nofrm:
    milk = str(input("enter amount of milk in litres and ml "))
    milkval = milk.split()
    lit = int(milkval[0])
    ml = int(milkval[2])
    litsum+=lit
    mlsum+=ml
    i = i+1

print("total amount of milk from",nofrm,"is",litsum,"litres", mlsum,"ml")