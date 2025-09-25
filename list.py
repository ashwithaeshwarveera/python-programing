#list
fruits = ["apple","banana","orange","grapes"]
print(fruits)



#adding to list
fruits = ["apple","banana","orange","grapes"]
fruits.append("mango")
print(fruits)


#remove to list
fruits = ["apple","banana","orange","grapes"]
fruits.remove ("orange")
print(fruits)

#changing to list
fruits = ["apple","banana","orange","grapes"]
fruits[2] == "pine apple"
print(fruits)

#access elements to list
fruits = ["apple","banana","orange","grapes"]
print(fruits[0])
print(fruits[1])


#sort the list
nums=[8,9,7,6,0,3,2]
nums.sort()
print(nums)

cartoon=["doramon","nobitha","shizuka","jian","suneo"]
x = "nobitha"
indx=0
while indx<len(cartoon):
    if (cartoon[indx] == x):
        print("x is present in cartoon")
    else:
        print("x not present in cartoon")
    indx+=1




cartoon=["doramon","nobitha","shizuka","jian","suneo"]
x = "nobitha"
if x in cartoon:
    print("x is present in cartoon")
else:
    print("x not present in cartoon")
    











