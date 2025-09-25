#slicing
fruits = ['apple','mango','banana','orange','grapes']
print(fruits[1:3])



fruits = ['apple','mango','banana','orange','grapes']
print(fruits[:4])
print(fruits[2:])

#step slicing

fruits = ['apple','mango','banana','orange','grapes']
print(fruits[::2])


#reverse tuple

fruits = ['apple','mango','banana','orange','grapes']
print(fruits[::-1])


#index_metosd
fruits = ['apple','mango','banana','orange','grapes']
index_apple = fruits.index('apple')
print(index_apple)


#counting method
nums = (1,2,3,4,3,2,3,3,5,3)
count_3 = nums.count(3)
print(count_3)
