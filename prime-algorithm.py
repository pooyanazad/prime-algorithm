n=int(input("Enter your number: "))
l = []
for i in range (2,n):
    if n%i==0:
        l.append(i)
if len(l) == 0 :
    print("Its Prime")
else:
    print("its devided by " + str(l))
