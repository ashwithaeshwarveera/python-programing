#arrays
#integer array
import array
nums = array.array('i',[1,2,3,4,])
print(nums)


#float array
import array
float = array.array('f',[1.1,2.2,3.3])
print(float)


##operations of array
#accesing of elements
import array
nums = array.array('i',[10,20,30,40])
print(nums[0])
print(nums[-1])


#slicing

nums = array.array('i',[10,20,30,40])
print(nums[:3])
print(nums[1:2])


#adding of elements

nums = array.array('i',[1,2,3,])
nums.append(4)
print(nums)


#buildings
nums = array.array('i',[1,2,3,4,5,6,7,8,9])
print(nums)
print(len(nums))                   
print(sum(nums))
print(max(nums))
print(min(nums))


#insert at specific index - .insert(index,value)
nums = array.array('i',[10,20,30,40])
nums.insert(2,50)
print(nums)

#removing element
nums = array.array('i',[10,20,30,40])
nums.remove(30)
print(nums)

#removing from index
del nums[2]
print(nums)



















