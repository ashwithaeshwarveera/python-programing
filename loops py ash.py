#loops (iteration statements)

#for loop
for i in range(1,7):
    print(i)
#in python range will be executed from 1 to 6
"""
when we want to repeat same lines of code multiple times we use loops
"""
count=0
while count<=10:
    print(count)
    count+=1
marks=10
while marks!=0:
    mark=int(input("enter marks"))
    if marks>90:
        print("grade A")
    elif marks>80:
        print("grade B")
    elif marks>50:
        print("grade c")
    else:
        print("fail")
