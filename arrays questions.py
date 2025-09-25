#1.
import array
nums = array.array('i',[1,2,3,4,5,6,7,8,9])
print(nums[0])
print(nums[-1])


#2.

nums = array.array('i',[1,2,3,4,5,6,7,8,9])
print(nums[2:5])

#3.

nums = array.array('i',[1,2,-3,-4,-5,-6,7,8,9])
print(nums[-6:-2])



#4.

nums = array.array('i',[1,2,3,4,5,6,7,8,9])
print(nums[::2])


#5.
nums = array.array('i',[5,10,15,20,25,30])     
x = nums[:4]
sum = 0
for val in x :
    sum += val
print('sum:',x)
print('sum:',sum)

#6.
nums = array.array('i',[1,2,3,4,5,6,7,8,9])
print(nums[::-1])
