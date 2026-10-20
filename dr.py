#Programa za zadanie 1 zad. 2
n=int(input("Enter a number: "))
i=1
while i<n:
    if n%i==0 and i%2==1:
        print(i)
    i+=1
