nums = [1,-5,6,3,-8,-9,4,5,2,0]
for val in nums :
    if val < 0 :
        continue
    print("nums",val)
        
 
nums = [1,-5,6,3,-8,-9,4,5,2,0]
nums = [nums for nums in nums if nums >= 0]







N = [1,3,4,6,9,28,7,18,9]
for num in N:
  if num%3 == 0:
    continue
  print(num)

