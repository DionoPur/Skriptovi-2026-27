n=int(input("Enter a the amount: "))
n2=0
i=0
n3=0
n1=[i for i in range(n)]
if n==0:
    print("Невалиден брой ")
else:
    while n>0:
        n1[i]=int(input("Enter a number: "))
        i+=1
        n-=1

    while n>0:
        if n1[i]%2==0:
            n2+=n1[i]
        i+=1
        n-=1
    print("The sum of even numbers is: ", n2)
    while n>0:
        if n1[i]%2!=0 and n1[i]>n3:
            n3=n1[i]
        i+=1
        n-=1
        if n==0 and n3==0:
            print("Няма нечетни")
        else:
            print("The largest odd number is: ", n3)



