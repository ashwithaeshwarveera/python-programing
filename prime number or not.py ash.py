num = int(input("enter a num:"))  # num=13
count = 0
for i in range(1, num+1):
    if (num % i == 0):  # 13%1==0,13%2!=0,13%3!=0,13%13==0
        count += 1

if (count == 2):
    print("the given num is a prime num")
else:
    print("the given num is not prime num")
