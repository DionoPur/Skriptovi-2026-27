#Program for Fibonachi numbers up to n
n=int(input("Enter a number: "))
p1=1
p2=0
p3=0
pd = []
while p2<n:
    pd.append(p2)
    p3=p1+p2
    p1=p2
    p2=p3
print(pd)
