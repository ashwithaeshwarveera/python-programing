nums = [1,4,9,16,25,36,49,64,81,100]
x = 81
indx = 0
while indx < len(nums):
    if (nums[indx] == x):
        print("the num found:",x)
        break
    else:
        print("finding...")
    indx += 1    

for i in range (1, 11):
    if ( i == 6 ):
        print("found:",6)
        break

nums = [1,2,3,4,5,6,7,8,9,10]
for indx in nums:
    if ( indx % 2 == 0):
        print("the num is found:",indx)
        break
else:
   print("the num is not found:")



while True :
    user_input = input("enter 'ashwitha' to stop:")
    if user_input == 'ashwitha':
        print("you entered ashwitha")
        break
    print("you entered:", user_input)

