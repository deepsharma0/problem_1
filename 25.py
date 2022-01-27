num = int(input("Enter a number that you want to check: "))
i = 0
m = 1
j = 1
fib = [0,1]
while j<=num:
    j+=i
    i = m
    m = j
    if j>num:
        break
    fib.append(j)
##print(fib)

if num == fib[-1]:
    print("your number is a fibbonaci number.")
else:
    print("your number is not a fibonnaci number.")    
    