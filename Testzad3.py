n = input("Enter a number: ")
sum=0
if int(n) <= 0:
    while int(n) <= 0:
        n = input("Enter a number: ")
z = len(n)
i = 0
while i != z:
    sum += int(n[i])
    i += 1
print("The sum of the numbers is: ", sum)
t=0
while z != 0:
    t += int(n[z]*(10**z))
print ("The number in reverse order is: ", t)
if n== str(t):
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")


