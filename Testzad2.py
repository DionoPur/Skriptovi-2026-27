i=0
n=[input("Enter a number: ") for i in range(100)]
n[i] = int(input("Enter a number: "))
sum=0
check=0

if int(n[i]) > 0:
    while n[i] > 0:
        n[i] = int(input("Enter a number: "))
        if n[i] < 0:
            if n[i]==n[0]:
                print(" Няма данни.")
            remove(n[i])
            break
        i += 1
    z=len(n)
    while i!=z:
        sum += n[i]
        i += 1
    print("The sum of the numbers is: ", sum)
    while i!=z:
        if n[i]>9 and n[i]<100:
            check += 1
    print("The number of two-digit numbers is: ", check)
    print("The average of the numbers is: ", sum/len(n))
else:
    print("Няма данни.")
    
