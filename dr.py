#Program for all deviders of n that are odd
n=int(input("Enter a number: "))
i=1
while i<n:
    if n%i==0 and i%2==1:
        print(i)
    i+=1