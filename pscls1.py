# 1. Check prime or not
a=int(input("Enter the number: "))
count=0
for i in range(1,a+1):
    if a%i==0:
        count+=1
if count==2:
    print("prime")
else:
    print("not prime")


a = 11
count = 0
for i in range(2, (a // 2) + 1):
    if a % i == 0:
        count += 1
if count == 0:
    print("Prime")
else:
    print("Not prime")


# 2. Check a number is perfect square
n = 16
for i in range(1, n):
    if i * i == n:
        print("Perfect square")
        break
else:
    print("Not a perfect square")

# 3. Check a number is sunny or not
n=16
for i in range(1,n+1):
    if i*i==n+1:
        print("sunny number")
        break
else:
    print("Not a sunny number")

#4. sum of digits in a number
n=103
sum=0
while n>0:
    digit=n%10
    sum+=digit
    n//=10
print(sum)

# 5. count of digits in a number
n=1034
count=0
while n>0:
    count+=1
    n//=10
print(count)

# 6. reverse of a number
n=124
reverse=0
while n>0:
    digit=n%10
    reverse=reverse*10+digit
    n//=10
print(reverse)

# 7. print each digit individually
n = int(input("Enter the number: "))
rev = 0
temp = n
while temp > 0:
    rev = rev * 10 + (temp % 10)
    temp //= 10
while rev > 0:
    print(rev % 10)
    rev //= 10

# 8. Check a number is palindrome or not 
n = 124
temp = n       
reverse = 0
while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n //= 10
if reverse == temp:
    print("Palindrome")
else:
    print("Not a palindrome")

# 9. Print the prime numbers from m to n:
m = 1500
n = 2500
for i in range(m, n + 1):
    if i > 1:
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                break
        else:
            print(i)






